#!/usr/bin/env python
import os, datetime, time,  sys, shutil, glob, re, subprocess as sp,tempfile
from commonAnTS import *
if len(sys.argv)<=1 or not os.path.exists(sys.argv[1]):
  print "No valid configuration file"
  sys.exit()
execfile(sys.argv[1])
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
#####      PROGRAM  VARIABLES      ######
MODES=["%DiskUse","Size","NumberOfRuns","Time"]    # DisQuota %, Size bytes, NumberOfRuns=n n latest 
#####         MAIN PROGRAM         ######
if MODE not in MODES:
  debugMsg(2,"%s is not an accepted mode only [\"%s\"] are accepted" % (MODE,"\",\"".join(MODES)))
  sys.exit(1)
  
while True:
  FILE_LIST=[]
  STAY_DIR={}
  if MODE in ["%DiskUse","Size"]:
    doneSize=getDirSize(CLEAN_DIR)
    diskSize,userAvailable,diskUsed,diskPUsage=getDiskUsage(CLEAN_DIR)
    upperBound = MODE == "%DiskUse" and FILER_DU_TOP or FILER_SQ_TOP
    lowerBound = MODE == "%DiskUse" and FILER_DU_BOT or FILER_SQ_BOT
    level      = MODE == "%DiskUse" and diskPUsage or doneSize
    units      = MODE == "%DiskUse" and "p" or "b"
    quota      = MODE == "%DiskUse" and long(diskSize*FILER_DU_BOT) or FILER_SQ_BOT
    if level >= upperBound:
      DEBUG and debugMsg(0,"Disk usage exeeds Upper boundary of %s and has reached %s" % (prettyPrintUnits(upperBound,units,2),prettyPrintUnits(level,units,2)))
      delQuota=diskUsed-quota
      DEBUG and debugMsg(0,"%s are going to be deleted" % prettyPrintUnits(delQuota,"b",2))
      if delQuota > doneSize:
        msg="Something is filling up the disks, %s is does not have enough files to get to the Bottom Boundary of %s" % (CLEAN_DIR,prettyPrintUnits(lowerBound,units,2))
        sendmail(YourEmail,body=msg)
        debugMsg(1,msg)
        aDelQuota=0
        #filling STAY_DIR
        for directory,subdirs,files in os.walk(CLEAN_DIR):
          for f in files:
            fullFName="%s/%s" % (directory,f)
            fMatch=re.match(r".*_R([0-9]{9}).*",f)
            if fMatch:
              run=fMatch.group(1)
              fSize=os.stat(fullFName).st_size
              STAY_DIR.setdefault(run,{}).setdefault(fullFName,fSize)
            else:
              debugMsg(1,"File %s does not have a run number and should not be in here deleting" % fullFName)
              FILE_LIST.append(fullFName)
              aDelQuota+=os.stat(fullFName).st_size
        #filling FILE_LIST
        for run in sorted(STAY_DIR.keys()):
          for f in STAY_DIR[run].keys():
            if aDelQuota + STAY_DIR[run][f] <= quota:
              FILE_LIST.append(f)
              aDelQuota+=STAY_DIR[run][f]
              DEBUG and debugMsg(0,"File %s has been included for deletion" % fullFName)
            else:
              break
  else: 
    runsInDTime = MODE == "Time" and getNumRunsWithinTime(CLEAN_DIR,FILER_TIME) or 0
    runs        = MODE == "Time" and (runsInDTime > FILER_NRUNS  and runsInDTime or FILER_NRUNS) or FILER_NRUNS
    timeStamp   = MODE == "Time" and long(time.time()) - (FILER_TIME * 3600) or 0  
    #filling STAY_DIR
    for directory,subdirs,files in os.walk(CLEAN_DIR):
      for f in files:
        fullFName="%s/%s" % (directory,f)
        fMatch=re.match(r".*_R([0-9]{9}).*",f)
        if fMatch:
          run=fMatch.group(1)
          fMtime=os.stat(fullFName).st_mtime
          STAY_DIR.setdefault(run,{}).setdefault(fullFName,fMtime)
        else:
          #debugMsg(1,"File %s does not have a run number and should not be in here deleting" % fullFName)
          FILE_LIST.append(fullFName)
    #filling FILE_LIST
    oldestRun = len(STAY_DIR.keys()) > runs and long(sorted(STAY_DIR.keys(),reverse=True)[runs-1]) or long(STAY_DIR.keys()[-1])
    for run in sorted(STAY_DIR.keys()): 
      for f in STAY_DIR[run].keys():
        if long(run) < oldestRun or STAY_DIR[run][f] < timeStamp:
          FILE_LIST.append(f)
        else:
          break
  DEBUG and debugMsg(0,"Found %d files to be deleted" % len(FILE_LIST))  
  #remove files
  DIR_LIST=[]
  for f in FILE_LIST:
    try:
      os.remove(f)
      DEBUG and debugMsg(0,"File %s has been removed" % f)
    except Exception,e:
      debugMsg(2,"problem deleting file: [Errno %d] %s, '%s'" % (e.errno,e.strerror,e.filename))
    if os.path.dirname(f) not in DIR_LIST and COLLECTING_DIR not in os.path.dirname(f):
      DIR_LIST.append(os.path.dirname(f))
  #remove emprty directories
  for d in DIR_LIST:
    try:
      os.removedirs(d)
      DEBUG and debugMsg(0,"Directory %s has been removed" % d)
    except Exception,e:
      print e
      DEBUG and debugMsg(0,"Directory delition failed: [Errno %d] %s, '%s'" % (e.errno,e.strerror,e.filename))
  time.sleep(FILER_CLEANNER_WAIT_TIME)
         
      
    
