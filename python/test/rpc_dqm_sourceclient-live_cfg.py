import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")

################# Geometry  ######################
process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.load("CondCore.DBCommon.CondDBSetup_cfi")


################# RPC Unpacker  ######################
process.rpcunpacker = cms.EDFilter("RPCUnpackingModule",
    InputLabel = cms.untracked.InputTag("source")
)

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

################# RPC Rec Hits  ######################
process.load("RecoLocalMuon.RPCRecHit.rpcRecHits_cfi")


################# DQM Cetral Modules ######################
process.load("DQMServices.Core.DQM_cfg")

process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'RPC DQM Consumer'

process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'RPC'

process.load("DQMServices.Components.DQMEnvironment_cfi")

################# DQM Digi Module ######################
process.load("DQM.RPCMonitorDigi.RPCDigiMonitoring_cfi")
process.rpcdigidqm.DigiEventsInterval = 100
process.rpcdigidqm.dqmshifter = True
process.rpcdigidqm.dqmexpert = True
process.rpcdigidqm.dqmsuperexpert = False
process.rpcdigidqm.DigiDQMSaveRootFile = False

################# DQM Client Modules ####################
process.load("DQM.RPCMonitorClient.RPCEventSummary_cfi")
process.rpcEventSummary.EventInfoPath = 'RPC/EventInfo'
process.rpcEventSummary.RPCPrefixDir = 'RPC/RecHits'
process.rpcEventSummary.RPCPrefixDir = 'RPC/RecHits'
process.rpcEventSummary.PrescaleFactor = 10
process.load("DQM.RPCMonitorClient.RPCMon_SS_Dbx_Global_cfi")

################# Quality Tests #########################
process.qTesterRPC = cms.EDFilter("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/RPCMonitorClient/test/RPCQualityTests.xml'),
    prescaleFactor = cms.untracked.int32(10)
)


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


################  Sequences ############################
process.rpcDigi = cms.Sequence(process.rpcunpacker*process.rpcRecHits*process.rpcdigidqm*process.rpcAfterPulse)
process.rpcClient = cms.Sequence(process.qTesterRPC*process.dqmEnv*process.rpcEventSummary*process.dqmSaver)
process.p = cms.Path(process.rpcDigi*process.rpcClient)
process.rpcRecHits.rpcDigiLabel = 'rpcunpacker'





