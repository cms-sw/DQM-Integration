#! /usr/bin/env python

import os,time,sys,shutil,glob
from sets import Set
from datetime import datetime
import smtplib
from email.MIMEText import MIMEText
from ROOT import TFile

def sendmail(EmailAddress,run):
    s=smtplib.SMTP("localhost")
    tolist=[EmailAddress]
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
        if (hist == None):
            #print "File is incomplete"
            f.Close()
            return 0
        else:
            #print "File is OK"
            f.Close()
            return 1
        

def filereg(db,bakdb,tmpdb,file,logfile):
    #server = 'srv-c2d05-19'
    if os.path.exists(tmpdb): os.remove(tmpdb)
    #logfile.write(os.popen('scp -Cpc blowfish '+server+ ':'+db+' '+tmpdb).read())
    #cmsdb = os.popen('ls -rt ' + bakdb + '* | tail -1').read().strip()
    shutil.copy(db,tmpdb)
    logfile.write('*** File Register ***\n')
    logfile.write(os.popen('visDQMRegisterFile '+ tmpdb +' "/Global/Online/ALL" "Global run" '+ file).read())
    #logfile.write(os.popen('scp -Cpc blowfish '+tmpdb+' '+server+':'+newdb).read())
    #logfile.write(os.popen('ssh '+server+' -t mv '+newdb+' '+db).read())
    t = datetime.now()
    tstamp = t.strftime("%Y%m%d")
    a = glob.glob(bakdb+'.'+tstamp+'*');
    if not len(a):
        tstamp = t.strftime("%Y%m%d_%H%M%S")
        bakdb = bakdb+'.'+tstamp
        shutil.copy(tmpdb,bakdb)
        shutil.move(tmpdb,db)
    else:
        shutil.move(tmpdb,db)

def filereg2(db,bakdb,tmpdb,oldfile,file,logfile):
    if os.path.exists(tmpdb): os.remove(tmpdb)
    shutil.copy(db,tmpdb)
    logfile.write('*** File UnRegister ***\n')
    logfile.write(os.popen('visDQMUnregisterFile '+ tmpdb +' ' + oldfile).read())
    logfile.write('*** File Register ***\n')
    logfile.write(os.popen('visDQMRegisterFile '+ tmpdb +' "/Global/Online/ALL" "Global run" '+ file).read())
    t = datetime.now()
    tstamp = t.strftime("%Y%m%d")
    a = glob.glob(bakdb+'.'+tstamp+'*');
    if not len(a):
        tstamp = t.strftime("%Y%m%d_%H%M%S")
        bakdb = bakdb+'.'+tstamp
        shutil.copy(tmpdb,bakdb)
        shutil.move(tmpdb,db)
    else:
        shutil.move(tmpdb,db)

# The following variables are defined at the mother script (2008/10/01)
#DIR = '/data/dqm/dropbox'  # directory to search new files
#DB = '/home/dqm/dqm.db' #master db
#BAKDB = '/data/dqm/filereg/backups/dqm.db' #bakcup db (timestamp will be attatched)
#TMPDB = '/data/dqm/dropbox/dqm-tmp.db' # temporal db
#FILEDIR = '/data/dqm/results' # directory, to which merged file is stored
#TMPDIR = '/data/dqm/.dropbox_tmp' # directory, in which merged file is created
#TimeTag = '/data/dqm/dropbox/timetag' #file for time tag for searching new file
#LOGDIR = '/data/dqm/filereg/log'
#SIZE_LIMIT = 5000000000  # size limit for merged file (5~10 Gbyte)
#WAITTIME = 120 # waiting time for new files (sec)

#os.popen('rm '+TMPDIR+'/DQM*')  # clean up temporary directory when start

TempTag = TimeTag + '-tmp'
if not os.path.exists(TimeTag):
    os.system('touch -t 01010000 '+ TimeTag)


#### search new files
NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TimeTag +' | grep -v DQM_Reference').read().split()
#NEW_ = os.popen('find '+ DIR +'/ -type f -name "DQM_*_R?????????.root" -newer '+ TimeTag +' | grep -v DQM_SiStrip | grep -v DQM_Reference').read().split()

if len(NEW_)==0:
    print 'Have not found new files...'
    os._exit(99)
print os.popen('ls -l '+TimeTag).read()
#os.system('touch '+ TimeTag)
os.system('touch '+ TempTag)
print datetime.now()
print 'Found '+str(len(NEW_))+' new file(s).'


#### sort new files by run number
pairs = []
for fname in NEW_:
    if filecheck(fname) == 0:
        print fname +' is incomplete. This file would not be merged.'
    else:
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
mergedfiles = []
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
        if os.path.exists(TMP_MERGED): os.remove(TMP_MERGED)
        LOGFILE = open(TMP_LOG,'a')
        LOGFILE.write(os.popen('visDQMMergeFile '+TMP_MERGED+' '+TMPDIR+'/DQM_*_R'+run+'.root').read())

        num = 0
        while not os.path.exists(TMP_MERGED):
            print 'Failed merging files for run '+run+'. Try again after two minutes'
            time.sleep(120)
            num = num + 1
            LOGFILE.write(os.popen('visDQMMergeFile '+TMP_MERGED+' '+TMPDIR+'/DQM_*_R'+run+'.root').read())
            if num > 30:
                break

        if os.path.exists(TMP_MERGED):
            print 'moving merged file to the master directory'
            #os.popen('scp -Cpc blowfish '+TMP_MERGED+' '+CMSMON+':'+MERGED)
            shutil.copy(TMP_MERGED,MERGED)
            os.remove(TMP_MERGED)
            os.remove(TMP_OLD_MERGED)
        else:
            sendmail(YourEmail,run)
            os.remove(TMP_OLD_MERGED)
            LOGFILE.close()
            os.remove(TMP_LOG)
            for file in TMP_FILES:
                os.remove(file)
            continue

        tag = 1
        while tag:
            if os.path.exists(MERGED):
                print 'Start registering : '+MERGED
                filereg2(DB,BAKDB,TMPDB,OLD_MERGED,MERGED,LOGFILE)
                os.remove(OLD_MERGED)
                LOGFILE.close()
                #os.system('scp -Cpc blowfish '+TMP_LOG+ ' '+CMSMON+':'+LOG)
                shutil.copy(TMP_LOG,LOG)
                os.remove(OLD_LOG)
                os.remove(TMP_LOG)
                print MERGED + ' is registerd'
                tag = 0
            else:
                print 'Cannot start file registering because '+MERGED +' is not created yet!!!'
                print 'Registeration will start automatically after 2 minutes...'
                time.sleep(120)
    else:
        MERGED = NEWDIR+'/DQM_V' + ver + '_R' + run + '_R' + run +'.root'
        LOG = MERGED[:-4]+'log'
        TMP_MERGED = TMPDIR+'/DQM_V' + ver + '_R' + run + '_R' + run +'.root'
        TMP_LOG = TMP_MERGED[:-4]+'log'

        print 'Run '+run+' is being merged...'
        if os.path.exists(TMP_MERGED): os.remove(TMP_MERGED)
        LOGFILE = open(TMP_LOG,'a')
        if int(ver)==1:
            shutil.copy(TMP_FILES[0],TMP_MERGED)
        else:
            LOGFILE.write(os.popen('visDQMMergeFile '+TMP_MERGED+' '+TMPDIR+'/DQM_*_R'+run+'.root').read())


        while not os.path.exists(TMP_MERGED):
            print 'Failed merging files for run '+run+'. Try again after two minutes'
            time.sleep(120)
            num = num + 1
            LOGFILE.write(os.popen('visDQMMergeFile '+TMP_MERGED+' '+TMPDIR+'/DQM_*_R'+run+'.root').read())
            if num > 30:
                break
            
        if os.path.exists(TMP_MERGED):
            print 'moving merged file to the master directory'
            #os.system('scp -Cpc blowfish '+TMP_MERGED+' '+CMSMON+':'+MERGED)
            shutil.copy(TMP_MERGED,MERGED)
            os.remove(TMP_MERGED)
        else:
            sendmail(YourEmail,run)
            LOGFILE.close()
            os.remove(TMP_LOG)
            for file in TMP_FILES:
                os.remove(file)
            continue
                
        tag = 1
        while tag:
            if os.path.exists(MERGED):
                print 'Start file registering : '+MERGED
                filereg(DB,BAKDB,TMPDB,MERGED,LOGFILE) #file registration
                LOGFILE.close()
                #os.system('scp -Cpc blowfish '+TMP_LOG+ ' '+CMSMON+':'+LOG)
                shutil.copy(TMP_LOG,LOG)
                os.remove(TMP_LOG)
                print MERGED + ' is registerd'
                tag = 0
            else:
                print 'Cannot start file registering because '+MERGED +' is not created yet!!!'
                print 'Registeration will start automatically some time later...'
                time.sleep(60)

    for file in TMP_FILES:
        os.remove(file)

    mergedfiles.append(MERGED)

shutil.copy2(TempTag,TimeTag)
os.remove(TempTag)
