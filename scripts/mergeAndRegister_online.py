#! /usr/bin/env python

import os,time,sys,shutil
from sets import Set

def fileunreg(db,file,logfile):
    tmpdb = '/cms/mon/data/.dropbox_test/dqm-tmp.db'
    newdb = db[:-3]+'-new.db'
    server = 'srv-c2d05-19'
    if os.path.exists(tmpdb): os.remove(tmpdb)
    logfile.write(os.popen('scp '+server+ ':'+db+' '+tmpdb).read())
    logfile.write('*** File UnRegister ***\n')
    logfile.write(os.popen('visDQMUnregisterFile '+ tmpdb +' ' + file).read())
    logfile.write(os.popen('scp '+tmpdb+' '+server+':'+newdb).read())
    os.remove(tmpdb)
    logfile.write(os.popen('ssh '+server+' -t mv '+newdb+' '+db).read())

def filereg(db,file,logfile):
    tmpdb = '/cms/mon/data/.dropbox_test/dqm-tmp.db'
    newdb = db[:-3]+'-new.db'
    server = 'srv-c2d05-19'
    if os.path.exists(tmpdb): os.remove(tmpdb)
    logfile.write(os.popen('scp '+server+ ':'+db+' '+tmpdb).read())
    logfile.write('*** File Register ***\n')
    logfile.write(os.popen('visDQMRegisterFile '+ tmpdb +' "/Global/Online/ALL" "Global run" '+ file).read())
    logfile.write(os.popen('scp '+tmpdb+' '+server+':'+newdb).read())
    os.remove(tmpdb)
    logfile.write(os.popen('ssh '+server+' -t mv '+newdb+' '+db).read())


CMSMON = 'srv-c2c06-02' # machine to which merged file is transfered

DIR = '/cms/mon/data/dropbox'  # directory to search new files
DB = '/home/dqm/dqm.db'
FILEDIR = '/cms/mon/data/dqm/results' # directory, to which merged file is stored
TMPDIR = '/cms/mon/data/.dropbox_test' # directory, in which merged file is created

#### Directories for test
#DIR = '/cms/mon/data/dropbox_test'  # directory to search new files
#DB = '/cms/mon/data/dqm/dqm.db'
#FILEDIR = '/cms/mon/data/dqm/tmp'
#TMPDIR = '/cms/mon/data/dropbox_test/tmp' # directory, in which merged file is created

#SIZE_LIMIT = 5000000000  # size limit for merged file (5~10 Gbyte)
WAITTIME = 300 # waiting time for new files (sec)

os.popen('rm '+TMPDIR+'/DQM*')  # clean up temporary directory when start

if not os.path.exists(TMPDIR +'/timeTag'):
    os.system('touch -t 01010000 '+ TMPDIR +'/timeTag')

####### ENDLESS LOOP WITH SLEEP
while 1:

    #### search new files
    #NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TMPDIR +'/timeTag | grep -v DQM_V').read().split()
    NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TMPDIR +'/timeTag').read().split()
    if len(NEW_)==0:
        print 'waiting for new files...'
        time.sleep(WAITTIME)
        continue
    print os.popen('ls -l '+TMPDIR+'/timeTag').read()
    os.system('touch '+ TMPDIR +'/timeTag')
    print 'Found '+str(len(NEW_))+' new file(s).'


    #### sort new files by run number
    pairs = []
    for fname in NEW_:
        run = fname[-14:-5] #run number of new file
        pairs.append((run,fname))
    pairs.sort()

    #### extract uniq runs
    Runs = []
    for pair in pairs:
        Runs.append(pair[0])
    UniqRuns = list(Set(Runs)) #remove duplicate run
    UniqRuns.sort()

        
    #### loop for runs
    for run in UniqRuns:
        
        ### copy files to temporal directory
        TMP_FILES = []
        for pair in pairs:
            if pair[0]==run:
                fname = pair[1]
                TMP_FILES.append(fname.replace(fname[:fname.find('/DQM')],TMPDIR))
                shutil.copy2(fname,TMPDIR)
                print os.popen('ls -l '+pair[1]).read()

        SUBDIR = '/'+run[0:3]+'/'+run[3:6]+'/'+run[6:9]
        NEWDIR = FILEDIR + SUBDIR # directory, to which merged file is stored
        if not os.path.exists(NEWDIR): os.makedirs(NEWDIR)

        ver = Runs.count(run) # ver: number of new files for this run
        if ver < 10:
            ver = '000' + str(ver)
        elif ver < 100:
            ver = '00' + str(ver)
        elif ver < 1000:
            ver = '0' + str(ver)


        #### merge files and register ####

        ### Check if old merged file exist
        if len(os.popen('ls '+ NEWDIR + '/DQM_V*_R'+run+'.root').read().split()):
            OLD_MERGED = os.popen('ls '+ NEWDIR + '/DQM_V*_R'+run+'*root').read().strip()
            OLD_LOG = OLD_MERGED[:-4]+'log'

            oldver = OLD_MERGED[OLD_MERGED.find('_V')+2:OLD_MERGED.find('_V')+6]
            TMP_OLD_MERGED = TMPDIR+'/DQM_V' + oldver + '_R' + run + '_R' + run +'.root'
            
            ver = int(oldver) + int(ver)
            if ver < 10:
                ver = '000' + str(ver)
            elif ver < 100:
                ver = '00' + str(ver)
            elif ver < 1000:
                ver = '0' + str(ver)
            
            MERGED = NEWDIR+'/DQM_V' + ver + '_R' + run + '_R' + run +'.root'
            LOG = MERGED[:-4]+'log'
            TMP_MERGED = TMPDIR+'/DQM_V' + ver + '_R' + run + '_R' + run +'.root'
            TMP_LOG = TMP_MERGED[:-4]+'log'

            
            shutil.copy(OLD_MERGED, TMP_OLD_MERGED)
            if not os.path.exists(OLD_LOG):
                os.system('touch '+ OLD_LOG)
                print 'log file was lost for unknown reason. It was recreated!!'
            shutil.copy(OLD_LOG, TMP_LOG)

            print 'Run '+run+' is being merged...'
            LOGFILE = open(TMP_LOG,'a')
            LOGFILE.write(os.popen('hadd '+TMP_MERGED+' '+TMPDIR+'/DQM_*_R'+run+'.root').read())
            print 'moving merged file to the master directory'
            os.system('scp '+TMP_MERGED+' '+CMSMON+':'+MERGED)
            os.remove(TMP_MERGED)
            os.remove(TMP_OLD_MERGED)

            tag = 1
            while tag:
                if os.path.exists(MERGED):
                    fileunreg(DB, OLD_MERGED, LOGFILE)
                    os.remove(OLD_MERGED)
                    print 'Start file registering : '+MERGED
                    filereg(DB,MERGED,LOGFILE) #file registration
                    LOGFILE.close()
                    os.system('scp '+TMP_LOG+ ' '+CMSMON+':'+LOG)
                    os.remove(OLD_LOG)
                    os.remove(TMP_LOG)
                    print MERGED + ' is registerd'
                    tag = 0
                else:
                    print 'Cannot start file registering because '+MERGED +' is not created yet!!!'
                    print 'Registeration will start automatically some time later...'
                    time.sleep(60)
        else:
            MERGED = NEWDIR+'/DQM_V' + ver + '_R' + run + '_R' + run +'.root'
            LOG = MERGED[:-4]+'log'
            TMP_MERGED = TMPDIR+'/DQM_V' + ver + '_R' + run + '_R' + run +'.root'
            TMP_LOG = TMP_MERGED[:-4]+'log'

            print 'Run '+run+' is being merged...'
            LOGFILE = open(TMP_LOG,'a')
            if int(ver)==1:
                shutil.copy(TMP_FILES[0],TMP_MERGED)
            else:
                LOGFILE.write(os.popen('hadd '+TMP_MERGED+' '+TMPDIR+'/DQM_*_R'+run+'.root').read())
            print 'moving merged file to the master directory'
            os.system('scp '+TMP_MERGED+' '+CMSMON+':'+MERGED)
            os.remove(TMP_MERGED)

            tag = 1
            while tag:
                if os.path.exists(MERGED):
                    print 'Start file registering : '+MERGED
                    filereg(DB,MERGED,LOGFILE) #file registration
                    LOGFILE.close()
                    os.system('scp '+TMP_LOG+ ' '+CMSMON+':'+LOG)
                    os.remove(TMP_LOG)
                    print MERGED + ' is registerd'
                    tag = 0
                else:
                    print 'Cannot start file registering because '+MERGED +' is not created yet!!!'
                    print 'Registeration will start automatically some time later...'
                    time.sleep(60)

        for file in TMP_FILES:
            os.remove(file)
