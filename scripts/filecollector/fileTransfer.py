#!/usr/bin/env python

import os, time, sys, shutil, glob, re, commands
from commonAnTS import *
if len(sys.argv)<=1 or not os.path.exists(sys.argv[1]):
  print "No valid configuration file"
  sys.exit()
execfile(sys.argv[1])
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

################################################################################
def getFileLists():
  newfiles={}
  trashfiles=[]
  filelist=[]
  for dir1, subdirs, files in os.walk(REGISTERED_DIR):
    for f in files:
      try:
        version=int(f.split("_V")[-1][:4])
        vlfn=f.split("_V")[0]+f.split("_V")[1][4:]
      except:
        version=1
        vlfn=f

      if vlfn not in newfiles.keys():
        newfiles[vlfn]=(version,"%s/%s" % (dir1,f))
      elif version > newfiles[vlfn][0]:
        trashfiles.append(newfiles[vlfn][1])
        newfiles[vlfn]=(version,"%s/%s" % (dir1,f))
      else:
        trashfiles.append("%s/%s" % (dir1,f))
  print "Found %d new files that will be registered, and %d files that will be %s" % (len(newfiles),len(trashfiles),(EMPTY_DONEDIR and "Erased" or "Skipped and sent to done")) 
  return (newfiles,trashfiles)
#=====================================================================================
def injectFile(f,renotify=False):
  fname=f.rsplit("/",1)[-1]
  run=f.split("_R")[-1][:9]
  iname="%s/%s" % (INJECTION_DIR,fname)
  shutil.move(f,iname)
  parameters=[TEST and "--test" or " ",
              #renotify and "--renotify" or " ",
              "--filename %s" % fname,
              "--type dqm",
              "--path %s" % INJECTION_DIR,
              "--destination dqm",
              "--hostname %s" % TRANSFER_HOSTNAME,
              "--config %s" % TRANSFER_CONFIGFILE,
              "--runnumber %s" % run,
              "--lumisection 95",
              "--numevents 834474816",
              "--appname ANTS",
              "--appversion ANTS_1_0"]
  cmd="%s %s" % (INJECTIONSCRIPT," ".join(parameters))
  result = commands.getstatusoutput(cmd)
  if result[0] >= 1:
    output = result[1]
    print "Error injecting file %s to transfer system checking if it exists" % f
    chkparameters=["--check","--filename %s" % fname,"--config %s" % TRANSFER_CONFIGFILE]
    cmd="%s %s" % (INJECTIONSCRIPT," ".join(chkparameters))
    result = commands.getstatusoutput(cmd)
    if result[0]==1:
      if "File not found in database" in result[1]:
        print "Error: file %s not found in transfer database, check configuration" % f
        return 0
      else:
        print "Warning: file %s already exists in transfer database" % f
	return 2
    else:
      if "File found in database" in result[1]:
        print "Warning: file %s already exists in transfer database" % f
	return 2
      else:
        print "Error: problem checking database entry for file %s\nAppError:%s" % (f,result[1])
        return 0
  else:
    print "File %s injected successfully" % f
  return 1
#=====================================================================================
def transferFiles():
  while True:
    #look for NEW files in REGISTERED_DIR and files that need to be cleared.
    newfiles,trashfiles=getFileLists() 
    
    #Making sure destination directories exist
    if not os.path.exists(DONE_DIR):
      os.makedirs(DONE_DIR)
    if not os.path.exists(INJECTION_DIR):
      os.makedirs(INJECTION_DIR)
    if not os.path.exists(JUNK_DIR):
      os.makedirs(JUNK_DIR)
    
    #Dealing with trash can  
    for tf in trashfiles:
      if EMPTY_DONEDIR:
        os.remove(tf)
      else:
        runnr=tf.split("_R")[-1][:9]
        ftdir="%s/%s/%s" % (DONE_DIR,runnr[:3],runnr[3:6])
        if not os.path.exists(ftdir):
          os.makedirs(ftdir)
        tfname="%s/%s" % (ftdir,tf.rsplit("/",1)[-1])
        if os.path.exists(tfname):
          ftdir="%s/%s/%s" % (JUNK_DIR,runnr[:3],runnr[3:6])
          tfname="%s/%s" % (ftdir,tf.rsplit("/",1)[-1])
        shutil.move(tf,tfname)
        
    #Down to bussines
    for key in sorted(newfiles.keys())[::-1]:
      ver,f=newfiles[key]
      ifr=injectFile(f)
            
    time.sleep(TRANSFERRER_WAIT_TIME)
#=====================================================================================
if __name__ == "__main__": 
  transferFiles()
