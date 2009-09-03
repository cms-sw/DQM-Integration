#!/usr/bin/env python

import os, time, sys, shutil, glob, re, commands


from RootArchivalAndTransferSystem_cfg import *
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

################################################################################
#=====================================================================================
def renotifyFile(f,stage):
  fname=f.rsplit("/",1)[-1]
  run=f.split("_R")[-1][:9]
  verDir  = "%s/%s" % (VERIFY_DIR,STAGES[stage+1]) 
  verFile = "%s/%s" % (verDir,f.rsplit("/",1)[-1])
  if not os.path.exists(verDir):
    os.makedirs(verDir)
  shutil.move(f,verFile)
  parameters=[TEST and "--test" or " ",
              "--renotify",
              "--filename %s" % fname,
              "--type dqm",
              "--path %s" % verDir,
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
  print result[1]
  if result[0] >= 1:
    output = result[1]
    print "Error injecting file %s to transfer system checking if it exists" % f
#=====================================================================================
def chkFileStat(fname):   
  chkparameters=["--check","--filename %s" % fname,"--config %s" % TRANSFER_CONFIGFILE]
  cmd="%s %s" % (INJECTIONSCRIPT," ".join(chkparameters))
  result = commands.getstatusoutput(cmd)
  return result

def saveFile(f):
  runnr=f.split("_R")[-1][:9]
  ftdir="%s/%s/%s" % (DONE_DIR,runnr[:3],runnr[3:6])
  if not os.path.exists(ftdir):
    os.makedirs(ftdir)
  tfname="%s/%s" % (ftdir,f.rsplit("/",1)[-1])
  if os.path.exists(tfname):
    print "file reapeared sending to junk"
    ftdir="%s" % (JUNK_DIR)
    tfname="%s/%s" % (ftdir,f.rsplit("/",1)[-1])
  shutil.move(f,tfname)
#=====================================================================================
if __name__ == "__main__":
  while True: 
    for stage in STAGES[::-1][1:]:
      stageDir    = "%s/%s" % (VERIFY_DIR,stage) 
      print "Processing %s" % stage
      for dir1, subdirs, files in os.walk(stageDir):
        for f in files:
          fileStat=chkFileStat(f)
          if "FILES_TRANS_CHECKED" in fileStat[1]:
            print "File %s has been succesfully transfered to CASTOR" % f
            fullFName= "%s/%s" % (dir1,f)
            saveFile(fullFName)
          else:
            print fileStat[1]
            print "File %s is being renotified" % f
            fullFName= "%s/%s" % (dir1,f)
            renotifyFile(fullFName,STAGES.index(stage))
  
    for dir1, subdirs, files in os.walk(INJECTION_DIR):
      print "Processing %s" % dir1
      for f in files:
        fileStat=chkFileStat(f)
        if "FILES_TRANS_CHECKED" in fileStat[1]:
          fullFName= "%s/%s" % (dir1,f)
          saveFile(fullFName)
        else:
          verDir  = "%s/%s" % (VERIFY_DIR,STAGES[0]) 
          verFile = "%s/%s" % (verDir,f)
          if not os.path.exists(verDir):
            os.makedirs(verDir)
          fullFName= "%s/%s" % (dir1,f)
          shutil.move(fullFName,verDir)
         
      time.sleep(VERIFY_WAIT_TIME)
  
