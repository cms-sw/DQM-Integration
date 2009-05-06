import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("DQM.Integration.test.inputsource_playback_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_playback_cfi")
process.DQMStore.referenceFileName = '/home/dqmdevlocal/reference/hlt_reference.root'

process.load("Configuration.StandardSequences.GeometryPilot2_cff")
process.load("Configuration.StandardSequences.MagneticField_cff") # for muon hlt dqm
process.GlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" ) # for muon hlt dqm
process.load("DQM.HLTEvF.HLTMonitor_cff")
process.load("DQM.HLTEvF.HLTMonitorClient_cff")

process.pp = cms.Path(process.dqmEnv+process.dqmSaver)
process.EventStreamHttpReader.consumerName = 'HLT DQM Consumer'
process.dqmEnv.subSystemFolder = 'HLT'
#process.hltResults.plotAll = True

