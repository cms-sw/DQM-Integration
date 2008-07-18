#!/usr/bin/env python
import os, time
#import mergeAndRegister_online.fileunreg 
#DB = '/home/dqm/dqm.db'
LOGFILE = open('archival_log.txt', 'a')

#local testing area
dir = "/nfshome0/smaruyam/CMSSW_2_0_10/src/DQM/Integration/scripts/tmp/" # Execution Directory, Local now
db =  "/nfshome0/smaruyam/CMSSW_2_0_10/src/DQM/Integration/scripts/tmp/tmp.db" # master db
adb = "/nfshome0/smaruyam/CMSSW_2_0_10/src/DQM/Integration/scripts/tmp/archival.db" # archival db
transfer_script = "/nfshome0/tier0/scripts/injectFileIntoTransferSystem.pl --type dqm --hostname srv-c2c06-02.cms --lumisection 1 --appname CMSSW --appversion CMSSW_2_0_10 "
bare_script = "/nfshome0/tier0/scripts/injectFileIntoTransferSystem.pl "
test_mode = "--destination TransferTest "
logic_test = "--test "
mock_up_mode = True
targetdir = "/castor/cern.ch/cms/store/data/dqm/" # Path to Castor
Null = "null"
disk_threshold = 80.0  # disk usage threshold, 80% now

"""
Temporary Port form Hyunkwan's Un-Register-File Script
"""
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

"""
Archiving Files
"""
def Archive() :
    print " *** Starting Archiver ***"
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
    print " *** Checking Disk Usage ***"
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
def ConfirmSize(filename, size) : # Disabled NOW
    print " *** Confirming Copied File Size for *** " , filename
    time.sleep(10)
 #   ls = "ls -l " + pnfsdir + filename
    ls = "rfdir " + targetdir + filename
#    print ls
    result = os.popen('%s' %ls)
#    print result
    for line in result.readlines() :
        error_check = "%s%s: No such file or directory" %(targetdir, filename)
        if cmp(line, error_check) == 0 :
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
Check File Path on Tape
"""
def ConfirmPath(filename, path) : # Disabled NOW
    print " *** Checking File Path *** " , filename
    time.sleep(10) 
 #   ls = "ls -l " + pnfsdir + filename 
    ls = "rfdir " + path + "/" + filename 
#    print ls 
    result = os.popen('%s' %ls) 
#    print result 
    for line in result.readlines() : 
        error_check = "%s%s: No such file or directory" %(targetdir, filename)
        if cmp(line, error_check) == 0 : 
            return False 
        else : return True 

"""
Path Specifier
"""
def CheckPath(filename) :
	tm = time.localtime(time.time())
        yearmonth = time.strftime("%Y%m", tm) 
	path = targetdir + yearmonth
	flag = ConfirmPath(filename, path)
	if flag is True : return path
	else :
		ppath = PreviousMonth(path)
	        flag = ConfirmPath(filename, ppath)
	        if flag is True : return ppath
		else :
	                npath = NextMonth(path)
        	        flag = ConfirmPath(filename, npath)
                	if flag is True : return npath
	                else : return Null ## Just for now! It should be crashed here

"""
PreviousMonth
"""
def PreviousMonth(path) :
	year = int(path[-6:-2])
	month= int(path[-2:])
	firstdigit = int(path[-1])
	if cmp(month, 01) == 0  :
		month = 12
		year = year - 1
		path = targetdir + str(year) + str(month)
		return path
	else :
		if month is 10 : month = "09"
		elif month is 11 : month = 10
		elif month is 12 : month = 11
		else : 
			firstdigit = firstdigit - 1
		path = targetdir + str(year )+ "0" + str(firstdigit)
		return path

""" 
NextMonth 
"""
def NextMonth(path) : 
	year = int(path[-6:-2])
	month= int(path[-2:])
	firstdigit = int(path[-1])
        if cmp(month, 12) == 0  :
                month = "01" 
                year = year + 1 
		path = targetdir + str(year) + str(month)
		return path
        else : 
                if cmp(month, "09") == 0 : month = 10
		elif month is 10 : month = 11
		elif month is 11 : month = 12
                else :  
                        firstdigit = firstdigit + 1
		path = targetdir + str(year )+ "0" + str(firstdigit)
		return path


"""
File Cleaner
"""
def Cleaner() :
    print " *** Cleaning File ***"
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
    print " *** Getting Merged File List from Master DB ***"
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
not null, size integer not null, mtime integer not null, atime text not null, status text null, path text null);
"""
def CheckPrivateDB(filepath) :
    string = filepath.split('|')
    print " *** Checking Archival DB ***"
    search = "'" + string[0] + "'"
    sqlite = "sqlite3 %s \"select status from t_files where name like %s \""  %(adb, search)
    result = os.popen(sqlite)
#    print result
    check_result = result.readlines()
#    print " Read Length is " , len(check_result)
    if len(check_result) == 0 :
        return Null # no entry
    else :
        return check_result[0].rstrip() # entry exist


"""
Tranfer Merged Files
"""
def Transfer() :
    print " *** Starting File Transfer ***"
    flag = False
    mergedfiles = GetListFromMasterDB(flag) # Retrieve Merged File List 
    for file in mergedfiles :
#        print file
        string = file.split('|')
	archived = CheckPrivateDB(string[0])
        if archived is Null :
            print "Brand New File "
            SendFile(string[0], archived)
        elif cmp(archived, "queued") == 0 :
            print "Queued File "
            SendFile(string[0], archived)
        elif cmp(archived, "archived") == 0 : print " Already Archived! "


"""
Update Private DB for Archival Information
"""
def UpdatePrivateDBForArchival(filepath, status, path) :
    print " *** Updating Archival DB ***"
    name = filepath
    size = os.path.getsize(filepath) 
    mtime = os.path.getmtime(filepath)
    tm = time.localtime(time.time())
    atime = time.strftime("%Y/%m/%d", tm) 

    if cmp(status,"queued") == 0 :
	    sqlite = "sqlite3 %s \"insert into t_files(name, size, mtime, atime, status, path) values('%s', '%d', '%d', '%s', '%s', '%s')\""  %(adb, name, size, mtime, atime, status, path)
	    result = os.popen(sqlite)
	    check_result = result.readlines()
#    print " Read Length is " , len(check_result)
	    if len(check_result) == 0 :
	        return True
	    else : return False
    if cmp(status,"archived") == 0 :
	    sqlite = "sqlite3 %s \"update t_files set status = '%s' where name = '%s';\""  %(adb, status, filepath)
	    result = os.popen(sqlite)
	    check_result = result.readlines()
#    print " Read Length is " , len(check_result)
	    if len(check_result) == 0 :
	        return True
	    else : return False
    if cmp(status,"archived") != 0 and cmp(status,"queued") != 0 : print " ***** Logic Flaw !!!! ****"


"""
Create a DB if not present
"""
def CreatePrivateDBForArchival() :
    print " *** Creating Archival DB ***"
    sqlite = "sqlite3 %s \"CREATE TABLE t_files (id integer primary key autoincrement, name text unique not null, size integer not null, mtime integer not null, atime text not null, status text null, path text null); \" " %adb
    result = os.popen(sqlite)
    check_result = result.readlines()
#    print " Read Length is " , len(check_result)
    if len(check_result) == 0 :
        return True
    else : 
        print result
        return False

"""
Mock Up Transfer System
to avoid creating null entries in db
"""
def MockUp(filepath) :
    print " *** Mock-Up Transfer Mode ***"
    success_string = "Warning: No filesize supplied (or filesize=0 chosen), but hostname = this machine: using size of file on disk\nDB inserts completed, running Tier 0 notification script\nFile sucessfully submitted for transfer.\n"
    fail_string = "Warning: No filesize supplied (or filesize=0 chosen), but hostname = this machine: using size of file on disk\nError: Found file in DB. To see its status please execute:\n /nfshome0/tier0/scripts/injectFileIntoTransferSystem.pl --check --filename test_transfer_test.root\n"
    check = CheckPrivateDB(filepath)
    if cmp(check, Null) == 0 : return success_string.splitlines()
    else : return fail_string.splitlines()

""" 
Mock Up Transfer System 
to avoid creating null entries in db 
""" 
def MockUpStatus(filepath) : 
    print " *** Mock-Up Status Mode ***"
    success_string = "FILES_TRANS_INSERTED: File found in database and sucessfully processed by T0 system.\n"
    fail_string = "File not found in database.\n"
    check = CheckPrivateDB(filepath) 
    if cmp(check,Null) == 0 : return fail_string.splitlines() 
    else : return success_string.splitlines()


"""
copy file to dcache or castor
"""
def SendFile(filepath, status) :
#    print " Status is " , status
    path = "null"
#    print "Shipping %s to %s" %(filepath, targetdir)
#   Assumed root name =  DQM_Vxx_Ryyyyyyyyy-Rzzzzzzzzz.root
    filename = filepath[-34:] # file name only
    if status is Null :
    	print " *** Shipping %s to Castor ***" %filepath
	nrun = filename[9:-16]
#    print nrun
	pathtofile = filepath[:-34]
#    print pathtofile
#    print filename

#    cdir = os.popen('pwd')
#    pwd = cdir.readline().rstrip()
#    print pwd
#    print "srmcp -debug==true file:////%s/%s \"%s%s\"" %(pwd, filepath, targetdir, filename)

#    result = os.popen('srmcp -debug==true file:////%s/%s "%s%s"' %(pwd, filepath, targetdir, filename) )
	if mock_up_mode == True :
		result = MockUp(filepath)
	else : 
		transfer_string = transfer_script + "--runnumber " + nrun + "--filepath " + pathtofile + "--filename " + filename
		tmp = os.popen('%s' %transfer_string )
		result = tmp.readlines() 
#	print result
	check = False
	for line in result :
		if cmp(line,"File sucessfully submitted for transfer.") == 0:
			check = True
			status = "queued"
        		print "%s is queued " %filepath
	        	update = UpdatePrivateDBForArchival(filepath, status, path)
        		if update is False : print "Updating Private DB Failed !"
	        	time.sleep(10)
			break
		elif cmp(line, "Error: Found file in DB. To see its status please execute:") == 0:
			print " Transfer Failed, because the file already exists on Tape! If not, you need rename the file name. " , result 
        	        break
		else : continue
	if check == False :
		print " Transfer Failed, because "  , result
		return 0

    if cmp(status, "queued") == 0 : 
    	print " *** Checking File Status ***", filepath
#    ls = "ls -l " + filename
	if mock_up_mode == True : result = MockUpStatus(filepath)
	else :    
		check_status = bare_script + "--check --filename " + filename
		time.sleep(10)
		tmp = os.popen('%s' %check_status)
		result = tmp.readlinese()
#	print result 
#    size = ""
	success = False
	for line in result :
		if cmp(line, "FILES_TRANS_INSERTED: File found in database and sucessfully processed by T0 system.") == 0:
			success = True
			status = "archived"
			path = CheckPath(filename)
			break
#        string = line.split()
#        print string
#        if len(string) == 9 :
#            print string[4]
#            size = string[4]
#    success = False
#    counter = 0
#    while success == False and counter < 5 : # repeat up to five times
#        counter += 1
#        success = ConfirmSize(filename, size)
#        if success is False :  ## now error check srmcp 
#            print "File Transfer Failed. This is %d time(s) Failure: "  %counter 
#        else : continue
	if success is True :
        	print "%s is copied " %filepath
	        update = UpdatePrivateDBForArchival(filepath, status, path)
        	if update is False : print "Updating Private DB Failed !"
	        time.sleep(10)
	elif success is False : print "Copying File was Failed! "
    if cmp(status,Null) != 0 and cmp(status,"queued") != 0 and cmp(status,"archived") is not 0: print " ********** Logic Flaw *** Unreachable !!!! "

"""
Remove file from disk
"""
def Remover(filepath) :
    print "Removeing File: %s" %filepath
    result = os.popen('rm -f %s' %filepath)
    for line in result.readlines() :
        if line == "" :  ## now error check rm
            print "File Removed"
            fileunreg(db, filepath, LOGFILE) #def fileunreg(db,file,logfile):
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
    LOGFILE.close()
