#! /usr/bin/env python

import os,time,sys,shutil

server = 'srv-c2c06-02' #machine to which files are transfered
#DIR = '/tmp/dqmpro/output'  #directory to search new files
#TMPDIR = '/cms/mon/data/.dropbox_tmp' # stealth area on cmsmon
#FILEDIR = '/cms/mon/data/dropbox' # directory, to which files are stored
#TimeTag = '/tmp/dqmpro/output/timetag' #file for time tag for searching new file

### Fore test and development
DIR = '/home/dqmprolocal/output'  #directory to search new files
TMPDIR = '/cms/mon/data/.dropbox_tmp' # stealth area on cmsmon
FILEDIR = '/cms/mon/data/dropbox_test' # directory, to which files are stored
TimeTag = '/home/dqmprolocal/output/timetag' #file for time tag for searching new file

WAITTIME = 120 # waiting time for new files (sec)

#os.popen('rm '+TMPDIR+'/DQM*')  # clean up temporary directory when start
TempTag = TimeTag + '-tmp'
if not os.path.exists(TimeTag):
        os.system('touch -t 01010000 '+ TimeTag)

####### ENDLESS LOOP WITH SLEEP
while 1:
    #### search new files
    #NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TimeTag +' | grep -v DQM_V').read().split()
    NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TimeTag).read().split()
    if len(NEW_)==0:
        print 'waiting for new files...'
        time.sleep(WAITTIME)
        continue

    os.system('touch '+ TempTag)
    print 'Found '+str(len(NEW_))+' new file(s).'
    print os.popen('ls -l '+TimeTag).read()

    #### sort new files by run number
    pairs = []
    for fname in NEW_:
        run = fname[-14:-5] #run number of new file
        pairs.append((run,fname))
    pairs.sort()

    #### loop for new files
    for pair in pairs:
        fname = pair[1]
        tmpfile = fname.replace(fname[:fname.find('/DQM_')],TMPDIR)
        file = fname.replace(fname[:fname.find('/DQM_')],FILEDIR)
        print os.popen('ls -l '+fname).read()
        
        ### copy files to stealth area cmsmon and move to final area
        os.popen('scp '+fname+' '+server+':'+tmpfile).read()
        os.popen('ssh '+server+' -t mv '+tmpfile+' '+file).read()

    shutil.copy2(TempTag,TimeTag)
    
