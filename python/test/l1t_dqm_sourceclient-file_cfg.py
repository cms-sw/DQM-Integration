import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("DQMServices.Core.DQM_cfg")

process.load("CondCore.DBCommon.CondDBSetup_cfi")

process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.RPCGeometry.rpcGeometry_cfi")

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.load("DQM.L1TMonitor.L1TMonitor_cff")

process.load("DQM.L1TMonitorClient.L1TMonitorClient_cff")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('file:/data1/lookarea/GlobalAug07.00017220.0001.A.storageManager.0.0000.dat')
)

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
process.DQM.collectorHost = 'srv-c2d05-19'
process.dqmSaver.convention = 'Online'
process.dqmSaver.dirName = '.'
process.dqmSaver.producer = 'DQM'
process.dqmEnv.subSystemFolder = 'L1T'
process.dqmSaver.saveByRun = 1
process.dqmSaver.saveAtJobEnd = True

