import FWCore.ParameterSet.Config as cms

process = cms.Process("DQMLumi")
process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
    destinations = cms.untracked.vstring('cout')
)

#----------------------------
# Event Source
#----------------------------
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = "DQM Luminosity Consumer"

#----------------------------
# DQM Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
### @@@@@@ Un-comment when running locally @@@@@@ ###
process.DQM.collectorHost = ''
### @@@@@@ Un-comment when running locally @@@@@@ ###
##process.dqmEnv.subSystemFolder = "LumiMonitor"
process.dqmSaver.dirName = '.'
#--------------------------
#  Lumi Producer and DB access
#-------------------------
process.DBService=cms.Service('DBService',
                              authPath= cms.untracked.string('/nfshome0/popcondev/conddb')
                              )
process.DIPLumiProducer=cms.ESSource("DIPLumiProducer",
          connect=cms.string('oracle://cms_omds_lb/CMS_RUNTIME_LOGGER')
                            )

#---------------------------------------------
# Global Tag
#---------------------------------------------
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
process.GlobalTag.DBParameters.authenticationPath  = process.DBService.authPath

#---------------------------
# Lumi Monitor
#---------------------------
process.load("DQMServices/Components/DQMLumiMonitor_cfi")
#----------------------------
# Define Sequence
#----------------------------
process.dqmmodules = cms.Sequence(process.dqmEnv
                                  + process.dqmLumiMonitor    
                                  + process.dqmSaver)
#----------------------------
# Proton-Proton Running Stuff
#----------------------------
process.p = cms.Path(process.dqmmodules)

