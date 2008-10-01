#! /usr/bin/env python

import os,time,sys,shutil

### set environments
DIR = '/data/dqm/dropbox'  # directory to search new files
DB = '/home/dqm/dqm.db' #master db
BAKDB = '/data/dqm/filereg/backups/dqm.db' #bakcup db (timestamp will be attatched)
TMPDB = '/data/dqm/dropbox/dqm-tmp.db' # temporal db
FILEDIR = '/data/dqm/results' # directory, to which merged file is stored
TMPDIR = '/data/dqm/.dropbox_tmp' # directory, in which merged file is created
TimeTag = '/data/dqm/dropbox/timetag' #file for time tag for searching new file
LOGDIR = '/data/dqm/filereg/log'
WAITTIME = 120 # waiting time for new files (sec)
MERGE_EXE = '/data/dqm/filereg/mergeAndRegister.py'

## For test and development
#DIR = '/data/dqm/dropbox_test'  # directory to search new files
#DB = '/data/dqm/filereg_test/dqm.db' #master db
#BAKDB = '/data/dqm/filereg_test/backups/dqm.db' #bakcup db (timestamp will be attatched)
#TMPDB = '/data/dqm/dropbox/dqm-tmp.db' # temporal db
#FILEDIR = '/data/dqm/results_test' # directory, to which merged file is stored
#TMPDIR = '/data/dqm/.dropbox_tmp' # directory, in which merged file is created
#TimeTag = '/data/dqm/dropbox_test/timetag' #file for time tag for searching new file
#LOGDIR = '/data/dqm/filereg_test/log'
#WAITTIME = 120 # waiting time for new files (sec)
#MERGE_EXE = '/data/dqm/filereg_test/mergeAndRegister.py'


if not os.path.exists(TimeTag):
        os.system('touch -t 01010000 '+ TimeTag)


####### ENDLESS LOOP WITH SLEEP
while 1:

    #### trigger by new files
    NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TimeTag).read().split()
    if len(NEW_)==0:
        print 'waiting for new files...'
        time.sleep(WAITTIME)
        continue

    #### start 'merge & register'
    execfile(MERGE_EXE)

    #### Get and write DQM summary to DBS
    print '****** Start to get and write DQM summary to DBS ******'
    for filename in mergedfiles:
	    #print filename
	    dir = filename[:filename.find('/DQM_')] #extract directory name
	    run = filename[-14:-5] #extract run number
	    DqmSummaryLog = dir + '/GetAndWriteDQMSummaryIntoOMDS_R' + run + '.log'
	    OUT_ = os.popen('GetAndWriteDQMSummaryIntoOMDS '+  filename + ' ' + DqmSummaryLog).read()

	    print OUT_
	    
