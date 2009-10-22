################################
#Global Variables:             # 
################################

YourEmail='lilopera@cern.ch'
ServerMail = "dqm@srv-C2D05-19.cms"
EXEDIR = '/nfshome0/dqmpro/filecollector' # directory to execute the relevant scripts
TRANSFER_HOSTNAME = "srv-C2D05-19"
TRANSFER_CONFIGFILE = "/nfshome0/dqm/.transfer/myconfig.txt"
INJECTIONSCRIPT = "/nfshome0/tier0/scripts/injectFileIntoTransferSystem.pl"
DEBUG=False

################################
#Waiting Times:                # 
################################
COLLECTOR_WAIT_TIME      = 10       # waiting time for new files (sec)
MERGER_WAIT_TIME         = 50        # waiting time for new files (sec)
REGISTER_WAIT_TIME       = 120
TRANSFERRER_WAIT_TIME    = 60
VERIFY_WAIT_TIME         = 600
IG_PACKER_WAIT_TIME      = 120       # waiting time for new files (sec)
PROD_CLEANNER_WAIT_TIME  = 3600*4
FILER_CLEANNER_WAIT_TIME = 3600*24
CLASSIFIER_WAIT_TIME	   = 120

################################
#Directories:                  # 
################################
 
COLLECTING_DIR         = '/home/dqmprolocal/output'  #directory to search recently produced files
DONE_DIR               = '/dqmdata/EventDisplay/.done' 	
DROPBOX                = '/dqmdata/dqm/dropbox' # directory, to which files are stored
FILER_MERGED_DIR       = '/dqmdata/dqm/merged' # directory, to backup merged files
IG_FILE_DROPBOX        = '/dqmdata/EventDisplay/dropbox' #Directory to store ig Files.
INDEX                  = '/home/dqm/idx'
INJECTION_DIR          = '/dqmdata/EventDisplay/Tier0Shipping/inject'   #Directory where files get placed once they have been sent.
JUNK_DIR               = '/dqmdata/dqm/junk'
MERGED_DIR             = '/data/dqm/merged' # directory, to which merged file are stored
OLD_IG_FILES           = '/dqmdata/EventDisplay/done'
BASE_DIRECTORY	       = "/dqmdata/EventDisplay/done"
REGISTERED_DIR         = '/dqmdata/EventDisplay/dropbox'     # 'Directory that stores registered files
SOURCES_DONE_DIR       = '/dqmdata/dqm/done/sources' # directory, to which processed files are stored
T_FILE_DONE_DIR        = '/home/dqmprolocal/done' # directory to store *_T files once they have been processed
TMP_DROPBOX            = '/dqmdata/dqm/.dropbox_tmp' # stealth area on cmsmon
VERIFY_DIR             = '/dqmdata/EventDisplay/Tier0Shipping/verify'
CLEAN_DIR              = BASE_DIRECTORY
################################
#ratsControl parameters:       # 
################################
#The following are the available modules defined in the ratsControl script
#Notice how they are the keys for the association
#MODULES=["Collector","Merger","Register","Transfer","Verify","All"]

RATS={"Transfer":{
	"hosts":["srv-c2d05-19"],
	"alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
	"script":"fileTransfer.py"
	},
      "Verify":{
	"hosts":["srv-c2d05-19"],
	"alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
	"script":"fileTransferVerify.py"
	},
      "Classifier":{
	"hosts":["srv-c2d05-11"],
	"alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
	"script":"fileClassifier"
	},  
      "FilerClean":{
  "hosts":["srv-c2c05-11"],
  "alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
  "script":"filerCleanner.py"
  }	
}

################################
#App Spesific parameters:      # 
################################
#fileCollector:                
RETRIES = 3

#fileMerger:                 
MAX_TOTAL_RUNS = 400
MAX_RUNS = 10

#fileRegister:                 
MAX_FILES = 10	 	  		# Max number of files to process at once

#fileTransfer:
EMPTY_DONEDIR = False

#fileTransferVerify:
STAGES=["st1","st2","st3","Error"]
EMPTY_DONEDIR = False

#igTier0FilePacker:
CLEANUP = False
MAX_ZIP_SIZE = 1610612736 # 1.5GB/70%   as max filesize.
COMPRESSION = 1 #Compression rate for zip file 1(min) - 9(max)

#Common Parameters for fileTransferVerify and fileTransfer
TEST=False

#producerFileCleaner:
PRODUCER_DU_TOP=90.0  #0% a 100%
PRODUCER_DU_BOT=50.0  

#fileClassifier
FILE_NAME_STD	= "iSpy_([_A-Z0-9]*)__([-_a-zA-Z0-9]*)__R([0-9]{9,9})_T([0-9]{8,8}).ig"
ERAS					= ["CRAFT","CRUZET","MWGR","BEAM"]

#filerCleaner:
FILER_DU_TOP           = 90.0  #0% a 100% porcentage of disk utilization (DU) when DU > FILER_DU_TOP files will be deleted until  
FILER_DU_BOT           = 50.0  #          DU = FILER_DU_BOT, or as close as it can get to it
FILER_SQ_TOP           = 20*pow(1024,3)   # size in bytes. when Directory size (DS) > FILER_SQ_TOP files will be deleted until
FILER_SQ_BOT           = 10*pow(1024,3)   # DS = FILER_SQ_BOT, or as close as it can get to it
FILER_NRUNS            = 5     #keeps latest FILER_NRUNS runs also sets the minimum number of runs to keep when mode is Time
FILER_TIME             = 3      #keeps files produced with in the last FILER_TIME hours
MODE                   = "Time"  #possibilities: "%DiskUse","Size","NumberOfRuns","Time"
