#! /usr/bin/env python

import os,time,sys,shutil

#DIR = '/cms/mon/data/dropbox'  # directory to search new files
#TimeTag = '/cms/mon/data/dropbox/timetag' #file for time tag for searching new file

#### Directories and files for test and development
DIR = '/cms/mon/data/dropbox_test'  # directory to search new files
TimeTag = '/cms/mon/data/dropbox_test/timetag' #file for time tag for searching new file

WAITTIME = 120 # waiting time for new files (sec)
MERGE_EXE = '/cms/mon/data/dqm/filereg_test/mergeAndRegister.py'

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
    print '**** merged files ****'
    for filename in mergedfiles:
	    print filename
