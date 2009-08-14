#! /usr/bin/env python

import os, time, sys, shutil, glob, smtplib, re
from datetime import datetime
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

DIRS = ['/dqmdata/dqm/merged'] 		#sys.argv[2:] #     # Directory with new (merged) files
DONEDIR = "/dqmdata/dqm/registered"     # 'Directory that stores registered files
JUNKDIR = "/dqmdata/dqm/junk"
INDEX = '/home/dqm/idx' 		#sys.argv[1] # '/home/dqm/idx'        # DQM GUI server index directory
WAITTIME = 120			        # Wait time for new files (sec)
MAXFILES = 10	 	  		# Max number of files to process at once

existing = dict([(long(runnr), [int(v),dqmfile]) for v,dqmfile,runnr in
                  [re.match(".*import-version=(\d+).*src-file=#\d+/([/_a-zA-Z0-9.]+).*runnr=(\d+)",a).groups() 
                    for a in os.popen("visDQMIndex dump %s catalogue |"
                           " grep '^SAMPLE #' " % INDEX).read().split("\n") 
                           if re.match(".*import-version=(\d+).*src-file=#\d+/([/_a-zA-Z0-9.]+).*runnr=(\d+)",a)]])



if not os.path.exists(DONEDIR):
  os.makedirs(DONEDIR)
    
if not os.path.exists(JUNKDIR):
  os.makedirs(JUNKDIR)
    
    
while True:  
  nfiles = 0
  new = []
  moveout = []
     
  for DIR in DIRS:
    for dir, subdirs, files in os.walk(DIR):
      for f in files:
        m = re.match(r'^DQM_V(\d+)_R(\d+)(__[-A-Za-z0-9_]+)?\.root$', f)
        if m:
          filerun = long(m.group(2))
          filev = int(m.group(1))
	  fileds = (m.group(3) or "").replace("__", "/")
          path = "%s/%s" % (dir, f)
          donepath = "%s/%s" % (DONEDIR, f)
          junkpath = "%s/%s" % (JUNKDIR, f)
          
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
      if nfiles > MAXFILES:
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

      
  if nfiles <= MAXFILES:
    time.sleep(WAITTIME)
