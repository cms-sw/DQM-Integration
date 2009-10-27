#!/usr/bin/env python
import os, datetime, time,  sys, shutil, glob, re, subprocess as sp,tempfile
from commonAnTS import *
if len(sys.argv)<=1 or not os.path.exists(sys.argv[1]):
  print "No valid configuration file"
  sys.exit()
execfile(sys.argv[1])
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
#####         MAIN PROGRAM         ######
while True:
  try:
    doneSize=getDirSize(T_FILE_DONE_DIR)
    diskSize,userAvailable,diskUsed,diskPUsage=getDiskUsage(T_FILE_DONE_DIR)
  except:
    doneSize=0
    diskSize,userAvailable,diskUsed,diskPUsage=getDiskUsage("/home")
  diskPUsage*=100
  if diskPUsage >= PRODUCER_DU_TOP:
    DEBUG and debugMsg(0,"Disk usage exeeds Upper boundary of %.2f%% and has reached %.2f%%" % (PRODUCER_DU_TOP,diskPUsage))
    quota=long(diskSize*PRODUCER_DU_BOT/100)
    delQuota=diskUsed-quota
    DEBUG and debugMsg(0,"%s are going to be deleted" %   prettyPrintUnits(delQuota,"b",2))
    if delQuota > doneSize:
      msg="Something is filling up the disks, %s does not have enough files to get to the Bottom Boundary of %.2f%%" % (T_FILE_DONE_DIR,PRODUCER_DU_BOT)
      sendmail(YourEmail,body=msg,subject="Something is filling up the disks")
      debugMsg(1,msg)
    aDelQuota=0
    FILE_LIST=[]
    for directory,subdirs,files in os.walk(T_FILE_DONE_DIR):
      subdirs.sort()
      for f in sorted(files,key=lambda a: a[a.rfind("_R",1)+2:a.rfind("_R",1)+11]):
        fMatch=re.match(r"(DQM|Playback|Playback_full)_V[0-9]{4}_([a-zA-Z]+)_R([0-9]{9})_T[0-9]{8}\.root",f)
        if fMatch:
          subSystem=fMatch.group(2)
          run=fMatch.group(3)
          destDir="%s/%s/%s/DQM_V0001_%s_R%s.root" % (SOURCES_DONE_DIR,run[0:3],run[3:6],subSystem,run)
          fullFName="%s/%s" % (directory,f)
          if os.stat(fullFName).st_size+aDelQuota <= delQuota:
            FILE_LIST.append(fullFName)
            aDelQuota+=os.stat(fullFName).st_size
            if  os.path.exists(destDir):
              DEBUG and debugMsg(0,"File %s is going to be deleted" % fullFName)
            else:
              debugMsg(1,"No subsystem file in repository %s for file %s, deleting any way" % (SOURCES_DONE_DIR,fullFName))
          else:
            break
    DEBUG and debugMsg(0,"Found %d files to be deleted" % len(FILE_LIST))
   #cleanning ouput directory
    for directory,subdirs,files in os.walk(COLLECTING_DIR):
      #no subdiretories allowed in COLLECTING_DIR the  directory
      if subdirs:
        debugMsg(2,"Output directory %s, must not contain subdirectories, cleanning" % COLLECTING_DIR)
      for sd in subdirs:
        fullSdName="%s/%s" % (directory,sd)
        for sdRoot,sdDirs,sdFiles in os.walk(fullSdName,topdown=False):
          for f in sdFiles:
            try:
              os.remove(f)
              debugMsg(0,"File %s has been removed" % f)
            except Exception,e:
              debugMsg(2,"Problem deleting file: [Errno %d] %s, '%s'" % (e.errno,e.strerror,e.filename))
          try:
            os.removedir(sdRoot)
            debugMsg(0,"File %s has been removed" % sdRoot)
          except Exception,e:
            debugMsg(2,"Problem deleting directory: [Errno %d] %s, '%s'" % (e.errno,e.strerror,e.filename))
      for f in files:
        if re.match(r"(DQM|Playback|Playback_full)_V[0-9]{4}_([a-zA-Z]+)_R([0-9]{9})_T[0-9]{8}\.root",f):
          continue
        if re.match(r".*\.tmp",f):
          continue
        fullFName="%s/%s" % (directory,f)
        FILE_LIST.append(fullFName)
      #cleaning tmp files:
      TMP_LIST=glob.glob("%s/*.tmp" % COLLECTING_DIR)
      TMP_LIST.sort(reverse=True,key=lambda x: os.stat(x).st_mtime)
      len(TMP_LIST)>0 and TMP_LIST.pop(0)
      DEBUG and debugMsg(0,"Found %d .tmp files to be deleted" % len(TMP_LIST))
      FILE_LIST.extend(TMP_LIST)
       #remove files
    DIR_LIST=[]
    for f in FILE_LIST:
      try:
        os.remove(f)
        debugMsg(0,"File %s has been removed" % f)
      except Exception,e:
        debugMsg(2,"problem deleting file: [Errno %d] %s, '%s'" % (e.errno,e.strerror,e.filename))
      if os.path.dirname(f) not in DIR_LIST and COLLECTING_DIR not in os.path.dirname(f):
        DIR_LIST.append(os.path.dirname(f))
    #remove emprty directories
    for d in DIR_LIST:
      try:
        os.removedirs(d)
        debugMsg(0,"Directory %s has been removed" % d)
      except Exception,e:
        print e
        debugMsg(1,"Directory delition failed: [Errno %d] %s, '%s'" % (e.errno,e.strerror,e.filename))
  time.sleep(PROD_CLEANNER_WAIT_TIME)
         
      
    
