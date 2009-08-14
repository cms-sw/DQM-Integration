#!/usr/bin/env python

import os, time, sys, shutil, glob, smtplib, re, commands
import getopt as gop
import zipfile as zp
from datetime import datetime
from email.MIMEText import MIMEText

SOURCEDIR = "/dqmdata/dqm/registered" #Directory where the original files are located.
INJECTIONDIR = "/dqmdata/dqm/Tier0Shipping/inject"   #Directory where files get placed once they have been sent.
VERIFYDIR= "/dqmdata/dqm/Tier0Shipping/verify"
DONEDIR = "/dqmdata/dqm/done/merged"
JUNKDIR = "/dqmdata/dqm/junk"
HOSTNAME = "srv-C2D05-19"
CONFIGFILE = "/nfshome0/dqm/.transfer/myconfig.txt"
INJECTIONSCRIPT = "/nfshome0/tier0/scripts/injectFileIntoTransferSystem.pl"

EMPTY_DONEDIR = False
WAIT_TIME = 600
################################################################################
def getFileLists():
  newfiles={}
  trashfiles=[]
  filelist=[]
  for dir1, subdirs, files in os.walk(SOURCEDIR):
    for f in files:
      try:
        version=int(f.split("_V")[-1][:4])
        vlfn=f.split("_V")[0]+f.split("_V")[1][4:]
      except:
        version=1
        vlfn=f
      if vlfn in newfiles.keys() and version >= newfiles[vlfn][0]:
        newfiles[vlfn]=(version,"%s/%s" % (dir1,f))
      elif vlfn not in newfiles.keys():
        newfiles[vlfn]=(version,"%s/%s" % (dir1,f))
      else:
        trashfiles.append("%s/%s" % (dir1,f))
  print "Found %d new files that will be registered, and %d files that will be %s" % (len(newfiles),len(trashfiles),(EMPTY_DONEDIR and "Erased" or "Skipped and sent to done"))
  return (newfiles,trashfiles)
#=====================================================================================
def injectFile(f,renotify=False):
  fname=f.rsplit("/",1)[-1]
  dname=f.rsplit("/",1)[0]
  run=f.split("_R")[-1][:9]
  iname="%s/%s" % (INJECTIONSCRIPT,fname)
  shutil.move(f,iname)
  parameters=[#"--test",
              "--filename %s" % fname,
              "--type dqm",
              "--path %s" % INJECTIONSCRIPT,
              "--destination dqm",
              "--hostname %s" % HOSTNAME,
              "--config %s" % CONFIGFILE,
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
    chkparameters=["--check","--filename %s" % fname,"--config %s" % CONFIGFILE]
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
    #look for NEW files in SOURCEDIR and files that need to be cleared.
    newfiles,trashfiles=getFileLists() 
    
    #Making sure destination directories exist
    if not os.path.exists(DONEDIR):
      os.makedirs(DONEDIR)
    if not os.path.exists(INJECTIONDIR):
      os.makedirs(INJECTIONDIR)
    if not os.path.exists(JUNKDIR):
      os.makedirs(JUNKDIR)
      
    #Dealing with trash can  
    for tf in trashfiles:
      if EMPTY_DONEDIR:
        os.remove(tf)
      else:
        runnr=tf.split("_R")[-1][:9]
        ftdir="%s/%s/%s" % (DONEDIR,runnr[:3],runnr[3:6])
        if not os.path.exists(ftdir):
          os.makedirs(ftdir)
        tfname="%s/%s" % (ftdir,tf.rsplit("/",1)[-1])
        if os.path.exists(tfname):
          ftdir="%s/%s/%s" % (JUNKDIR,runnr[:3],runnr[3:6])
          tfname="%s/%s" % (ftdir,tf.rsplit("/",1)[-1])
        shutil.move(tf,tfname)
        
    #Down to bussines
    for key in sorted(newfiles.keys())[::-1]:
      ver,f=newfiles[key]
      ifr=injectFile(f)
      if ifr == 2:
        runnr=f.split("_R")[-1][:9]
        ftdir="%s/%s/%s" % (DONEDIR,runnr[:3],runnr[3:6])
        if not os.path.exists(ftdir):
          os.makedirs(ftdir)
        tfname="%s/%s" % (ftdir,f.rsplit("/",1)[-1])
        if os.path.exists(tfname):
          ftdir="%s/%s/%s" % (JUNKDIR,runnr[:3],runnr[3:6])
          if not os.path.exists(ftdir):
            os.makedirs(ftdir)
          tfname="%s/%s" % (ftdir,f.rsplit("/",1)[-1])
        shutil.move(f,tfname)
      #elif ifr == 1:
      #  vdir="%s/%s" %(INJECTIONDIR,f.rsplit("/",1)[-1])
      #  shutil.move(f,vdir)
      
    time.sleep(WAIT_TIME)
#=====================================================================================
if __name__ == "__main__": 
  transferFiles()
