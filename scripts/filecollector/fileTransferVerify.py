#!/usr/bin/env python

import os, time, sys, shutil, glob, smtplib, re, commands
import getopt as gop
import zipfile as zp
from datetime import datetime
from email.MIMEText import MIMEText

SOURCEDIR = "/dqmdata/dqm/Tier0Shipping/inject" #Directory where the original files are located.
DONEDIR = "/dqmdata/dqm/done/merged"
JUNKDIR = "/dqmdata/dqm/junk"
VERIFYDIR = "/dqmdata/dqm/Tier0Shipping/verify"
HOSTNAME = "srv-C2D05-19"
CONFIGFILE = "/nfshome0/dqm/.transfer/myconfig.txt"
INJECTIONSCRIPT = "/nfshome0/tier0/scripts/injectFileIntoTransferSystem.pl"
STAGES=["st1","st2","st3","Error"]
EMPTY_DONEDIR = False
WAIT_TIME = 600
################################################################################
#=====================================================================================
def renotifyFile(f,stage):
  run=f.split("_R")[-1][:9]
  verDir  = "%s/%s" % (VERIFYDIR,STAGES[stage+1]) 
  verFile = "%s/%s" % (verDir,f.rsplit("/",1)[-1])
  if not os.path.exists(verDir):
    os.makedirs(verDir)
  shutil.move(f,verFile)
  parameters=["--test",
              "--renotify",
              "--filename %s" % verFile,
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
#=====================================================================================
def chkFileStat(fname):   
  chkparameters=["--check","--filename %s" % fname,"--config %s" % CONFIGFILE]
  cmd="%s %s" % (INJECTIONSCRIPT," ".join(chkparameters))
  result = commands.getstatusoutput(cmd)
  return result

def saveFile(f):
  runnr=f.split("_R")[-1][:9]
  ftdir="%s/%s/%s" % (DONEDIR,runnr[:3],runnr[3:6])
  if not os.path.exists(ftdir):
    os.makedirs(ftdir)
  tfname="%s/%s" % (ftdir,f.rsplit("/",1)[-1])
  if os.path.exists(tfname):
    print "file reapeared sending to junk"
    ftdir="%s" % (JUNKDIR)
    tfname="%s/%s" % (ftdir,f.rsplit("/",1)[-1])
  shutil.move(f,tfname)
#=====================================================================================
if __name__ == "__main__":
  while True: 
    for stage in range(len(STAGES)-1):
      stageDir    = "%s/%s" % (VERIFYDIR,STAGES[stage]) 
      print "Processing %s" % STAGES[stage]
      for dir1, subdirs, files in os.walk(stageDir):
        for f in files:
          fileStat=chkFileStat(f)
          if "FILES_TRANS_CHECKED" in fileStat[1]:
            print "File %s has been succesfully transfered to CASTOR" % f
            fullFName= "%s/%s" % (dir1,f)
            saveFile(fullFName)
          else:
            print "File %s is being renotified" % f
            fullFName= "%s/%s" % (dir1,f)
            renotifyFile(fullFName,stage)
  
    for dir1, subdirs, files in os.walk(SOURCEDIR):
      print "Processing %s" % dir1
      for f in files:
        fileStat=chkFileStat(f)
        if "FILES_TRANS_CHECKED" in fileStat[1]:
          fullFName= "%s/%s" % (dir1,f)
          saveFile(fullFName)
        else:
          verDir  = "%s/%s" % (VERIFYDIR,STAGES[0]) 
          verFile = "%s/%s" % (verDir,f)
          if not os.path.exists(verDir):
            os.makedirs(verDir)
          fullFName= "%s/%s" % (dir1,f)
          shutil.move(fullFName,verDir)
         
      time.sleep(WAIT_TIME)
  
