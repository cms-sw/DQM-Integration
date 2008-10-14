import FWCore.ParameterSet.Config as cms

process = cms.Process("EvFDQM")

#----------------------------
#### Event Source
#----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'FED DQM Consumer'


#----------------------------
#### DQM Environment
#----------------------------
process.load("DQMServices.Core.DQM_cfg")
#process.DQMStore.referenceFileName = "DT_reference.root"


#----------------------------
#### DQM Live Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'FED'
#-----------------------------


# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
                                    )

# Global tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')
process.GlobalTag.connect ="frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"
process.GlobalTag.globaltag = "CRAFT_V1H::All"


#-----------------------------
#### Sub-system configuration follows

# DT DQM sequence
process.load("DQM.DTMonitorModule.dtDataIntegrityTask_EvF_cff")

# ECAL DQM sequences
import DQM.EcalBarrelMonitorTasks.EBHltTask_cfi
process.ebDQMEvF = DQM.EcalBarrelMonitorTasks.EBHltTask_cfi.ecalBarrelHltTask.clone()
import DQM.EcalEndcapMonitorTasks.EEHltTask_cfi
process.eeDQMEvF = DQM.EcalEndcapMonitorTasks.EEHltTask_cfi.ecalEndcapHltTask.clone()

# DQM Modules
process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)


#-----------------------------
### Define the path
process.evfDQMPath = cms.Path(process.dqmmodules + process.dtDQMEvF + process.ebDQMEvF + process.eeDQMEvF)


