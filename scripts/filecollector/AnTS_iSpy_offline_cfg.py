###### GLOBAL CONFIG FILE VARIABLES        ######
DEBUG				= False
FILE_TYPE		= ".ig"  #always include the dot "."

################################
#Directories:                  # 
################################
AFS_BASE_DIR		= "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/ispy-files/data/"
BASE_DIRECTORY	= "/data/ispy-files/data"
CASTOR_BASE			= "/castor/cern.ch/cms/store/temp/dqm"
DROPBOX					= "/data/ispy-files/dropbox"
INSTANCE_DIR		= "online"
REPOSITORY_DIR	= "/data/ispy-files/.repo"
TMP_DROPBOX			= "/data/ispy-files/.dropbox"


################################
#Waiting Times:                # 
################################
CASTOR_WAIT_TIME			= 120
CLASSIFIER_WAIT_TIME	= 120
AFS_FILER_WAIT_TIME		= 120
TIME_OUT							= 600  #time out for command execution

################################
#App Spesific parameters:      # 
################################
#fileClassifier
FILE_NAME_STD	= "iSpy_([_A-Z0-9]*)__([-_a-zA-Z0-9]*)__R([0-9]{9,9})_T([0-9]{8,8}).ig"
ERAS					= ["CRAFT","CRUZET","MWGR","BEAM"]

#afsFiler
QUOTA					= 18*1024*1024*1024 #in bytes
EXCLUDED      = ["2008-BEAM"]  #directories relative to the AFS_BASE_DIR excluded from deletion, 
                               #keep in mind that the size of this directory is not taken in to account for the QUOTA
                               #in other words, QUOTA should be equals to the desired used space - size of excluded directories
