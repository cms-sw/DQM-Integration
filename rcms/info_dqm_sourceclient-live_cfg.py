import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")

#----------------------------
#### Event Source
#----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'Info DQM Consumer'
process.EventStreamHttpReader.maxEventRequestRate = cms.untracked.double(1.0)
#process.EventStreamHttpReader.sourceURL = cms.string('http://srv-c2d05-14:22100/urn:xdaq-application:lid=30')

#----------------------------
#### DQM Environment
#----------------------------
process.load("DQMServices.Core.DQM_cfg")
#process.DQMStore.referenceFileName = "DT_reference.root"

#----------------------------
#### DQM Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'Info'
#-----------------------------
process.load("DQMServices.Components.DQMProvInfo_cfi")

# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
                                    )

# Global tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = 'GR09_H_V4::All' # or any other appropriate
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')

process.load("EventFilter.L1GlobalTriggerRawToDigi.l1GtUnpack_cfi")

process.load("EventFilter.ScalersRawToDigi.ScalersRawToDigi_cfi")

#-----------------------------
#### Sub-system configuration follows
process.dump = cms.EDAnalyzer('EventContentAnalyzer')

# DQM Modules
process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)
process.evfDQMmodulesPath = cms.Path(
                              process.l1GtUnpack*
                              process.scalersRawToDigi*
#			      process.dump*
                              process.dqmProvInfo*
                              process.dqmProvInfo*
                              process.dqmmodules 
)
process.schedule = cms.Schedule(process.evfDQMmodulesPath)
