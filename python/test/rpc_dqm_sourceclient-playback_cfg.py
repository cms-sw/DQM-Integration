import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.RPCGeometry.rpcGeometry_cfi")

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.load("CondCore.DBCommon.CondDBSetup_cfi")

process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")
process.DQMStore.referenceFileName = '/home/dqmdevlocal/reference/rpc_reference.root'

process.load("DQM.Integration.test.environment_playback_cfi")

process.load("DQM.Integration.test.inputsource_playback_cfi")
process.EventStreamHttpReader.consumerName = 'RPC DQM Consumer'

process.load("DQM.RPCMonitorClient.RPCEventSummary_cfi")

process.load("DQM.RPCMonitorDigi.RPCDigiMonitoring_cfi")

process.load("DQM.RPCMonitorClient.RPCMon_SS_Dbx_Global_cfi")


process.RPCCabling = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0),
        authenticationPath = cms.untracked.string('/nfshome0/hltpro/cmssw/cfg/')
    ),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('RPCEMapRcd'),
        tag = cms.string('RPCEMap_v2')
    )),
    connect = cms.string('frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_20X_RPC'),
    siteLocalConfig = cms.untracked.bool(False)
)

process.rpcunpacker = cms.EDFilter("RPCUnpackingModule",
    InputLabel = cms.untracked.InputTag("source"),
    doSynchro = cms.bool(False)
)

process.qTesterRPC = cms.EDFilter("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/RPCMonitorClient/test/RPCQualityTests.xml'),
    QualityTestPrescaler = cms.untracked.int32(10)
)

process.p = cms.Path(process.rpcunpacker*process.rpcRecHits*process.rpcdigidqm*process.rpcAfterPulse*process.qTesterRPC*process.dqmEnv*process.rpcEventSummary*process.dqmSaver)
process.rpcRecHits.rpcDigiLabel = 'rpcunpacker'
process.DQMStore.verbose = 0
process.DQM.collectorHost = 'srv-c2d05-18'
process.dqmEnv.subSystemFolder = 'RPC'
process.rpcdigidqm.DigiEventsInterval = 100
process.rpcdigidqm.dqmshifter = True
process.rpcdigidqm.dqmexpert = True
process.rpcdigidqm.dqmsuperexpert = False
process.rpcdigidqm.DigiDQMSaveRootFile = False
process.rpcEventSummary.EventInfoPath = 'RPC/EventInfo'
process.rpcEventSummary.RPCPrefixDir = 'RPC/RecHits'
process.rpcEventSummary.RPCPrefixDir = 'RPC/RecHits'
process.rpcEventSummary.PrescaleFactor = 10
