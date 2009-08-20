#!/usr/bin/env python

import os, time, sys, shutil, glob, smtplib, re
import getopt as gop
import zipfile as zp
from datetime import date
from email.MIMEText import MIMEText

SOURCEDIR = "/dqmdata/EventDisplay/dropbox" #Directory where the original files are located.
DESTDIR = "/dqmdata/EventDisplay/Tier0_Test" #Directory where zipped files will be stored for transfer.
DONEDIR = "/dqmdata/EventDisplay/done"
CLEANUP = False
MAX_ZIP_SIZE = 1610612736 # 1.5GB/70%   as max filesize.
COMPRESSION = 1 #Compression rate for zip file 1(min) - 9(max)
WAITTIME = 120 # waiting time for new files (sec)
def Tier0sort(x,y):
  try: 
    arun=re.search("_R[0-9]{9}",x).group(0).split("_R")[-1]
    brun=re.search("_R[0-9]{9}",y).group(0).split("_R")[-1]
    aext=x.split(".")[-1]
    bext=y.split(".")[-1]
    aver=re.search("_T[0-9]{8}",x).group(0).split("_T")[-1]
    bver=re.search("_T[0-9]{8}",y).group(0).split("_T")[-1]
    if arun == brun:
      if aver == bver:
        if aext < bext: 
          return -1 
        elif aext > bext:
          return 1
        else:
          return 0
      else:
        if aver < bver: 
          return -1 
        elif aver > bver:
          return 1
        else:
          return 0
    else:
      if arun < brun: 
        return -1 
      elif arun > brun:
        return 1
      else:
        return 0
  except: 
    if x < y: 
      return -1 
    elif x > y:
      return 1
    else:
      return 0  
#=====================================================================================
def genName(zipFile):
  filelist=zipFile.namelist()
  count=len(filelist)
  runs=[]
  for f in filelist:
    try:
      runs.append("%09d" % long(re.search("_R[0-9]{1,9}",f).group(0).split("_R")[-1]))
    except AttributeError:
      dt=date.today()
      d=dt.strftime("%y%m%d")
      run="etc%s%s" % (d[:3],d[3:])
      runs.append(run)
  runs.sort()
  d=date.today()
  return "iSpy_ONLINE_%s_R_R%s_%s_NF%03d.zip" % (d.strftime("%Y%m%d"),runs[0],runs[-1],count) 
#=====================================================================================
def getFileList():
  newfiles=[]
  for dir1, subdirs, files in os.walk(SOURCEDIR):
    for f in files:
      if ".ig" in f:
        newfiles.append("%s/%s" % (dir1,f))
  newfiles.sort(Tier0sort)
  return newfiles
#=====================================================================================
def moveToDone(arcName,fullFileName):
  try:
    run="%09d" % long(re.search(r'_R[0-9]{1,9}',arcName).group(0)[2:])
  except:
    dt=date.today()
    d=dt.strftime("%y%m%d")
    run="etc%s%s" % (d[:3],d[3:])
  fdondedir="%s/%s/%s" % (DONEDIR,run[:3],run[3:6])
  if not os.path.exists(fdondedir):
    os.makedirs(fdondedir)
  fdone= "%s/%s" % (fdondedir,arcName)
  shutil.move(fullFileName,fdone)

#=====================================================================================
def packfiles():
  tmpName="tempzipfile.zip"
  fullTmpName="%s/%s" % (SOURCEDIR,tmpName)
  while True:
    filesToPack=getFileList()
    if len(filesToPack) == 0:
      print "Waiting for new files..."
      time.sleep(WAITTIME)
      continue
    if not os.path.exists(DESTDIR):
      os.makedirs(DESTDIR)
    if not os.path.exists(fullTmpName):
      print "Creating file %s " % (fullTmpName,)
      zpFile=zp.ZipFile(fullTmpName,"w",COMPRESSION-1)
    else:
      zpFile=zp.ZipFile(fullTmpName,"a",COMPRESSION-1)
    for f in filesToPack:
      print "Compressing file %s into %s" % (f,fullTmpName)
      arcName=f.rsplit("/",1)[-1]
      filelist=zpFile.namelist()
      if os.stat(fullTmpName).st_size+os.stat(f).st_size < MAX_ZIP_SIZE and arcName not in filelist:
        zpFile.write(f,arcName,COMPRESSION-1)
        moveToDone(arcName,f)
      elif arcName in filelist:
        print "WARNING: File %s already contained in archive, ignoring" % arcName
        moveToDone(arcName,f)
      else:
        zipName="%s/%s" % (DESTDIR,genName(zpFile))
        zpFile.close()
        counter=1
        while os.path.exists(zipName):
          zipName="%s_%03d.zip" %(zipName.split(re.search(r'(|\_[0-9]{3})\.zip',zipName).group(0))[0],counter)
          counter+=1          
        shutil.move(fullTmpName,zipName)
        print "Saving file %s " % zipName
        print "Creating file %s " % (fullTmpName,)
        zpFile=zp.ZipFile(fullTmpName,"w",COMPRESSION-1)
        zpFile.write(f,arcName,COMPRESSION-1)
        moveToDone(arcName,f)    
    zpFile.close()
    #zipName="%s/%s" % (DESTDIR,genName(doneList))
    
    
if __name__ == "__main__": 
  packfiles()
