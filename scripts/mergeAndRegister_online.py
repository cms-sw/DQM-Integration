#! /usr/bin/env python

import os,time,sys,shutil

def filereg(db,file,logfile):
    tmpdb = '/nfshome0/hkseo/dqm-tmp.db'
    newdb = db[:-3]+'-new.db'
    if os.path.exists(tmpdb): os.remove(tmpdb)
    if os.path.exists(db): shutil.copy2(db, tmpdb)
    logfile.write('*** File Register ***\n')
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

#SIZE_LIMIT = 5000000000  # size limit for merged file (5~10 Gbyte)
SIZE_LIMIT =10000000
WAIT = 30 # waiting time for new files (sec)



if not os.path.exists(TMPDIR +'/timeTag'):
    os.system('touch -t 01010000 '+ TMPDIR +'/timeTag')

####### ENDLESS LOOP WITH SLEEP
while 1:

    #### check new files
    NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TMPDIR +'/timeTag').read().split()
    if len(NEW_)==0:
        print 'waiting for new files...'
        time.sleep(WAIT)
        continue

    print 'Found '+str(len(NEW_))+' new file(s).'

    #### loop for new files
    for NEW in NEW_:
        if NEW==NEW_[0]: os.system('touch '+ TMPDIR +'/timeTag')
        print NEW
        TMP_NEW = NEW.replace(DIR,TMPDIR)
        shutil.copy2(NEW,TMP_NEW)

        #### check if merged file exist & the size of the last merged file
        if NEW==NEW_[0]:
            FILE_EXIST = len(os.popen('ls '+ FILEDIR + '/DQM_V*.root').read().split())
            if FILE_EXIST > 0:
                INI_MERGED = MERGED = os.popen('ls -rt '+ FILEDIR + '/DQM_V*.root | tail -1').read().strip()
                INI_LOG = LOG = MERGED[:-4]+'log'
                TMP_MERGED = MERGED.replace(FILEDIR,TMPDIR)
                TMP_LOG = TMP_MERGED[:-4]+'log'
                shutil.copy2(MERGED,TMP_MERGED)
                shutil.copy2(LOG,TMP_LOG)
            else:
                INI_MERGED = FILEDIR + '/DQM_V0000_R000000000-R000000000.root'
                INI_LOG = INI_MERGED[:-4]+'log'
        else:
            FILE_EXIST = len(os.popen('ls '+ TMPDIR + '/DQM_V*.root').read().split())
            if FILE_EXIST > 0:
                TMP_MERGED = os.popen('ls -rt '+ TMPDIR + '/DQM_V*.root | tail -1').read().strip()
                TMP_LOG = TMP_MERGED[:-4]+'log'
                MERGED = TMP_MERGED.replace(TMPDIR,FILEDIR)
                LOG = MERGED[:-4]+'log'
                
        if FILE_EXIST > 0:
            FILE_SIZE = os.path.getsize(TMP_MERGED) + os.path.getsize(NEW)
            if FILE_SIZE > SIZE_LIMIT:
                FILE_EXIST = 0
                if NEW != NEW_[0]:
                    if os.path.exists(INI_MERGED): os.remove(INI_MERGED)
                    uniq_chk(MERGED)
                    shutil.move(TMP_MERGED,MERGED)
                    print 'Start file registering...'
                    LOGFILE = open(TMP_NEW_LOG,'a')
                    filereg(DB,MERGED,LOGFILE) #file registration
                    LOGFILE.close()
                    if os.path.exists(INI_LOG): os.remove(INI_LOG)
                    shutil.move(TMP_LOG,LOG)
        
        run = NEW[-14:-5] #run number of new file

        if FILE_EXIST > 0:

            ### create the name of new merged file
            ver = int(MERGED[-31:-27])
            irun = MERGED[-25:-16]
            frun = MERGED[-14:-5]

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

            ### merge new file in temp area
            TMP_NEW_MERGED = TMPDIR + '/DQM_V' + ver + '_R' + irun + '-R' + frun + '.root'
            TMP_NEW_LOG = TMP_NEW_MERGED[:-4]+'log'

            shutil.copy2(TMP_LOG,TMP_NEW_LOG)
            LOGFILE = open(TMP_NEW_LOG,'a')
            LOGFILE.write(os.popen('hadd '+TMP_NEW_MERGED+' '+TMP_NEW+ ' '+TMP_MERGED).read())
            LOGFILE.flush()
            os.remove(TMP_MERGED)
            os.remove(TMP_NEW)
            os.remove(TMP_LOG)
        else:
            irun = run
            frun = run
            TMP_NEW_MERGED = TMPDIR + '/DQM_V0001_R'+irun+'-R'+frun+'.root'
            TMP_NEW_LOG = TMP_NEW_MERGED[:-4]+'log'
            shutil.move(TMP_NEW,TMP_NEW_MERGED)
            LOGFILE = open(TMP_NEW_LOG,'a')


        ### move merged file to master directory & do file registration
        if NEW==NEW_[len(NEW_)-1]:
            NEW_MERGED = TMP_NEW_MERGED.replace(TMPDIR,FILEDIR)
            NEW_LOG = TMP_NEW_LOG.replace(TMPDIR,FILEDIR)
            if os.path.exists(INI_MERGED): os.remove(INI_MERGED)
            uniq_chk(NEW_MERGED) #check if the name of new merged file is unique
            shutil.move(TMP_NEW_MERGED, FILEDIR)

            print 'Start file registering...'
            filereg(DB,NEW_MERGED,LOGFILE) #file registration
            LOGFILE.close()
            if os.path.exists(INI_LOG): os.remove(INI_LOG)
            shutil.move(TMP_NEW_LOG, FILEDIR)
