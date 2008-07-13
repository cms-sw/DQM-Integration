import FWCore.ParameterSet.Config as cms

process = cms.Process("DTDQM")
process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("EventFilter.DTTFRawToDigi.dttfunpacker_cfi")

process.load("DQM.Integration.test.dtReco_cff")

process.load("DQM.DTMonitorModule.dtDataIntegrityTask_cfi")

process.load("DQM.DTMonitorClient.dtDataIntegrityTest_cfi")

process.load("DQM.DTMonitorModule.dtDigiTask_cfi")

process.load("DQM.DTMonitorClient.dtOccupancyTest_cfi")

process.load("DQM.DTMonitorModule.dtTriggerTask_cfi")

process.load("DQM.DTMonitorClient.dtLocalTriggerTest_cfi")

process.load("DQM.DTMonitorModule.dtSegmentTask_cfi")

process.load("DQM.DTMonitorClient.dtSegmentAnalysisTest_cfi")

process.load("DQM.DTMonitorClient.dtSummaryClients_cfi")

process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('file:/data1/lookarea/GlobalAug07.00017220.0001.A.storageManager.0.0000.dat')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING')
    ),
    destinations = cms.untracked.vstring('cout')
)

process.dtqTester = cms.EDFilter("QualityTester",
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/DTMonitorClient/test/QualityTests.xml')
)

process.dqmmodules = cms.Sequence(process.dqmEnv+process.dqmSaver)
process.reco = cms.Sequence(process.dtunpacker+process.dttfunpacker+process.dt1DRecHits+process.dt4DSegments)
process.dtDQMTask = cms.Sequence(process.dtDigiMonitor+process.dtTriggerMonitor)
process.dtDQMTest = cms.Sequence(process.dataIntegrityTest+process.triggerTest+process.dtOccupancyTest+process.dtSegmentAnalysisMonitor+process.dtSummaryClients+process.dtqTester)
process.dtDQMPath = cms.Path(process.dqmmodules+process.reco+process.dtDQMTask+process.segmentTest+process.dtDQMTest)
process.DQM.collectorHost = 'srv-c2d05-16'
process.DQM.collectorPort = 9090
process.dqmSaver.convention = 'Online'
process.dqmSaver.dirName = '/cms/mon/data/dropbox'
process.dqmSaver.producer = 'Playback'
process.dqmEnv.subSystemFolder = 'DT'
process.dqmSaver.saveByRun = 1
process.dqmSaver.saveAtJobEnd = True
process.DTLinearDriftAlgo_CosmicData.recAlgoConfig.tTrigModeConfig.kFactor = -0.7
process.dtTriggerMonitor.process_dcc = True
process.dtTriggerMonitor.dcc_label = 'dttfunpacker'

