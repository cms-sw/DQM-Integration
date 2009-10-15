#! /usr/bin/env python

import os, time, sys, shutil, glob, smtplib, re
from datetime import datetime
from commonAnTS import *
if len(sys.argv)<=1 or not os.path.exists(sys.argv[1]):
  print "No valid configuration file"
  sys.exit()
execfile(sys.argv[1])
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
existing = dict([(long(runnr), [int(v),dqmfile]) for v,dqmfile,runnr in
                  [re.match(".*import-version=(\d+).*src-file=#\d+/([/_a-zA-Z0-9.]+).*runnr=(\d+)",a).groups() 
                    for a in os.popen("visDQMIndex dump %s catalogue |"
                           " grep '^SAMPLE #' " % INDEX).read().split("\n") 
                           if re.match(".*import-version=(\d+).*src-file=#\d+/([/_a-zA-Z0-9.]+).*runnr=(\d+)",a)]])



if not os.path.exists(REGISTERED_DIR):
  os.makedirs(REGISTERED_DIR)
    
if not os.path.exists(JUNK_DIR):
  os.makedirs(JUNK_DIR)
    
    
while True:  
  nfiles = 0
  new = []
  moveout = []
     
  for dir, subdirs, files in os.walk(FILER_MERGED_DIR):
    for f in files:
      m = re.match(r'^DQM_V(\d+)_R(\d+)(__[-A-Za-z0-9_]+)?\.root$', f)
      if m:
        filerun = long(m.group(2))
        filev = int(m.group(1))
        fileds = (m.group(3) or "").replace("__", "/")
        path = "%s/%s" % (dir, f)
        donepath = "%s/%s" % (REGISTERED_DIR, f)
        junkpath = "%s/%s" % (JUNK_DIR, f)
        
        if filerun not in existing and (filerun > 1 or fileds != ""):
          new.append((filerun, filev, fileds, path,donepath ))
          # ^ negative version so reverse sort later will sort into
          # descending order by run, ascending order by version.
        else:
          if (filerun > 1 or fileds != "") and filev > existing[filerun][0]:
            new.append((filerun, filev, fileds, path,donepath ))
          else:
            print "File %s is older than the one already registered: descarting" % f
            moveout.append((path,junkpath))
  for path, junkpath in moveout:
    shutil.move(path,junkpath)

  if len(new):
    print '%s: found %d new files.' % (datetime.now(), len(new))

    for run, version, dataset, path, donepath in sorted(new)[::-1]:
      nfiles += 1
      if nfiles > MAX_FILES:
        break
      if run in existing and version < existing[run][0]:
	print 'File %s is older than the latest registered moving on' % path	
	shutil.move(path,donepath)
      	continue  
      print 'Registering %s for run %09d' % (path, run)
      if dataset != "":
        os.system('set -x; visDQMIndex -d add %s %s' % (INDEX, path))
      else:
        os.system('set -x; visDQMIndex -d add --dataset "/Global/Online/ALL" %s %s' % (INDEX, path))
      existing[run]=[version,path]
      shutil.move(path,donepath)

      
  if nfiles <= MAX_FILES:
    time.sleep(REGISTER_WAIT_TIME)
