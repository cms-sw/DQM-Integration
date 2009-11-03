import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("DQM.Integration.test.environment_playback_cfi")

process.load("DQM.L1TMonitor.L1TEmulatorMonitor_cff")    
process.load("DQM.L1TMonitorClient.L1TEMUMonitorClient_cff")    

process.load("Configuration.StandardSequences.Geometry_cff")

process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

##  Subsystem masking in summary map (case insensitive)
##  l1t: all, gt, muons, jets, taujets, isoem, nonisoem, met
process.l1temuEventInfoClient.dataMaskedSystems =cms.untracked.vstring("All")
##  emu: all, dttf, dttpg, csctf, csctpg, rpc, gmt, ecal, hcal, rct, gct, glt
#process.l1tEventInfoClient.emulatorMaskedSystems = cms.untracked.vstring("All")
#process.l1temuEventInfoClient.emulatorMaskedSystems = cms.untracked.vstring(")

#from L1Trigger.HardwareValidation.L1HardwareValidation_cff import *
#newHWSequence = cms.Sequence(deEcal+deHcal+deRct+deGct+deDt+deDttf+deCsc+deCsctf+deRpc+deGmt+deGt*l1compare)
#process.globalReplace("L1HardwareValidation", newHWSequence)


#replace DQMStore.referenceFileName = "L1TEMU_reference.root"

process.EventStreamHttpReader.consumerName = 'L1TEMU DQM Consumer'
process.dqmEnv.subSystemFolder = 'L1TEMU'
