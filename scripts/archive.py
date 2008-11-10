#!/usr/bin/env python
import os, time, shutil, zipfile, commands, sys, glob
from datetime import datetime
fileSizeThreshold = 1000000000 # 1GB to get away from technicality of large zip file size
disk_threshold = 80 # 80% full
transferScript = "/nfshome0/tier0/scripts/injectFileIntoTransferSystem.pl"# T0 System Script
targetdir = "/castor/cern.ch/cms/store/dqm/" # Castor Store Area
dir = "/nfshome0/smaruyam/CMSSW_2_0_10/src/test/" # File Directory
dbdir = "/nfshome0/smaruyam/CMSSW_2_0_10/src/test/" # db Directory
cfgfile = " /xxxx/yyyy/config.txt "# configuration file
cfgarg  = " --config " + cfgfile
fullTransferArg = cfgarg + " --type dqm --hostname srv-C2D05-19 --lumisection 1 --appname CMSSW --appversion CMSSW_2_0_10 "
statusCheck = cfgarg + " --check --filename "
emptyString = "empty"

logfile = open('archival_log.txt', 'a')# Redundant, Temporaly Use
tmpdb = dbdir + "tmp/tmp.db"
bakdb = dbdir + "tmp/backup.db"
db = dbdir + "db.db"

"""
Check and Return Output
"""
def CheckCommand(cmd):
	result = commands.getstatusoutput(cmd)
	if result[0] == 0:
		output = result[1]
		return result
	else :
		print "Command Exits with non-zero Status,", result[0]
		return result

"""
Disk Usage Check
df out put is assumed as follows.
Filesystem            Size  Used Avail Use% Mounted on
/dev/sda3              73G   45G   25G  65% /
/dev/sda1              99M   12M   83M  12% /boot
none                  2.0G     0  2.0G   0% /dev/shm
/dev/sdb1             917G   83G  788G  10% /data
cmsnfshome0:/nfshome0
                      805G  673G  133G  84% /cmsnfshome0/nfshome0
"""
def DiskUsage() :
    print " *** Checking Disk Usage ***"
    df_file=os.popen('df')
    usage = False
    lines = df_file.readlines()
    list = lines[4].split() # 5th line from top. Split at tab or white space
    string = list[4][:-1] # NEED check for the host
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
Check File Path on Tape
""" 
def ConfirmPath(file, path) :
	print " *** Checking File Path *** "
	time.sleep(10) 
	fullpath = path + "/" + file[len(dir):]
	mycmd = "rfdir "
	myarg = fullpath
	cmd = mycmd + myarg
	print cmd 
	result = CheckCommand(cmd)
	if result[0] == 0:
		output = result[1]
		if cmp(output,"") != 0:
			for line in output.splitlines():
				print " rfdir result is ",line
				error_check = "No such file or directory"
				if line.find(error_check) != -1 :return emptyString
				print " rfdir result is ",line.split()
				if len(line.split()) > 7:
					string = line.split()[-1]
					print "Last Item is ", string
					print "Last Item is ", fullpath
					if cmp(string,fullpath) == 0: return fullpath
	return emptyString

"""
Scan Directories
"""
def ScanDir(file) :
        mycmd = "rfdir "
        myarg = targetdir
        cmd = mycmd + myarg
        print "Scanning tape area  ",cmd
        result = CheckCommand(cmd)
        if result[0] == 0:
		if cmp(result[1],"") != 0:
	                output = result[1].split('\n')
        	        for line in output :
				if len(line.split()) > 8:
					newpath = targetdir + line.split()[-1]
					print "Looking for File at ", newpath
					confirmpath = ConfirmPath(file, newpath)
					print "Returned Path ", confirmpath
					if cmp(confirmpath, newpath + "/" + file[len(dir):] ) == 0: return confirmpath
	return emptyString

"""
Path Specifier
"""
def CheckPath(filename) :
	mtime = os.stat(filename).st_mtime
	year = time.localtime(mtime)[0]
        month = time.localtime(mtime)[1]
	if month > 9: yearmonth = str(year) + str(month)
	else: yearmonth = str(year) + "0" + str(month)
        path = targetdir + yearmonth
	print "Best Guess for the path is ", path
        newpath = ConfirmPath(filename, path)
        if cmp(newpath,emptyString) != 0 : return newpath
        else :# scan all path
		newpath = ScanDir(filename)
		return newpath

"""
Set Path
"""
def SetPath(file):
	path = CheckPath(file)
	print path
	if cmp(path,emptyString) != 0:
		newpath = "rfio:" + path
		print "Register New Path ", newpath
		filereg(db,bakdb,tmpdb,newpath,logfile)
		return True
	else :print "File Transferred, but not found on tape\n"
	return False

"""
File Cleaner, Remove the oldest file
"""
def Cleaner() :
	print " *** Cleaning File ***"
	files = GetAllFiles()
	for file in files:
		if file.find(".zip") != -1:#zip file
			status = CheckFileStatus(file)# check transfer status
			if status is True:
				pathfind = SetPath(file)
				if pathfind is True :# path found on tape
					Delete(file)# remove only if transferred 
					return # exits when the files deleted
		if file.find(".root") != -1:
			Delete(file)
			return # exits when the file deleted
	else : print "No File to be removed!\n"

"""
Getting All Files from DB
"""
def GetAllFiles() :
	print " *** Getting All Files from db ***"
        sqlite = db + " \"select name from t_files where name like '%DQM%.root' or name like '%DQM%.zip'order by mtime asc\""
	mycmd = "sqlite3 "
	myarg = sqlite
	cmd = mycmd + myarg
	result = CheckCommand(cmd)
	if result[0] == 0:
		output = result[1].split('\n')
		return output
	else : return emptyString

"""
Check File Status
"""
def CheckFileStatus(filepath):
        filename = filepath[len(dir):]
	print filename
	checkString = statusCheck + filename
	mycmd = transferScript
	myarg = checkString
	cmd = mycmd + myarg
	result = CheckCommand(cmd)
	if result[0] == 0:
		output = result[1].split('\n')
		for line in output:
			print line
			if line.find("FILES_TRANS_CHECKED: File found in database and checked by T0 system.") != -1: return True
			elif line.find("File not found in database.") != -1: return False
	flag = True
	TransferWithT0System(filepath,flag)
	mtime = os.stat(filepath).st_mtime
	print "Old M Time is ", mtime
	os.utime(filepath,None)# change mtime to help path search
	mtime2 = os.stat(filepath).st_mtime
	print "New M Time is ", mtime2
	return False

"""
Transfer File with T0 System
"""
def TransferWithT0System(filepath, flag):
	filename = filepath[len(dir):]
	nrun = filepath[len(dir)+len("DQM_Online_R"):-len("_R000064807.zip")]
	transfer_string = transferScript + " --runnumber " + nrun + " --path " + dir + " --filename " + filename
#	transfer_string += " --test " # TEST, no file transfer, REMOVE this line if transfer is needed!
	if flag is True: transfer_string += " --renotify "# transfer failed previously, trying to send it again
	mycmd = transfer_string
	myarg = fullTransferArg
	cmd = mycmd + myarg
	print cmd
	result = CheckCommand(cmd)
	if result[0] == 0:
		output = result[1].split('\n')
		for line in output:
			print line
        	        if line.find("File sucessfully submitted for transfer.") != -1 and flag is False:
                	        print "%s is queued " %filepath
                        	return True
        	        if line.find("File sucessfully re-submitted for transfer.") != -1 and flag is True:
                	        print "%s is resubmitted " %filepath
                        	return True
	return False

"""
Read and sort file from db
"""
def GetFileFromDB():
	print " *** Getting Merged File List from Master DB ***"
	string = "'%DQM_V%_R%.root'"
        search1 = "'%RPC%'"
        search2 = "'%zip%'"
        sqlite = " %s \"select name, size, mtime from t_files where name like %s and not name like %s and not name like %s order by mtime asc\" "  %(db, string, search1, search2)
	mycmd = "sqlite3"
	myarg = sqlite
	cmd = mycmd + myarg
        result = CheckCommand(cmd)
        if result[0] == 0:
                return result[1]
	else: return emptyString

"""
Get List of un-merged files
"""
def GetListOfFiles():
	print "Retrieving list of files from DB ...\n"
	totalSize = 0
	zipFileList = ''
	fileList = GetFileFromDB().split('\n')
	for line in fileList:
		if cmp(line,"") != 0 and cmp(line,emptyString) != 0:
			string = line.rstrip().split('|')
			name = string[0]
			print name
			print "String just read is ", string
			number = string[1]
			print "Number just read is ", number
			totalSize += int(number)
			print "Current File Size Sum is ", totalSize, " out of Limit", fileSizeThreshold
			zipFileList += " " + name
			if totalSize > fileSizeThreshold:
        			return zipFileList
	return emptyString # it's too small

"""
Temporary Port form Hyunkwan's Un-Register-File Script
"""
def filereg(db,bakdb,tmpdb,file,logfile):
    if os.path.exists(tmpdb): os.remove(tmpdb)
    shutil.copy(db,tmpdb)
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

def fileunreg(db,bakdb,tmpdb,oldfile,logfile):
    if os.path.exists(tmpdb): os.remove(tmpdb)
    shutil.copy(db,tmpdb)
    logfile.write('*** File UnRegister ***\n')
    logfile.write(os.popen('visDQMUnregisterFile '+ tmpdb +' ' + oldfile).read())
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

"""
Remove and Unregister Files
"""
def Remove(oldFiles):
	print "Removing Files ... "
	for file in oldFiles.split():
		Delete(file)

"""
Remove and Register Files
"""
def RemoveAndRegister(newFile,oldFiles):
        for file in oldFiles.split():
		newpath = newFile + "#" + file[len(dir):]
		print "Registering New File Path ", newpath
		filereg(db,bakdb,tmpdb,newpath,logfile)
                Delete(file)

"""
Remove and Unregister A File
"""
def Delete(file):
	fileunreg(db,bakdb,tmpdb,file,logfile)
	print file, "removed from db..."
	os.remove(file)
	print file, "removed from disk..."

"""
Main Prog
"""
if __name__ == "__main__":
	print "Starting Archival *Test* Script ...\n"
	DiskUsage()# check disk usage
	zipFileList = GetListOfFiles() # get list of files for merging
	print zipFileList
	if cmp(zipFileList, emptyString) == 0 : print "Sum of Files is below Threshold = ", fileSizeThreshold, "\n"
	else :# make zip file only if the output file will be large enough
		firstFile = "DQM_Online_" + zipFileList.split()[0][len(dir)+len("DQM_V0010_"):-len("R000064807.root")]
		lastFile  = zipFileList.split()[-1][len(dir)+len("DQM_V0010_R000064807_"):-len(".root")]
		outputFileName = dir + firstFile + lastFile + ".zip"
		print "1st File = ", firstFile, " Last File = ", lastFile
		if os.path.exists(outputFileName) is True: os.remove(outputFileName)# remove old one if exists
		if lastFile.find("R") != -1 and firstFile.find("R") != -1:
			zip = zipfile.ZipFile(outputFileName, "w")# create zip file
			for name in zipFileList.split():
				print name
				zip.write(name,os.path.basename(name), zipfile.ZIP_STORED)# add each file
			zip.close()# close zip file
			filepath = outputFileName
			zipFileSize = os.path.getsize(filepath)
			print "Zip File Size = ",zipFileSize 
			if zipFileSize > fileSizeThreshold :# check if file is large enough 
				zip = zipfile.ZipFile(outputFileName, "r")# open file to see it readable
				for info in zip.infolist():# print to see zipfile is uncompressed
					print info.filename, info.date_time, info.file_size, info.compress_size
				zip.close()# close zip file
#				filereg(db,bakdb,tmpdb,filepath,logfile)
				flag = False# brand new transfer 
				transfer = TransferWithT0System(filepath,flag)# Sending file to Castor
				if transfer is True: RemoveAndRegister(filepath,zipFileList)# register newpaths and remove files
			else: raise RuntimeError
		else: raise RuntimeError
	logfile.close()
