#! /usr/bin/env python

import os, time, sys, shutil, glob, re
from datetime import datetime
if len(sys.argv)<=1 or not os.path.exists(sys.argv[1]):
  print "No valid configuration file"
  sys.exit()
execfile(sys.argv[1])
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
while True:
  #### search new files
  NRUNS = 0
  NFOUND = 0
  NEW = {}
  for dir, subdirs, files in os.walk(DROPBOX):
    for f in files:
      if not f.startswith("DQM_Reference") and re.match(r'^DQM_.*_R[0-9]{9}\.root$', f):
	runnr = f[-14:-5]
        donefile = "%s/%s/%s/%s" % (SOURCES_DONE_DIR, runnr[0:3], runnr[3:6], f)
        f = "%s/%s" % (dir, f)
	if os.path.exists(donefile) and os.stat(donefile).st_size == os.stat(f).st_size:
	  print "WARNING: %s was already processed but re-appeared" % f
	  os.remove(f)
	  continue
        NEW.setdefault(runnr, []).append(f)
        NFOUND += 1
  
  if NFOUND:
    print '%s: found %d new files in %d runs.' % (datetime.now(), NFOUND, len(NEW))

    newFiles = []
    allOldFiles = []
    for run in sorted(NEW.keys())[::-1]:
      NRUNS += 1
      if NRUNS > MAX_RUNS:
        break

      files = NEW[run]
      runnr = "%09d" % long(run)
      destdir = "%s/%s/%s" % (MERGED_DIR, runnr[0:3], runnr[3:6])
      bkdestdir = "%s" % (FILER_MERGED_DIR)
      donedir = "%s/%s/%s" % (SOURCES_DONE_DIR, runnr[0:3], runnr[3:6])
      oldfiles = sorted(glob.glob("%s/DQM_V????_R%s.root" % (destdir, runnr)))[::-1]
      if len(oldfiles) > 0:
        version = int(oldfiles[0][-20:-16]) + 1
        files.append(oldfiles[0])
      else:
	version = 1

      if not os.path.exists(destdir):
        os.makedirs(destdir)
      if not os.path.exists(donedir):
        os.makedirs(donedir)
      if not os.path.exists(bkdestdir):
        os.makedirs(bkdestdir)
    
      destfile = "%s/DQM_V%04d_R%s.root" % (destdir, version, runnr)
      bkdestfile = "%s/DQM_V%04d_R%s.root" % (bkdestdir, version, runnr)
      logfile = "%s.log" % destfile[:-5]
      tmpdestfile = "%s.tmp" % destfile
    
      print 'Merging run %s to %s (adding %s to %s)' % (run, destfile, files, oldfiles)
      LOGFILE = open(logfile, 'a')
      LOGFILE.write(os.popen('DQMMergeFile %s %s' % (tmpdestfile, " ".join(files))).read())
      LOGFILE.close()
      if not os.path.exists(tmpdestfile):
        body = 'Failed merging files for run %s. Will try again later.' % run
        print body
        sendmail(YourEmail,run,body)
	continue
    
      shutil.move(tmpdestfile, destfile)
      shutil.copy2(destfile,bkdestfile)
      for f in files:
	shutil.move(f, "%s/%s" % (donedir, f.rsplit('/', 1)[1]))
  
  if NRUNS <= MAX_RUNS:
    time.sleep(MERGER_WAIT_TIME)
