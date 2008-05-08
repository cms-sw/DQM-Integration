#! /usr/bin/env python

import os,time,sys,shutil

def fileunreg(db,file,logfile):
    tmpdb = '/cms/mon/data/.dropbox_test/dqm-tmp.db'
    newdb = db[:-3]+'-new.db'
    server = 'srv-c2d05-19'
    if os.path.exists(tmpdb): os.remove(tmpdb)
    #if os.path.exists(db): shutil.copy2(db, tmpdb)
    logfile.write(os.popen('scp '+server+ ':'+db+' '+tmpdb).read())
    logfile.write('*** File Register ***\n')
    logfile.write(os.popen('visDQMUnregisterFile '+ tmpdb +' ' + file).read())
    #shutil.move(tmpdb, newdb)
    logfile.write(os.popen('scp '+tmpdb+' '+server+':'+newdb).read())
    os.remove(tmpdb)
    #if os.path.exists(db): os.remove(db)
    #os.rename(newdb,db)
    # logfile.write(os.popen('ssh '+server+' -t rm '+db).read())
    logfile.write(os.popen('ssh '+server+' -t mv '+newdb+' '+db).read())

def filereg(db,file,logfile):
    tmpdb = '/cms/mon/data/.dropbox_test/dqm-tmp.db'
    newdb = db[:-3]+'-new.db'
    server = 'srv-c2d05-19'
    if os.path.exists(tmpdb): os.remove(tmpdb)
    #if os.path.exists(db): shutil.copy2(db, tmpdb)
    logfile.write(os.popen('scp '+server+ ':'+db+' '+tmpdb).read())
    logfile.write('*** File Register ***\n')
    logfile.write(os.popen('visDQMRegisterFile '+ tmpdb +' "/Global/Online/ALL" "Global run" '+ file).read())
    #shutil.move(tmpdb, newdb)
    logfile.write(os.popen('scp '+tmpdb+' '+server+':'+newdb).read())
    os.remove(tmpdb)
    #if os.path.exists(db): os.remove(db)
    #os.rename(newdb,db)
    # logfile.write(os.popen('ssh '+server+' -t rm '+db).read())
    logfile.write(os.popen('ssh '+server+' -t mv '+newdb+' '+db).read())

def uniq_chk(filename):
    if os.path.exists(filename):
        log = filename[:-4]+'log'
        newname = filename[:-5]+'.1'+filename[-5:]
        newlog = newname[:-4]+'log'
        uniq_chk(newname)
        os.rename(filename,newname)
        os.rename(log,newlog)
        print filename + ' already exist.: modified the name of existing file.'
    else:
        return
	
# runs for testing 403  409  420  426  429
# find /cms/mon/data/dqm/results -name 'DQM_*_R000038403*.root' | grep -v _RPCexpert_ | xargs visDQMRegisterFile dqm.db /Global/Online/ALL "Global run"
DIR = '/cms/mon/data/dropbox'  # directory to search new files
#DIR = '/cms/mon/data/dropbox_test'  # directory to search new files
#DB = '/cms/mon/data/dqm/dqm.db'
DB = '/home/dqm/dqm.db'
#FILEDIR = '/cms/mon/data/dropbox_test' # directory, to which merged file is stored
FILEDIR = '/cms/mon/data/dqm/results' # directory, to which merged file is stored
TMPDIR = '/cms/mon/data/.dropbox_test' # directory, in which merged file is created
CMSMON = 'srv-c2c06-02' # machine to which merged file is transfered

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
    print 'Found '+str(len(NEW_))+' new file(s).'

    #### sort new files by run number
    pairs = []
    for fname in NEW_:
        run = fname[-14:-5] #run number of new file
        pairs.append((run,fname))
    pairs.sort()

    NEW_ = []
    for pair in pairs:
        NEW_.append(pair[1])
        
    #### loop for new files
    for NEW in NEW_:
        if NEW==NEW_[0]: os.system('touch '+ TMPDIR +'/timeTag')
        run = NEW[-14:-5] #run number of new file
        SUBDIR = '/'+run[0:3]+'/'+run[3:6]+'/'+run[6:9]
        NEWDIR = FILEDIR + SUBDIR # directory, to which merged file is stored
        #NEWDIR = NEW[0:NEW.find('DQM')-1]
        TMP_NEW = TMPDIR + '/'+ NEW[NEW.find('DQM'):]
        print NEW +' is being copied.'
        shutil.copy2(NEW,TMP_NEW)


        #### check if merged file exist
        if len(os.popen('ls '+ TMPDIR + '/DQM_V????_R'+run+'_R'+run+'.root').read().split()):
            TMP_MERGED = os.popen('ls -rt '+ TMPDIR + '/DQM_V????_R'+run+'_R'+run+'.root | tail -1').read().strip()
            TMP_LOG = TMP_MERGED[:-4]+'log'
            irun = TMP_MERGED[-14:-5]
            FILE_EXIST = 1
        elif len(os.popen('ls '+ NEWDIR + '/DQM_V*_R'+run+'_R'+run+'.root').read().split()):
            MERGED = os.popen('ls -rt '+ NEWDIR + '/DQM_V*_R'+run+'_R'+run+'.root | tail -1').read().strip()
            LOG = MERGED[:-4]+'log'
            TMP_MERGED = MERGED.replace(NEWDIR,TMPDIR)
            TMP_LOG = TMP_MERGED[:-4]+'log'
            shutil.copy2(MERGED,TMP_MERGED)
            if not os.path.exists(LOG):
                os.system('touch '+ LOG)
                print 'log file was lost for unknown reason. It was recreated!'
            shutil.copy2(LOG,TMP_LOG)
                
            irun = TMP_MERGED[-14:-5]
            FILE_EXIST = 1
        else:
            FILE_EXIST = 0

        ### if new file has different run number from the previous one, register the previous merged file
        if NEW!=NEW_[0] and run != oldrun:
            ### move previous merged file to master directory & do file registration
            SUBDIR = '/'+oldrun[0:3]+'/'+oldrun[3:6]+'/'+oldrun[6:9]
            NEWDIR = FILEDIR + SUBDIR
            if not os.path.exists(NEWDIR): os.makedirs(NEWDIR)
            NEW_MERGED = TMP_OLD_MERGED.replace(TMPDIR,NEWDIR)
            NEW_LOG = TMP_OLD_LOG.replace(TMPDIR,NEWDIR)
            if len(os.popen('ls '+ NEWDIR + '/DQM_V*_R'+oldrun+'*root').read().split()):
                OLD_MERGED = os.popen('ls '+ NEWDIR + '/DQM_V*_R'+oldrun+'*root').read().strip()
                OLD_LOG = OLD_MERGED[:-4]+'log'
		fileunreg(DB, OLD_MERGED, LOGFILE)
                os.remove(OLD_MERGED)
                os.remove(OLD_LOG)
            uniq_chk(NEW_MERGED) #check if the name of new merged file is unique
            #shutil.move(TMP_OLD_MERGED, NEW_MERGED)
            os.system('scp '+TMP_OLD_MERGED+ ' '+CMSMON+':'+NEW_MERGED)

            tag = 1
            while tag:
                if os.path.exists(NEW_MERGED):
                    os.remove(TMP_OLD_MERGED)
                    print 'Start file registering : '+ NEW_MERGED
                    filereg(DB,NEW_MERGED,LOGFILE) #file registration
                    LOGFILE.close()
                    #shutil.move(TMP_OLD_LOG, NEW_LOG)
                    os.system('scp '+TMP_OLD_LOG+ ' '+CMSMON+':'+NEW_LOG)
                    os.remove(TMP_OLD_LOG)
                    tag = 0
                else:
                    print 'Cannot start file registering because '+NEW_MERGED +' is not created yet!!!'
                    print 'Registeration will start automatically some time later...'
                    time.sleep(60)
                               
        if FILE_EXIST > 0:
            ### create the name of new merged file
            irun = run
            ver = int(TMP_MERGED[TMP_MERGED.find('_V')+2:TMP_MERGED.find('_V')+6])
            ver += 1
            if ver < 10:
                ver = '000' + str(ver)
            elif ver < 100:
                ver = '00' + str(ver)
            elif ver < 1000:
                ver = '0' + str(ver)
                
            ### merge new file in temp area
            TMP_NEW_MERGED = TMPDIR + '/DQM_V' + ver + '_R' + irun + '_R' + irun +'.root'
            TMP_NEW_LOG = TMP_NEW_MERGED[:-4]+'log'
            
            shutil.copy2(TMP_LOG,TMP_NEW_LOG)
            LOGFILE = open(TMP_NEW_LOG,'a')
            print 'merging '+NEW
            #LOGFILE.write(os.popen('hadd '+TMP_NEW_MERGED+' '+NEW+ ' '+TMP_MERGED).read())
            LOGFILE.write(os.popen('hadd '+TMP_NEW_MERGED+' '+TMP_NEW+ ' '+TMP_MERGED).read())
            LOGFILE.flush()
            os.remove(TMP_MERGED)
            os.remove(TMP_NEW)
            os.remove(TMP_LOG)
        else:
            irun = run
            TMP_NEW_MERGED = TMPDIR + '/DQM_V0001_R'+ irun + '_R' + irun +'.root'
            TMP_NEW_LOG = TMP_NEW_MERGED[:-4]+'log'
            #shutil.copy2(NEW,TMP_NEW_MERGED)
            shutil.move(TMP_NEW,TMP_NEW_MERGED)
            LOGFILE = open(TMP_NEW_LOG,'a')

        oldrun = run
        TMP_OLD_MERGED = TMP_NEW_MERGED
        TMP_OLD_LOG = TMP_NEW_LOG
        
        ### move merged file to master directory & do file registration
        if NEW==NEW_[len(NEW_)-1]:
            SUBDIR = '/'+run[0:3]+'/'+run[3:6]+'/'+run[6:9]
            NEWDIR = FILEDIR + SUBDIR
            if not os.path.exists(NEWDIR): os.makedirs(NEWDIR)
            NEW_MERGED = TMP_NEW_MERGED.replace(TMPDIR,NEWDIR)
            NEW_LOG = TMP_NEW_LOG.replace(TMPDIR,NEWDIR)
            if len(os.popen('ls '+ NEWDIR + '/DQM_V*_R'+run+'*root').read().split()):
                OLD_MERGED = os.popen('ls '+ NEWDIR + '/DQM_V*_R'+run+'*root').read().strip()
                OLD_LOG = OLD_MERGED[:-4]+'log'
		fileunreg(DB, OLD_MERGED, LOGFILE)
                os.remove(OLD_MERGED)
                os.remove(OLD_LOG)
            uniq_chk(NEW_MERGED) #check if the name of new merged file is unique
            #shutil.move(TMP_NEW_MERGED, NEWDIR)
            os.system('scp '+TMP_NEW_MERGED+ ' '+CMSMON+':'+NEWDIR)

            tag = 1
            while tag:
                if os.path.exists(NEW_MERGED):
                    os.remove(TMP_NEW_MERGED)
                    print 'Start file registering...'
                    filereg(DB,NEW_MERGED,LOGFILE) #file registration
                    print NEW_MERGED + ' is registerd'
                    LOGFILE.close()
                    #shutil.move(TMP_NEW_LOG, NEWDIR)
                    os.system('scp '+TMP_NEW_LOG+ ' '+CMSMON+':'+NEWDIR)
                    os.remove(TMP_NEW_LOG)
                    tag = 0
                else:
                    print 'Cannot start file registering because '+NEW_MERGED +' is not created yet!!!'
                    print 'Registeration will start automatically some time later...'
                    time.sleep(60)

