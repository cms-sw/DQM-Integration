import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.SelectHLTOutput = cms.untracked.string('hltOutputHLTDQM')

process.load("DQMServices.Core.DQM_cfg")
process.DQMStore.referenceFileName = "/dqmdata/dqm/reference/hlt_reference.root"

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_cfi")

process.load("Configuration.StandardSequences.GeometryPilot2_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.GlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" ) # for muon hlt dqm
#SiStrip Local Reco
process.SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")
process.TkDetMap = cms.Service("TkDetMap")

#---- for P5 (online) DB access
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

process.load("DQM.HLTEvF.HLTMonitor_cff")
process.load("DQM.HLTEvF.HLTMonitorClient_cff")
process.load("DQM.TrigXMonitor.HLTScalers_cfi")
process.load("DQM.TrigXMonitorClient.HLTScalersClient_cfi")
process.hlts.l1GtData = cms.InputTag("l1GtUnpack","","DQM")
process.hlts.dqmFolder = cms.untracked.string("HLT/HLTScalers_SM")
process.hltsClient.dqmFolder = cms.untracked.string("HLT/HLTScalers_SM")
process.p = cms.EndPath(process.hlts+process.hltsClient+process.dqmEnv+process.dqmSaver)


#process.pp = cms.Path(process.dqmEnv+process.dqmSaver)
process.EventStreamHttpReader.consumerName = 'HLT DQM Consumer'
process.dqmEnv.subSystemFolder = 'HLT'
#process.hltResults.plotAll = True

