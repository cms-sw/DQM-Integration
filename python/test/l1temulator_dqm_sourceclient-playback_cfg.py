import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TEmuDQMpback")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("DQM.Integration.test.inputsource_playback_cfi")
process.load("DQM.Integration.test.environment_playback_cfi")

process.load("DQM.L1TMonitor.L1TEmulatorMonitor_cff")    
process.load("DQM.L1TMonitorClient.L1TEMUMonitorClient_cff")    

#replace DQMStore.referenceFileName = "L1TEMU_reference.root"

process.EventStreamHttpReader.consumerName = 'L1TEMU DQM Consumer'
process.dqmEnv.subSystemFolder = 'L1TEMU'

process.source.sourceURL  = cms.string("http://srv-c2c05-27:50082/urn:xdaq-application:lid=29") 
