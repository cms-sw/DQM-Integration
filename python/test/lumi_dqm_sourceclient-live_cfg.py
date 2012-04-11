import FWCore.ParameterSet.Config as cms

process = cms.Process("DQMLumi")
#process.MessageLogger = cms.Service("MessageLogger",
#    debugModules = cms.untracked.vstring('siPixelDigis',
#                                         'siPixelClusters'),
#    cout = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
#    destinations = cms.untracked.vstring('cout')
#)
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

#----------------------------
# Event Source
#----------------------------
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'DQM Luminosity Consumer'
process.EventStreamHttpReader.SelectHLTOutput = cms.untracked.string('hltOutputALCALUMIPIXELS')


#process.source = cms.Source("EmptySource",
#       numberEventsInRun = cms.untracked.uint32(100),
#       firstRun = cms.untracked.uint32(167807),
#       numberEventsInLuminosityBlock = cms.untracked.uint32(1),
#       firstLuminosityBlock = cms.untracked.uint32(10)
#       )
#process.maxEvents = cms.untracked.PSet(
#      input = cms.untracked.int32(-1)
#      )
#process.source= cms.Source("PoolSource",
#        processingMode=cms.untracked.string('RunsAndLumis'),        
#        fileNames=cms.untracked.vstring(
#        'file:/tmp/lumi/009F3522-D604-E111-A08D-003048F1183E.root')
#)
#----------------------------
# DQM Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
### @@@@@@ Un-comment when running locally @@@@@@ ###
process.DQM.collectorHost = 'dqm-integration.cms'
process.DQM.collectorPort = 9090

### @@@@@@ Un-comment when running locally @@@@@@ ###
process.dqmEnv.subSystemFolder = "Info/Lumi"
process.dqmSaver.dirName = '.'
process.dqmSaver.saveByTime = 60
process.dqmSaver.saveByMinute = 60

#---------------------------------------------
# Global Tag
#---------------------------------------------

#--------------------------
#  Lumi Producer and DB access
#-------------------------
process.DBService=cms.Service('DBService',
                              authPath= cms.untracked.string('/nfshome0/popcondev/conddb')
                              )
process.DIPLumiProducer=cms.ESSource("DIPLumiProducer",
          connect=cms.string('oracle://cms_omds_lb/CMS_RUNTIME_LOGGER')
                            )
#---------------------------
#----------------------------
# Sub-system Configuration
#----------------------------
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
process.GlobalTag.DBParameters.authenticationPath  = process.DBService.authPath
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.EndOfProcess_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.siPixelDigis.InputLabel = cms.InputTag("hltFEDSelectorLumiPixels")

process.reconstruction_step = cms.Sequence(
    process.siPixelDigis +
    process.siPixelClusters
)


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
process.p = cms.Path(process.reconstruction_step *
                     process.dqmmodules)

