import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("DQM.Integration.test.inputsource_playback_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_playback_cfi")

process.load("DQM.CSCMonitorModule.test.csc_dqm_sourceclient_cfi")

process.p = cms.Path(process.dqmClient+process.dqmEnv+process.dqmSaver)
process.EventStreamHttpReader.consumerName = 'CSC DQM Consumer'
process.dqmEnv.subSystemFolder = 'CSC'

