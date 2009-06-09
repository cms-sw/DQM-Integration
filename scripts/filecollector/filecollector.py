#! /usr/bin/env python

import os,time,sys,glob,zipfile
from sets import Set

#set environments
exedir = '/nfshome0/dqm/filecopy' # directory to execute the relevant scripts
YourEmail='lilopera@cern.ch'
DIR = '/home/dqmprolocal/output'  #directory to search new files
TMPDIR = '/dqmdata/dqm/.dropbox_tmp' # stealth area on cmsmon
FILEDIR = '/dqmdata/dqm/dropbox' # directory, to which files are stored
TFILEDONEDIR = '/home/dqmprolocal/done' # directory to store *_T files once they have been processed
IGFILEDIR = '/dqmdata/EventDisplay' #Directory to store ig Files.
WAITTIME = 120 # waiting time for new files (sec)
RETRIES = 3

def filecheck(rootfile):
	cmd = exedir + '/filechk.sh ' + rootfile
	a = os.popen(cmd).read().split()
	tag = a.pop()

	if tag == '(int)(-1)':
		#print "File corrupted"
		return 0
	elif tag == '(int)0':
		#print "File is incomplete"
		return 0
	elif tag == '(int)1':
		#print "File is OK"
		return 1
	else:
		return 0
	
def sendmail(EmailAddress,run):
	sever=os.getenv("HOSTNAME")
  s=smtplib.SMTP("localhost")
  tolist=[EmailAddress, "lat@cern.ch"]
  body="File copy to dropbox failed by unknown reason for run:%09d on server: %s" % (run,server)
  msg = MIMEText(body)
  msg['Subject'] = "File merge failed."
  msg['From'] = ServerMail
  msg['To'] = EmailAddress
  s.sendmail(ServerMail,tolist,msg.as_string())
  s.quit()
		
def convert(infile, ofile):
	cmd = exedir + '/convert.sh ' + infile + ' ' +ofile
	os.system(cmd)

####### ENDLESS LOOP WITH SLEEP
while True:
  NRUNS = 0	#Number of runs found
  NFOUND = 0  #Number of files found
  NEW = {}
  TAGS= []
  for dir, subdirs, files in os.walk(DIR):
    for f in files:
      if re.match('^DQM_.*_R[0-9]*_T[0-9]*\.root$', f) or re.match('^Playback_.*_R[0-9]*_T[0-9]*\.root$', f):
        runnr = long(f[f.find("_R")+2:f.find("_T")])
        donefile = "%s/%s/%s/%s" % (TFILEDONEDIR, runnr[0:3], runnr[3:6], f)
        f = "%s/%s" % (dir, f)
        if os.path.exists(donefile) and os.stat(donefile).st_size == os.stat(f).st_size:
          print "WARNING: %s was already processed but re-appeared" % f
          os.remove(f)
          continue
        NEW.setdefault(runnr, []).append(f)
        NFOUND += 1  
        
  TAGS=sorted(glob.glob('%s/tagfile_runend_*' % DIR ),reverse=True)
  if len(TAGS)==0:
    if len(NEW.keys()) <= 1:
      print 'waiting for new files to process...'
      time.sleep(WAITTIME)
      continue
    print 'No tagfile_runend foud, checking for *_T files that could have been left behind'
    TAGRUNEND=long(sorted(NEW.keys(),reverse=True))[1])
  else:
  	TAGRUNEND=long(TAGS[0].split("_")[2])
  
  for tag in TAGS[1:]
  for run,files in NEW.items()
    if run <= TAGRUNEND:
      done=False
      Tfiles=sorted(files,reverse=True)
      for Tfile in Tfiles:
      	subsystem=Tfile.split("_")[2]
      	version=len(glob.glob("%s/DQM_V*_%s_R%09d.root" % (FILEDIR,subsystem,run)))+1
      	finalTMPfile="%s/DQM_V%04d_%s_R%09d.root" % (TMPDIR,version,subsystem,run)
      	finalfile="%s/DQM_V%04d_%s_R%09d.root" %   (FILEDIR,version,subsystem,run)
      	fpTfile="%s/%s" % (DIR,Tfile)
      	runstr="%09d" % run
      	finalTfile="%s/%s/%s/%s" % (TFILEDONEDIR,runstr[0:3],runstr[3,6],Tfile)
      	if os.path.exists(finalTMPfile):
      		os.remove(finalTMPfile)
      	if not done:
        	if filecheck(fpTfile) == 0:
        		if "Playback" in fpTfile:
        			dqmfile = fpTfile.replace('Playback','DQM')
  					  convert(fpTfile,dqmfile)
  					  os.rename(fpTfile,finalTfile)
  					  fpTfile=dqmfile
        		os.copy(fpTfile,finalTMPfile)
        		for i in range(RETRIES):
          		if os.path.exists(finalTMPfile) and os.stat(finalTMPfile).st_size == os.stat(fpTfile).st_size:
          			os.rename(fpTfile,finalTfile)
          			os.rename(finalTMPfile,finalfile)
          			
          			break
          		else:
          			print "Problem transfering final file for run %09d\n Retrying in %d" % (run,WAITTIME)
          			if i == RETRIES-1: sendMail(YourEmail,run)
          			time.sleep(WAITTIME)
   
        	else:
        		print "file %s is incomplete looking for next DQM_V*_%s_R%09d_T*.root valid file" % (fpTfile,subsystem,run)
        		os.rename(fpTfile,finalTfile)
        else:
        	os.rename(fpTfile,finalTfile)
  
  #Dealing with .ig files
  NEWIGF = {}
  ignames=sorted(glob.glob("*.ig"))
  igfready=[]
  for i in range(len(ignames)):
  	try:
  		os.rename("%s/%s" % (DIR,ignames[i]),"%s/tmp_%s" % (DIR,ignames[i]))
  		igfready.append(ignames[i])
  	except:
  		pass

  for igfile in igfready:
  	igf=zipfile.ZipFile("%s/%s" % (DIR,igfile),'r')
  	namelist=sorted(igf.namelist())
  	igf.close()
  	runnr=long(namelist[0].split("/")[1].split("_")[1])
  	NEWIGF.setdefault(runnr, []).append(igfile)
  
  for run , files in NEWIGF.items():
   	weeknumber=long(time.strftime("%W"))+1
  	date=time.strftime("%Y%m%d")
		i=0
		for igfile in files: 
	  	tmpdestigfile="%s/iSpyProd_%02d_%s_R%09d_%03d.ig" (TMPDIR,weeknumber,date,run,i)
      destigfile="%s/iSpyProd_%02d_%s_R%09d_%03d.ig" (IGFILEDIR,weeknumber,date,run,i)
      fpigfile="%s/%s" (DIR,igfile)
      i+=1
      os.copy(fpigfile,tmpdestigfile)
  		for i in range(RETRIES):
    		if os.path.exists(tmpdestigfile) and os.stat(tmpdestigfile).st_size == os.stat(fpigfile).st_size:
    			os.rename(tmpdestigfile,destigfile)
    			os.remove(fpigfile)
    			break
    		else:
    			print "Problem transfering final ig file for run %09d\n Retrying in %d" % (run,WAITTIME/2)
    			if i == RETRIES-1: sendMail(YourEmail,run)
    			time.sleep(WAITTIME/2)
