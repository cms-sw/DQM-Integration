#! /usr/bin/env python

import os,time,sys,shutil

def filereg(db,file,logfile):
    tmpdb = '/nfshome0/hkseo/dqm-tmp.db'
    newdb = db[:-3]+'-new.db'
    if os.path.exists(tmpdb): os.remove(tmpdb)
    if os.path.exists(db): shutil.copy2(db, tmpdb)
    logfile.write(os.popen('visDQMRegisterFile '+ tmpdb +' "/Global/Online/ALL" "Global run" '+ file).read())
    shutil.move(tmpdb, newdb)
    if os.path.exists(db): os.remove(db)
    os.rename(newdb,db)

def uniq_chk(filename):
    if os.path.exists(filename):
        log = filename[:-4]+'log'
        newname = filename[:-27]+'.1'+filename[-27:]
        newlog = newname[:-4]+'log'
        uniq_chk(newname)
        os.rename(filename,newname)
        os.rename(log,newlog)
        print filename + ' already exist.: modified the name of existing file.'
    else:
        return
	
# runs for testing 403  409  420  426  429
# find /cms/mon/data/dqm/results -name 'DQM_*_R000038403*.root' | grep -v _RPCexpert_ | xargs visDQMRegisterFile dqm.db /Global/Online/ALL "Global run"
DIR = '/cms/mon/data/dropbox_test'
#DIR = '/cms/mon/data/dqm/results/000/038/483'
DB = '/cms/mon/data/dqm/dqm.db' #mastor db: /cms/mon/data/dqm/dqm.db
FILEDIR = '/cms/mon/data/archive_test'
TMPDIR = '/nfshome0/hkseo/tmp'

if not os.path.exists(TMPDIR +'/timeTag'):
    os.system('touch -t 01010000 '+ TMPDIR +'/timeTag')

####### ENDLESS LOOP WITH SLEEP
while 1:

    #### check new files
    NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TMPDIR +'/timeTag').read().split()
    if len(NEW_)==0:
        print 'waiting for new files...'
        time.sleep(30)
        continue

    #### loop for new files
    for NEW in NEW_:
        print NEW
        time.sleep(1)

        if NEW==NEW_[0]: os.system('touch '+ TMPDIR +'/timeTag')

        #### extract run number of new file
        run = NEW[-14:-5]

        #### check if merged file exist & the size of the last merged file
        FILE_EXIST = len(os.popen('ls '+ TMPDIR + '/DQM_V*.root').read().split())
        SIZE_LIMIT = 10000000

        if FILE_EXIST > 0:
            FILE = os.popen('ls -rt '+ TMPDIR + '/DQM_V*.root | tail -1').read().strip()
            LOG = FILE[:-4]+'log'
            FILE_SIZE = os.path.getsize(FILE) + os.path.getsize(NEW)
            if FILE_SIZE > SIZE_LIMIT:
                FILE_EXIST = 0
                if NEW != NEW_[0]:
                    filereg(DB,FILE,LOGFILE) #file registration
                    LOGFILE.close()
		    
		    

        if FILE_EXIST > 0:
            ver = int(FILE[-31:-27])
            irun = FILE[-25:-16]
            frun = FILE[-14:-5]

            ### create the name of new merged file
            if run > frun:
                frun = run
            elif run < irun:
                irun = run

            ver += 1
            if ver < 10:
                ver = '000' + str(ver)
            elif ver < 100:
                ver = '00' + str(ver)
            elif ver < 1000:
                ver = '0' + str(ver)
                
            NEW_MERGED = TMPDIR + '/DQM_V' + ver + '_R' + irun + '-R' + frun + '.root'
	    NEW_ARCHIVED = FILEDIR + '/DQM_V' + ver + '_R' + irun + '-R' + frun + '.root'
            NEW_LOG = NEW_MERGED[:-4]+'log'
            uniq_chk(NEW_MERGED) #check if the name of new merged file is unique

            ### merge new file
            shutil.copy2(LOG,NEW_LOG)
            LOGFILE = open(NEW_LOG,'a')
            LOGFILE.write(os.popen('hadd '+NEW_MERGED+' '+NEW+ ' '+FILE).read())
            LOGFILE.flush()
            os.remove(FILE)
            os.remove(LOG)
        else:
            irun = run
            frun = run
            NEW_MERGED = TMPDIR + '/DQM_V0001_R'+irun+'-R'+frun+'.root'
	    NEW_ARCHIVED = FILEDIR + '/DQM_V0001_R' + irun + '-R' + frun + '.root'
            NEW_LOG = NEW_MERGED[:-4]+'log'
            uniq_chk(NEW_MERGED) #check if the name of new merged file is unique

            shutil.copy(NEW,NEW_MERGED)
            LOGFILE = open(NEW_LOG,'a')
	    
        shutil.move(NEW_MERGED, FILEDIR)	    

        if NEW==NEW_[len(NEW_)-1]:
            filereg(DB,NEW_ARCHIVED,LOGFILE) #file registration
            LOGFILE.flush()
