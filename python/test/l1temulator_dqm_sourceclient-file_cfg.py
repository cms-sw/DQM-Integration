import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TEmuDQMfile")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
#process.load("DQM.Integration.test.environment_cfi")

process.load("DQM.L1TMonitor.L1TEmulatorMonitor_cff")    
process.load("DQM.L1TMonitorClient.L1TEMUMonitorClient_cff")    

#include geometry only at top level cfg
process.load("Configuration.StandardSequences.Geometry_cff")

### global tag
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
##online
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')
##off-line (overwite)
process.GlobalTag.connect = "frontier://PromptProd/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = "GR09_P_V2::All"
#process.prefer("GlobalTag")
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')


#from L1Trigger.HardwareValidation.L1HardwareValidation_cff import *
#newHWSequence = cms.Sequence(deEcal+deHcal+deRct+deGct+deDt+deDttf+deCsc+deCsctf+deRpc+deGmt+deGt*l1compare)
#process.globalReplace("L1HardwareValidation", newHWSequence)

##  Subsystem masking in summary map (case insensitive)
##  l1t: all, gt, muons, jets, taujets, isoem, nonisoem, met
process.l1temuEventInfoClient.dataMaskedSystems =cms.untracked.vstring("All")
##  emu: all, dttf, dttpg, csctf, csctpg, rpc, gmt, ecal, hcal, rct, gct, glt
#process.l1tEventInfoClient.emulatorMaskedSystems = cms.untracked.vstring("All")
process.l1temuEventInfoClient.emulatorMaskedSystems = cms.untracked.vstring("dttf", "dttpg", "csctf", "csctpg", "rpc", "ecal", "hcal", "rct", "glt")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.source = cms.Source("PoolSource",
#process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring(
    '/store/data/Commissioning09/Cosmics/RAW/v3/000/118/969/FEA12E2E-EEC5-DE11-8BD0-000423D98C20.root'
    #'file:/lookarea_SM/MWGR_29.00106019.0036.A.storageManager.07.0000.dat'
    )
)

process.DQMStore.verbose = 0
process.DQM.collectorHost = "srv-c2d05-12"
process.DQM.collectorPort = 9190
#process.DQMStore.referenceFileName = "/cmsnfshome0/nfshome0/nuno/DQM_L1TEMU_Ref.root"

process.MessageLogger = cms.Service("MessageLogger",
    detailedInfo = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO')
    ),
    critical = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    ),
    debugModules = cms.untracked.vstring('*'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        WARNING = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noLineBreaks = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('detailedInfo',
        'critical',
        'cout')
)

process.DQMStore.verbose = 0
process.dqmSaver.convention = 'Online'
process.dqmSaver.dirName = '.'
process.dqmSaver.producer = 'DQM'
process.dqmEnv.subSystemFolder = 'L1TEMU'
process.dqmSaver.saveByRun = 1
process.dqmSaver.saveAtJobEnd = True
