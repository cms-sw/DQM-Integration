import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")

process.load("DQM.Integration.test.inputsource_playback_cfi")
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("DQM.Integration.test.environment_playback_cfi")

process.load("DQM.L1TMonitor.L1TEmulatorMonitor_cff")    
process.load("DQM.L1TMonitorClient.L1TEMUMonitorClient_cff")    
process.l1GtParameters.BstLengthBytes = 52
process.load("Configuration.StandardSequences.Geometry_cff")

#masking sequence: 
process.l1temuEventInfoClient.maskedSystems = [0,1,1,0,0,0, 1,1,1,0,1]

#off-line
#process.GlobalTag.globaltag = 'CRAFT_V2P::All'
#process.GlobalTag.connect = 'frontier://FrontierProd/CMS_COND_21X_GLOBALTAG'
#on-line
#process.GlobalTag.globaltag = 'CRAFT_V2H::All'
#process.GlobalTag.connect = 'frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG'

#replace DQMStore.referenceFileName = "L1TEMU_reference.root"
process.EventStreamHttpReader.consumerName = 'L1TEMU DQM Consumer'
process.dqmEnv.subSystemFolder = 'L1TEMU'
