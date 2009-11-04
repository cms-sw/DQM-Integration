import FWCore.ParameterSet.Config as cms
process = cms.Process("HcalTimingTest")

process.load("DQM.Integration.test.inputsource_cfi")

process.EventStreamHttpReader.consumerName = 'Hcal Timing DQM Consumer'

process.MessageLogger = cms.Service("MessageLogger",
     categories   = cms.untracked.vstring(''),
     destinations = cms.untracked.vstring('cout'),
     debugModules = cms.untracked.vstring('*'),
     cout = cms.untracked.PSet(
         threshold = cms.untracked.string('WARNING'),
         WARNING = cms.untracked.PSet(limit = cms.untracked.int32(0))
     )
)

process.load("EventFilter.HcalRawToDigi.HcalRawToDigi_cfi")

process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("L1Trigger.Configuration.L1DummyConfig_cff")
process.load("EventFilter.L1GlobalTriggerRawToDigi.l1GtUnpack_cfi")
process.l1GtUnpack.DaqGtInputTag = 'source'

process.load("DQM.HcalMonitorModule.HcalTimingModule_cfi")

#-----------------------------
# Hcal Conditions: from Global Conditions Tag 
#-----------------------------

process.load("DQM.Integration.test.FrontierCondition_GT_cfi")


### include to get DQM histogramming services
process.load("DQMServices.Core.DQM_cfg")
### set the verbose
process.DQMStore.verbose = 0
#### BEGIN DQM Online Environment #######################
### replace YourSubsystemName by the name of your source ###
### use it for dqmEnv, dqmSaver
process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_cfi")
### path where to save the output file
#process.dqmSaver.dirName = '.'
### the filename prefix
#process.dqmSaver.producer = 'DQM'
### possible conventions are "Online", "Offline" and "RelVal"
#process.dqmSaver.convention = 'Online'
process.dqmEnv.subSystemFolder = 'HcalTiming'

process.p = cms.Path(process.hcalDigis*process.l1GtUnpack*process.hcalTimingMonitor*process.dqmEnv*process.dqmSaver)


