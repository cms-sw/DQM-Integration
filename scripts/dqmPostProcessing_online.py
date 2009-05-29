#! /usr/bin/env python

import os, time, sys, shutil, glob, smtplib, re
from datetime import datetime
from email.MIMEText import MIMEText
#from ROOT import TFile
if len(sys.argv) <= 1: sys.exit(0)
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

DIR = '/data/dqm/dropbox'  # directory to search new files
DB = '/home/dqm/dqm.db' #master db
TMPDB = '/home/dqm/dqm.db.tmp' # temporal db
FILEDIR = '/data/dqm/merged' # directory, to which merged file is stored
DONEDIR = '/data/dqm/done' # directory, to which processed files are stored
WAITTIME = 120 # waiting time for new files (sec)
MAX_TOTAL_RUNS = 100
MAX_RUNS = 10

YourMail = "lilopera@cern.ch"
ServerMail = "dqm@srv-C2D05-19.cms"

def sendmail(EmailAddress,run):
  s=smtplib.SMTP("localhost")
  tolist=[EmailAddress, "lat@cern.ch"]
  body="File merge failed by unknown reason for run"+run
  msg = MIMEText(body)
  msg['Subject'] = "File merge failed."
  msg['From'] = ServerMail
  msg['To'] = EmailAddress
  s.sendmail(ServerMail,tolist,msg.as_string())
  s.quit()

def filecheck(rootfile):
  f = TFile(rootfile)
  if (f.IsZombie()):
      #print "File corrupted"
      f.Close()
      return 0
  else:
      hist = f.FindObjectAny("reportSummaryContents")
      #(skip filecheck for HcalTiming files!!)
      if (hist == None and rootfile.rfind('HcalTiming') == -1):
          #print "File is incomplete"
          f.Close()
          return 0
      else:
          #print "File is OK"
          f.Close()
          return 1
      
while True:
  #### search new files
  NRUNS = 0
  NFOUND = 0
  NEW = {}
  for dir, subdirs, files in os.walk(DIR):
    for f in files:
      if not f.startswith("DQM_Reference") and re.match(r'^DQM_.*_R[0-9]{9}\.root$', f):
	runnr = f[-14:-5]
        donefile = "%s/%s/%s/%s" % (DONEDIR, runnr[0:3], runnr[3:6], f)
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
      destdir = "%s/%s/%s" % (FILEDIR, runnr[0:3], runnr[3:6])
      donedir = "%s/%s/%s" % (DONEDIR, runnr[0:3], runnr[3:6])
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
    
      destfile = "%s/DQM_V%04d_R%s.root" % (destdir, version, runnr)
      logfile = "%s.log" % destfile[:-5]
      tmpdestfile = "%s.tmp" % destfile
    
      print 'Merging run %s to %s (adding %s to %s)' % (run, destfile, files, oldfiles)
      ntries = 0
      while ntries < 30:
        LOGFILE = open(logfile, 'a')
        LOGFILE.write(os.popen('DQMMergeFile %s %s' % (tmpdestfile, " ".join(files))).read())
	LOGFILE.close()
        if not os.path.exists(tmpdestfile):
          print 'Failed merging files for run %s. Try again after two minutes' % run
          sendmail(YourMail,run)
    	  time.sleep(WAITTIME)
    	  ntries += 1
        else:
    	  break
    
      os.rename(tmpdestfile, destfile)
      for f in files:
	os.rename(f, "%s/%s" % (donedir, f.rsplit('/', 1)[1]))

      allOldFiles.extend(oldfiles)
      newFiles.append((long(run), destfile))
  
    if os.path.exists(TMPDB):
      os.remove(TMPDB)
  
    if os.path.exists(DB):
      os.rename(DB, TMPDB)
    else:
      os.system('set -x; visDQMRegisterFile %s "/Global/Online/ALL" "Global run"' % TMPDB)
  
    while len(allOldFiles) > 0:
      (slice, rest) = (allOldFiles[0:50], allOldFiles[50:])
      os.system('set -x; visDQMUnregisterFile %s %s' % (tmpdb, " ".join(slice)))
      allOldFiles = rest
      for old in slice:
        os.remove(old)
  
    existing = [long(x) for x in os.popen("sqlite3 %s 'select distinct runnr from t_data order by runnr desc'" % TMPDB).read().split()]
    for runnr, file in newFiles:
      print 'Registering %s for run %d' % (file, runnr)
      older = [x for x in existing if x < runnr]
      newer = [x for x in existing if x > runnr]
      if len(newer) > MAX_TOTAL_RUNS:
	print "Too many newer runs (%d), not registering %s for run %d" % (len(newer), file, runnr)
	continue

      if len(older) > MAX_TOTAL_RUNS:
	print "Too many older runs (%d), pruning data for oldest run %d" % (len(older), older[0])
	os.system(r"set -x; sqlite3 %s 'delete from t_data where runnr = %d'" % older[0])
	os.system(r"set -x; sqlite3 %s 'delete from t_files where name like '\''%\_R%09d.root'\'' escape '\'\\\'" % older[0])
	os.system(r"set -x; sqlite3 %s 'vacuum'")

      os.system('set -x; visDQMRegisterFile %s "/Global/Online/ALL" "Global run" %s' % (TMPDB, file))
  
    os.rename(TMPDB, DB)

  if NRUNS <= MAX_RUNS:
    time.sleep(WAITTIME)
