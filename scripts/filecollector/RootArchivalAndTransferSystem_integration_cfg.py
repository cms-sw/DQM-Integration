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
TRANSFERRER_WAIT_TIME    = 3600*4
VERIFY_WAIT_TIME         = 600
IG_PACKER_WAIT_TIME      = 120       # waiting time for new files (sec)
PROD_CLEANNER_WAIT_TIME  = 3600*4
FILER_CLEANNER_WAIT_TIME = 3600*24

################################
#Directories:                  # 
################################
COLLECTING_DIR         = '/home/dqmdevlocal/output'  #directory to search reently produced files
DONE_DIR               = '/dqmdata/dqmintegration/done/merged' 		#sys.argv[1] # '/home/dqm/idx'        # DQM GUI server index directory
DROPBOX                = '/dqmdata/dqmintegration/dropbox' # directory, to which files are stored
FILER_MERGED_DIR       = '/dqmdata/dqmintegration/merged' # directory, to backup merged files
IG_FILE_DROPBOX        = '/dqmdata/EventDisplay/dropbox' #Directory to store ig Files.
INDEX                  = '/home/dqm/idx'
INJECTION_DIR          = '/dqmdata/dqmintegration/Tier0Shipping/inject'   #Directory where files get placed once they have been sent.
JUNK_DIR               = '/dqmdata/dqmintegration/junk'
MERGED_DIR             = '/dqmdata/dqmintegration/mergeauthority' # directory, to which merged file are stored
OLD_IG_FILES           = '/dqmdata/EventDisplay'
REGISTERED_DIR         = '/dqmdata/dqmintegration/registered'     # 'Directory that stores registered files
SOURCES_DONE_DIR       = '/dqmdata/dqmintegration/done/sources' # directory, to which processed files are stored
T_FILE_DONE_DIR        = '/home/dqmdevlocal/done' # directory to store *_T files once they have been processed
TMP_DROPBOX            = '/dqmdata/dqmintegration/.dropbox_tmp' # stealth area on cmsmon
VERIFY_DIR             = '/dqmdata/dqmintegration/Tier0Shipping/verify'
CLEAN_DIR              = '/dqmdata/dqmintegration/done'

################################
#ratsControl parameters:       # 
################################
#The following are the available modules defined in the ratsControl script
#Notice how they are the keys for the association
#MODULES=["Collector","Merger","Register","Transfer","Verify","All"]

RATS={"Collector":{
	"hosts":["srv-c2d05-09","srv-c2d05-10","srv-c2d05-11","srv-c2d05-15","srv-c2d05-16","srv-c2d05-17"],
	"alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
	"script":"fileCollector.py"
	},
      "Merger":{
	"hosts":["srv-c2d05-18"],
	"alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
	"script":"fileMerger.py"
	},
      "Register":{
	"hosts":["srv-c2d05-18"],
	"alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
	"script":"fileRegister.py"
	},
      "Transfer":{
	"hosts":["srv-c2d05-18"],
	"alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
	"script":"fileTransfer.py"
	},
      "Verify":{
	"hosts":["srv-c2d05-18"],
	"alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
	"script":"fileTransferVerify.py"
	},  
      "ProdClean":{
  "hosts":["srv-c2d05-09","srv-c2d05-10","srv-c2d05-11","srv-c2d05-15","srv-c2d05-16","srv-c2d05-17"],
  "alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
  "script":"producerFileCleanner.py"
  }  
      "FilerClean":{
  "hosts":["srv-c2c05-11"],
  "alivechk":"/nfshome0/dqmpro/filecollector/aliveCheck.sh",
  "script":"fileCleanner.py"
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
TEST=True

#producerFileCleaner:
PRODUCER_DU_TOP=90.0  #0% a 100%
PRODUCER_DU_BOT=50.0

#fileCleaner:
FILER_DU_TOP           = 90.0  #0% a 100% porcentage of disk utilization (DU) when DU > FILER_DU_TOP files will be deleted until  
FILER_DU_BOT           = 50.0  #          DU = FILER_DU_BOT, or as close as it can get to it
FILER_SQ_TOP           = 20*pow(1024^3)   # size in bytes. when Directory size (DS) > FILER_SQ_TOP files will be deleted until
FILER_SQ_BOT           = 10*pow(1024^3)   # DS = FILER_SQ_BOT, or as close as it can get to it
FILER_NRUNS            = 500     #keeps latest FILER_NRUNS runs also sets the minimum number of runs to keep when mode is time
FILER_TIME             = 24      #keeps files produced with in the last FILER_TIME hours
MODE                   = "Time"  #possibilities: "%DiskUse","Size","NumberOfRuns","Time"
