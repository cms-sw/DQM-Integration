import FWCore.ParameterSet.Config as cms

process = cms.Process("DTDQM")

#----------------------------
#### Event Source
#----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.DQMEventStreamHttpReader.consumerName = 'DT DQM Consumer'

#----------------------------
#### DQM Environment
#----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/dt_reference.root'
#process.DQMStore.referenceFileName = "DT_reference.root"

process.load("DQMServices.Components.DQMEnvironment_cfi")


#----------------------------
#### DQM Live Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'DT'
#process.dqmSaver.dirName = "."
#-----------------------------


# DT reco and DQM sequences
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("DQM.DTMonitorModule.dt_dqm_sourceclient_common_cff")
#---- for P5 (online) DB access
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
#---- for offline DB
#process.GlobalTag.globaltag = "GR09_H_V2::All"

# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
                                    )

process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)

process.dtDQMPathPhys = cms.Path(process.unpackers + process.dqmmodules + process.physicsEventsFilter *  process.dtDQMPhysSequence)

#process.dtDQMPathCalib = cms.Path(process.unpackers + process.dqmmodules + process.calibrationEventsFilter * process.dtDQMCalib)

process.dttfunpacker.DTTF_FED_Source = cms.InputTag("rawDataCollector")
process.dtunpacker.inputLabel = cms.InputTag("rawDataCollector")
process.gtDigis.DaqGtInputTag = cms.InputTag("rawDataCollector")
process.scalersRawToDigi.scalersInputTag = cms.InputTag("rawDataCollector")

print "Running with run type = ", process.runType.getRunType()

#----------------------------
#### pp run settings 
#----------------------------

if (process.runType.getRunType() == process.runType.pp_run):
    process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/dt_reference_pp.root'

    process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(
             SelectEvents = cms.vstring('HLT_Mu*', 
                                        'HLT_DoubleMu*', 
                                        'HLT_L1SingleMu*', 
                                        'HLT_IsoMu*', 
                                        'HLT_Dimuon*', 
                                        'HLT_L2DoubleMu*', 
                                        'HLT_L2Mu*', 
                                        'HLT_L1TrackerCosmics*',
                                        'HLT_PADimuon*',
                                        'HLT_PADoubleMu*',
                                        'HLT_PAL1DoubleMu*',
                                        'HLT_PAL1SingleMu*',
                                        'HLT_PAMu*')
                                      )

#----------------------------
#### cosmic run settings 
#----------------------------

if (process.runType.getRunType() == process.runType.cosmic_run):
    process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/dt_reference_cosmic.root'

    process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(
             SelectEvents = cms.vstring('HLT_L1TrackerCosmics*',
                                        'HLT_L1SingleMuOpen_AntiBPTX*')
                                      )

#----------------------------
#### HI run settings 
#----------------------------

if (process.runType.getRunType() == process.runType.hi_run):
    process.dtunpacker.fedbyType = cms.bool(False)
    process.dttfunpacker.DTTF_FED_Source = cms.InputTag("rawDataRepacker")
    process.dtunpacker.inputLabel = cms.InputTag("rawDataRepacker")
    process.gtDigis.DaqGtInputTag = cms.InputTag("rawDataRepacker")
    process.scalersRawToDigi.scalersInputTag = cms.InputTag("rawDataRepacker")
    
    process.dtDigiMonitor.ResetCycle = cms.untracked.int32(9999)

    process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/dt_reference_hi.root'

    process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(
             SelectEvents = cms.vstring('HLT_Mu*', 
                                        'HLT_DoubleMu*', 
                                        'HLT_L1SingleMu*', 
                                        'HLT_IsoMu*', 
                                        'HLT_Dimuon*', 
                                        'HLT_L2DoubleMu*', 
                                        'HLT_L2Mu*', 
                                        'HLT_L1TrackerCosmics*')
                                      )
