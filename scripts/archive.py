#!/usr/bin/env python
import os, time
#import fileunreg from mergeAndRegister_online.py 
#def fileunreg(db,file,logfile):

#local testing area
dir = "/afs/cern.ch/user/s/smaruyam/CMSSW_2_0_6/src/DQM/Integration/scripts/tmp/" # Execution Directory, Local now
db = "/afs/cern.ch/user/s/smaruyam/CMSSW_2_0_6/src/DQM/Integration/scripts/tmp/tmp.db" # master db
adb = "/afs/cern.ch/user/s/smaruyam/CMSSW_2_0_6/src/DQM/Integration/scripts/tmp/archival.db" # archival db
targetdir = "/castor/cern.ch/user/s/smaruyam/Archive/" # Command for Archival, Local now
#pnfsdir = "/pnfs/cms/WAX/2/mayaruma/Archive/" # Directory on Tape, dCache now
disk_threshold = 80.0  # disk usage threshold, 80% now

"""
Archiving Files
"""
def Archive() :
    print "Starting Archiver "
    if os.path.exists(adb) is False : CreatePrivateDBForArchival()
#    count = 0
#    DiskUsage()   # disabeled for now
    Transfer()
#        diskusage = False # for test

"""
Disk Usage Check
df out put is assumed as follows.
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev/sda3             78012484   2627788  71421864   4% /
/dev/sda1               101086     11487     84380  12% /boot
none                   2068904         0   2068904   0% /dev/shm
/dev/sdb1            5046428668 635248096 4154836768  14% /cms/mon/data
cmsnfshome0:/nfshome0
                     412849344 270910144 120967680  70% /cmsnfshome0/nfshome0
# cmsmon is 5th line from top.
"""
def DiskUsage() :
    print "Checking Disk Usage"
    df_file=os.popen('df')
    usage = False
    lines = df_file.readlines()
    list = lines[4].split() # 5th line from top. Split at tab or white space
    string = list[4][:-1] # NEED check for cmsmon #
    fusage = float(string)
    print fusage
    if fusage > disk_threshold : # disk is more than 80% full
        print "Disk Usage too high"
        usage = True
    if usage == True :
        Cleaner()
    else :
        print "Disk Usage is low enough"


"""
check copied file and its size
rfdir out put is assumed as follows.
-rw-r--r--   1 smaruyam zh                         10 May 08 22:35 /castor/cern.ch/user/s/smaruyam/Archive/test.txt
"""
def ConfirmSize(filename, size) :
    print "Confirming Copied File Size for " , filename
    time.sleep(10)
 #   ls = "ls -l " + pnfsdir + filename
    ls = "rfdir " + targetdir + filename
#    print ls
    result = os.popen('%s' %ls)
#    print result
    for line in result :
        error_check = "%s%s: No such file or directory" %(targetdir, filename)
        if line == error_check :
            return False
        else :
#            print line
            string = line.split()
            if len(string) == 9 :
#                print string[4]
                if string[4] == size :
                    print "Size matched, Copy Success"
                    return True
                else : return False
            else : return False

"""
File Cleaner
"""
def Cleaner() :
    print "Cleaning File"
    flag = True
    archivedfiles = GetListFromMasterDB(flag).readlines()
    if len(archivedfiles) != 0 :
        string = archivedfiles[0].rstrip() 
        string.split()
        filepath = string[0]
        Remover(filepath)
    if len(archivedfiles) == 0 : print "Cleaning Failed because DB gave a Null List!"


"""
Master DataBase Reference
"""
def GetListFromMasterDB(flag) :
    print "Getting Merged File List from Master DB"
    if flag is False : # Retrive Merged File Info Only
        string = "'" + dir + "DQM_V%_R%.root" + "'"
#        print string
        search = "'%RPC%'" 
        sqlite = "sqlite3 %s \"select name, size, mtime from t_files where name like %s and not name like %s \" "  %(db, string, search)
        result = os.popen(sqlite)
#        print result
        return result
    if flag is True : # Retrive Merged and Un-Merged File Info # Need check on Un-Merged Files DB (where is it?)
        sqlite = "sqlite3 %s \"select name, mtime from t_files where name like '%DQM%.root' order by mtime asc\""  %db
        result = os.popen(sqlite)
#        print result
        return result


"""
Private DataBase Check
Private DB is asuumed as follows.
CREATE TABLE t_files (id integer primary key autoincrement, name text unique
not null, size integer not null, mtime integer not null, atime text not null);
"""
def CheckPrivateDB(filepath) :
    string = filepath.split('|')
    print "Checking Archival DB for " , string[0]
    search = "'" + string[0] + "'"
    sqlite = "sqlite3 %s \"select name, size, mtime, atime from t_files where name like %s \""  %(adb, search)
    result = os.popen(sqlite)
#    print result
    check_result = result.readlines()
#    print " Read Length is " , len(check_result)
    if len(check_result) == 0 :
        return False # no entry
    else :
        return True # entry exist


"""
Tranfer Merged Files
"""
def Transfer() :
    print "Starting File Transfer"
    flag = False
    mergedfiles = GetListFromMasterDB(flag) # Retrieve Merged File List 
    archived = True
    for file in mergedfiles :
#        print file
        string = file.split('|')
        archived = CheckPrivateDB(string[0])
        if archived is False :
#        print "Here is Root File List ", mergedfiles
            SendFile(string[0])
        else : continue


"""
Update Private DB for Archival Information
"""
def UpdatePrivateDBForArchival(filepath) :
    print "Updating Archival DB for " , filepath
    name = filepath
    size = os.path.getsize(filepath) 
    mtime = os.path.getmtime(filepath)
    tm = time.localtime(time.time())
    atime = time.strftime("%Y/%m/%d", tm) 
    sqlite = "sqlite3 %s \"insert into t_files(name, size, mtime, atime) values('%s', '%d', '%d', '%s')\""  %(adb, name, size, mtime, atime)
    result = os.popen(sqlite)
    check_result = result.readlines()
#    print " Read Length is " , len(check_result)
    if len(check_result) == 0 :
        return True
    else : return False

"""
Create a DB if not present
"""
def CreatePrivateDBForArchival() :
    print "Creating Archival DB"
    sqlite = "sqlite3 %s \"CREATE TABLE t_files (id integer primary key autoincrement, name text unique not null, size integer not null, mtime integer not null, atime text not null); \" " %adb
    result = os.popen(sqlite)
    check_result = result.readlines()
#    print " Read Length is " , len(check_result)
    if len(check_result) == 0 :
        return True
    else : 
        print result
        return False


"""
copy file to dcache or castor
"""
def SendFile(filepath) :
    print "Shipping %s to %s" %(filepath, targetdir)
#   Assumed root name =  DQM_Vxx_Ryyyyyyyyy-Rzzzzzzzzz.root
    filename = filepath[-34:] # file name only
#    print filename

#    cdir = os.popen('pwd')
#    pwd = cdir.readline().rstrip()
#    print pwd
#    print "srmcp -debug==true file:////%s/%s \"%s%s\"" %(pwd, filepath, targetdir, filename)

#    result = os.popen('srmcp -debug==true file:////%s/%s "%s%s"' %(pwd, filepath, targetdir, filename) )
    result = os.popen('rfcp %s %s' %(filepath, targetdir) )
#    print result

#    ls = "ls -l " + filename
    ls = "rfdir %s%s" %(targetdir, filename)
#    print ls 
    time.sleep(10)
    result = os.popen('%s' %ls)
#    print result 
    size = ""
    for line in result.readlines() :
#        print line
        string = line.split()
#        print string
        if len(string) == 9 :
#            print string[4]
            size = string[4]
    success = False
    counter = 0
    while success == False and counter < 5 : # repeat up to five times
        counter += 1
        success = ConfirmSize(filename, size)
        if success is False :  ## now error check srmcp 
            print "File Transfer Failed. This is %d time(s) Failure: "  %counter 
        else : continue
    if success is True :
            print "%s is copyied " %filepath
            update = UpdatePrivateDBForArchival(filepath)
            if update is False : print "Updating Private DB Failed !"
            time.sleep(10)
    if success is False : print "Copying File was Failed! "


"""
Remove file from disk
"""
def Remover(filepath) :
    print "Removeing File: %s" %filepath
    result = os.popen('rm -f %s' %filepath)
    for line in result.readlines() :
        if line == "" :  ## now error check rm
            print "File Removed"
        else :
            print "Cannot Remove This File because ", line

"""
Main Script
"""
if __name__ == "__main__":
####### ENDLESS LOOP
    print "Starting Test Script ..."
    count = 0
    while True :
        Archive()
        count += 1
        print "Looping " , count, "Time(s)"
        if count >= 2 : break
        else : continue
