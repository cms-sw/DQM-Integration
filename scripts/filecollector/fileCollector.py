#! /usr/bin/env python

import os,time,sys,glob,zipfile,re,shutil,stat
from commonAnTS import *
if len(sys.argv)<=1 or not os.path.exists(sys.argv[1]):
  print "No valid configuration file"
  sys.exit()
execfile(sys.argv[1])
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
def filecheck(rootfile):
  cmd = EXEDIR + '/filechk.sh ' + rootfile
  a = os.popen(cmd).read().split()
  tag = a.pop()
  if tag == '(int)(-1)':
    DEBUG and debugMsg(1,"File %s corrupted" % rootfile)
    return 0
  elif tag == '(int)0':
    DEBUG and debugMsg(1, "File %s is incomplete" % rootfile)
    return 0
  elif tag == '(int)1':
    DEBUG and debugMsg(0, "File %s is OK" % rootfile)
    return 1
  else:
    return 0
     
def convert(infile, ofile):
  cmd = EXEDIR + '/convert.sh ' + infile + ' ' +ofile
  os.system(cmd)

####### ENDLESS LOOP WITH SLEEP
while True:
  NRUNS = 0  #Number of runs found
  NFOUND = 0  #Number of files found
  NEW = {}
  TAGS= []
  #Dealing with .ig files
  ignames=sorted(glob.glob("%s/*.ig" % COLLECTING_DIR))
  for igfile in ignames:
    if re.search("_R[0-9]{9}",igfile):
      runstr=igfile.split("_R")[-1][:9]
      destdir="%s/%s/%s" % (IG_FILE_DROPBOX,runstr[:3],runstr[3:6])
      destfile="%s/%s" % (destdir,igfile.rsplit("/",1)[-1])
      if not os.path.exists(destdir):
        os.makedirs(destdir)
      shutil.move(igfile,destfile)
      os.chmod(destfile,stat.S_IREAD|stat.S_IRGRP|stat.S_IROTH| stat.S_IWRITE|stat.S_IWGRP|stat.S_IWOTH)
    else:
      destfile="%s/%s" % (OLD_IG_FILES,igfile.rsplit("/",1)[-1])
      ref=1
      ndestfile=destfile
      while os.path.exists(ndestfile):
        ndestfile="%s-%03d.ig" %(destfile.split(".ig")[0],ref)
        ref+=1	
      shutil.move(igfile,ndestfile)
      debugMsg(1, "file %s is not a standar name file, saved in %s directory for manual handeling" % (igfile,OLD_IG_FILES))
  for dir, subdirs, files in os.walk(COLLECTING_DIR):
    for f in files:
      if re.match('^DQM_.*_R[0-9]*_T[0-9]*\.root$', f) or re.match('^Playback_.*_R[0-9]*_T[0-9]*\.root$', f):
        runnr = long(f[f.rfind("_R")+2:f.rfind("_T")])
        subsystem=f.split("_")[2]
        runstr="%09d" % runnr
        donefile = "%s/%s/%s/%s" % (T_FILE_DONE_DIR, runstr[0:3], runstr[3:6], f)
        f = "%s/%s" % (dir, f)
        if os.path.exists(donefile) and os.stat(donefile).st_size == os.stat(f).st_size:
          debugMsg(1, "File %s was already processed but re-appeared" % f)
          os.remove(f)
          continue
        NEW.setdefault(runnr, {}).setdefault(subsystem,[]).append(f)
        NFOUND += 1  
  if len(NEW.keys()) == 0:
    time.sleep(COLLECTOR_WAIT_TIME)
    continue
      
  TAGS=sorted(glob.glob('%s/tagfile_runend_*' % COLLECTING_DIR ),reverse=True)
  if len(TAGS)==0:
    if len(NEW.keys()) <= 1:
      time.sleep(COLLECTOR_WAIT_TIME)
      continue
    debugMsg(0, 'No tagfile_runend foud, checking for *_T files that could have been left behind')
    TAGRUNEND=long(sorted(NEW.keys(),reverse=True)[1])
  else:
    TAGRUNEND=long(TAGS[0].split("_")[2])
    
  for tag in TAGS:
    os.remove(tag)

  for run,subsystems in NEW.items():
    if run <= TAGRUNEND:
      for subsystem,files in  subsystems.items():
        done=False
        keeper=0
        Tfiles=sorted(files,reverse=True)
        for Tfile in Tfiles:
          version=len(glob.glob("%s/DQM_V*_%s_R%09d.root" % (DROPBOX,subsystem,run)))+1
          finalTMPfile="%s/DQM_V%04d_%s_R%09d.root" % (TMP_DROPBOX,version,subsystem,run)
          finalfile="%s/DQM_V%04d_%s_R%09d.root" %   (DROPBOX,version,subsystem,run) 
          runstr="%09d" % run
          finalTfile="%s/%s/%s/%s" % (T_FILE_DONE_DIR,runstr[0:3],runstr[3:6],Tfile.split("/")[-1])
          finalTsubdir="%s/%s" % (T_FILE_DONE_DIR,runstr[0:3])
          finalTdir="%s/%s/%s" % (T_FILE_DONE_DIR,runstr[0:3],runstr[3:6])
          if not os.path.exists(finalTsubdir):
            os.makedirs(finalTsubdir)
          if not os.path.exists(finalTdir):
            os.makedirs(finalTdir)
          if os.path.exists(finalTMPfile):
            os.remove(finalTMPfile)
          if not done:
            if filecheck(Tfile) == 1:
              if "Playback" in Tfile:
                dqmfile = Tfile.replace('Playback','DQM')
                convert(Tfile,dqmfile)
                os.rename(Tfile,finalTfile.replace('Playback','Playback_full'))
                Tfile=dqmfile  
              for i in range(RETRIES):
                shutil.copy(Tfile,finalTMPfile)
                if os.path.exists(finalTMPfile) and os.stat(finalTMPfile).st_size == os.stat(Tfile).st_size:
                  os.rename(Tfile,finalTfile)
                  os.rename(finalTMPfile,finalfile)
                  os.chmod(finalfile,stat.S_IREAD|stat.S_IRGRP|stat.S_IROTH| stat.S_IWRITE|stat.S_IWGRP|stat.S_IWOTH)  
                  break
                else:
                  body = "Problem transfering final file for run %09d\n Retrying in %d" % (run,COLLECTOR_WAIT_TIME)
                  debugMsg(2, body)
                  if i == RETRIES-1: sendmail(YourEmail,run,body,subject="Error tranfering file to filer")
                  time.sleep(COLLECTOR_WAIT_TIME)
              done=True
            else:
              DEBUG and debugMsg(0, "file %s is incomplete looking for next DQM_V*_%s_R%09d_T*.root valid file" % (Tfile,subsystem,run))
              if keeper == 0:
                keeper+=1
                shutil.move(Tfile,finalTfile+"_d")
              else:
                os.remove(Tfile) #
                
          else:
            if keeper == 0:
              keeper+=1
              shutil.move(Tfile,finalTfile+"_d")
            else:
              os.remove(Tfile) #
  #continue
      
  
