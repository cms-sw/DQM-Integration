import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TEmuDQMfile")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.L1TMonitor.L1TEmulatorMonitor_cff")    
process.load("DQM.L1TMonitorClient.L1TEMUMonitorClient_cff")    

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",  #"NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('file:/cmsnfshome0/nfshome0/nuno/datafile.root')
)

process.DQMStore.verbose = 0
process.DQM.collectorHost = "srv-c2d05-16"
#process.DQM.collectorPort = 9190
process.DQMStore.referenceFileName = "/cmsnfshome0/nfshome0/nuno/DQM_L1TEMU_Ref.root"


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

