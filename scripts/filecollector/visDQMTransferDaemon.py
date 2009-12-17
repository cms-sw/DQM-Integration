#!/usr/bin/env python

import os, time, sys, shutil, glob, re, commands
from commonAnTS import *
from tempfile import mkstemp
if len(sys.argv)<=3 or not os.path.exists(sys.argv[1]):
  for items in sys.argv:
    print items
  print "No valid configuration file"
  sys.exit()
execfile(sys.argv[1])
SOURCE_DIR=sys.argv[2]
REPOSITORY_DIR=sys.argv[3]
try:
  DESTINATION_DIRS=sys.argv[4:]
except:
  DESTINATION_DIRS=[]
DEBUG=False
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
NEWFILES={}
################################################################################
def getFileLists():
  global NEWFILES
  NEWFILES={}
  for infoPath in glob.glob("%s/*.root.dqminfo" % SOURCE_DIR):
    try:
      info=eval(file(infoPath).read())
    except KeyboardInterrupt, e:
      sys.exit(0)
    except:
      debugMsg(2, "Could not read info from file %s " % infoPath)
      os.rename(infoPath,"%s.bad" % infoPath)  
      continue
    NEWFILES.setdefault(infoPath,info)
  DEBUG and debugMsg(0, "Found %d new files that will be injected" % len(NEWFILES))
  return 
#===============================================================================
def injectFile(fInfo,renotify=False):
  fName=os.path.basename(fInfo['path'])
  dirName="%s/%s" % (REPOSITORY_DIR,os.path.dirname(fInfo['path']))
  run=fInfo['runnr']
  parameters=[TEST and "--test" or " ",
              #renotify and "--renotify" or " ",
              "--filename %s" % fName,
              "--type dqm",
              "--path %s" % dirName,
              "--destination dqm",
              "--hostname %s" % TRANSFER_HOSTNAME,
              "--config %s" % TRANSFER_CONFIGFILE,
              "--runnumber %d" % long(run),
              "--lumisection 95",
              "--numevents 834474816",
              "--appname ANTS",
              "--appversion ANTS_1_0"]
  cmd="%s %s" % (INJECTIONSCRIPT," ".join(parameters))
  result = commands.getstatusoutput(cmd)
  if result[0] >= 1:
    output = result[1]
    debugMsg(2, "Error injecting file %s to transfer system checking if it exists" % fName)
    chkparameters=["--check","--filename %s" % fName,"--config %s" % TRANSFER_CONFIGFILE]
    cmd="%s %s" % (INJECTIONSCRIPT," ".join(chkparameters))
    result = commands.getstatusoutput(cmd)
    if result[0]==1:
      if "File not found in database" in result[1]:
        debugMsg(2, "File %s not found in transfer database, check configuration" % fName)
        return 0
      else:
        debugMsg(1,"File %s already exists in transfer database" % fName)
	return 2
    else:
      if "File found in database" in result[1]:
        debugMsg(2,"File %s already exists in transfer database" % fName)
	return 2
      else:
        debugMsg(2, "Problem checking database entry for file %s\nAppError:%s" % (fName,result[1]))
        return 0
  else:
    debugMsg(0, "File %s injected successfully" % fName)
  return 1
#=====================================================================================
def transferFiles():
  while True:
    try:
      #look for NEW files in REGISTERED_DIR and files that need to be cleared.
      getFileLists() 
      
      for outDir in DESTINATION_DIRS:
        if not os.path.exists(outDir):  
          os.makedirs(outDir)
            
      #Down to bussines
      for key in sorted(NEWFILES.keys(),key=lambda x:NEWFILES[x]['runnr'],reverse=True):
        if 'TRANSFER' in NEWFILES[key].keys():
          debugMsg(1,"File %s already Injected moving it onward" % key )
          for outDir in DESTINATION_DIRS:
            if not os.path.exists("%s/%s" % (outDir,ninfo)):
              os.link(finfo,"%s/%s" % (outDir,ninfo))
              DEBUG and debugMsg(0, "info file %s linked in %s/%s" % (key,outDir,ninfo))
          os.unlink(key)
          continue
        DEBUG and debugMsg(0, "Injecting file %s" % NEWFILES[key]['path'])
        iFr=injectFile(NEWFILES[key])
        if iFr == 0:
          os.rename(key,"%s.bad" % key)
          continue
        NEWFILES[key]['TRANSFER']='Injected'
        finfo="%s/%s.dqminfo" % (REPOSITORY_DIR,NEWFILES[key]['path'])
        ninfo=os.path.basename(key)
        # Save the information.  Replaces the .dqminfo file with an updated
        # one, with the actual zip file path.  There is a short window where
        # the info file does not exist, which is ok since everyone reading
        # the files protects against disappearing info files.
        (dname, filepart) = finfo.rsplit("/", 1)
        (fd, tmp) = mkstemp(dir=dname)
        os.write(fd, "%s\n" % NEWFILES[key])
        os.close(fd)
        os.chmod(tmp, 0644)
        os.remove(finfo)
        os.rename(tmp, finfo)
        for outDir in DESTINATION_DIRS:
          if not os.path.exists("%s/%s" % (outDir,ninfo)):
            os.link(finfo,"%s/%s" % (outDir,ninfo))
            DEBUG and debugMsg(0, "info file %s linked in %s/%s" % (key,outDir,ninfo))
        os.unlink(key)
        DEBUG and debugMsg(0, "info file %s unlinked" % key)
      time.sleep(TRANSFERRER_WAIT_TIME)
    except KeyboardInterrupt, e:
      sys.exit(0)

    except Exception, e:
      debugMsg(2,"Application excption: %s " % e)
      
    
#=====================================================================================
if __name__ == "__main__": 
  transferFiles()
