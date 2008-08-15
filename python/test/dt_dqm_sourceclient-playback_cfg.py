import FWCore.ParameterSet.Config as cms

process = cms.Process("DTDQM")

#----------------------------
#### Event Source
#----------------------------
process.load("DQM.Integration.test.inputsource_playback_cfi")
process.EventStreamHttpReader.consumerName = 'DT DQM Consumer'


#----------------------------
#### DQM Environment
#----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.DQMStore.referenceFileName = "/home/dqmdevlocal/reference/dt_reference.root"


#----------------------------
#### DQM Playback Environment
#----------------------------
process.load("DQM.Integration.test.environment_playback_cfi")
process.dqmEnv.subSystemFolder = 'DT'
#-----------------------------


# DT reco and DQM sequences
process.load("DQM.Integration.test.dt_dqm_sourceclient_common_cff")

# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
                                    )

process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)

process.dtDQMPath = cms.Path(process.calibrationEventsFilter * process.dqmmodules + process.reco + process.dtDQMTask + process.dtDQMTest)


