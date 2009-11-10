import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("DQM.Integration.test.inputsource_cfi")
#process.EventStreamHttpReader.sourceURL = cms.string('http://srv-c2c05-06:22100/urn:xdaq-application:lid=30')
process.EventStreamHttpReader.SelectHLTOutput = cms.untracked.string('hltOutputHLTDQM')

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_cfi")

process.load("Configuration.StandardSequences.GeometryPilot2_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.GlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" ) # for muon hlt dqm
#SiStrip Local Reco
process.SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")
process.TkDetMap = cms.Service("TkDetMap")

process.load( "Configuration.StandardSequences.FrontierConditions_GlobalTag_cff" )
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = "GR09_H_V3::All"


process.load("DQM.HLTEvF.HLTMonitor_cff")
process.load("DQM.HLTEvF.HLTMonitorClient_cff")
process.load("DQM.TrigXMonitor.HLTScalers_cfi")
process.load("DQM.TrigXMonitorClient.HLTScalersClient_cfi")
process.hlts.l1GtData = cms.InputTag("l1GtUnpack","","DQM")
process.hlts.dqmFolder = cms.untracked.string("HLT/HLTScalers_SM")
process.hltsClient.dqmFolder = cms.untracked.string("HLT/HLTScalers_SM")
process.p = cms.EndPath(process.hlts+process.hltsClient)


process.pp = cms.Path(process.dqmEnv+process.dqmSaver)
process.EventStreamHttpReader.consumerName = 'HLT DQM Consumer'
process.dqmEnv.subSystemFolder = 'HLT'
#process.hltResults.plotAll = True

