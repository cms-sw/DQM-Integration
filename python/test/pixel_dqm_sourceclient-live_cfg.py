import FWCore.ParameterSet.Config as cms

process = cms.Process("PIXELDQMLIVE")

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelDigis', 
                                         #'siPixelClusters', 
                                         'SiPixelRawDataErrorSource', 
                                         'SiPixelDigiSource', 
                                         #'SiPixelClusterSource',
					 'sipixelEDAClient'),
    cout = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
    destinations = cms.untracked.vstring('cout')
)

#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'Pixel DQM Consumer'
process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_HI*'))
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_HICentralityVeto','HLT_HIJet35U_Core','HLT_HIL1DoubleMuOpen_Core','HLT_HIMinBiasBSC_Core','HLT_HIPhoton15_Core'))

#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
#process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/pixel_reference.root'

process.load("DQMServices.Components.DQMEnvironment_cfi")

#----------------------------
# DQM Live Environment
#-----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder    = "Pixel"

#-----------------------------
# Magnetic Field
#-----------------------------
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

#-------------------------------------------------
# GEOMETRY
#-------------------------------------------------
process.load("Configuration.StandardSequences.Geometry_cff")

#-------------------------------------------------
# GLOBALTAG
#-------------------------------------------------
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

#-----------------------
#  Reconstruction Modules
#-----------------------
process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
process.siPixelDigis.InputLabel = 'source'
process.siPixelDigis.IncludeErrors = True
process.load("RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi")

#--------------------------
# Pixel DQM Source and Client
#--------------------------
process.load("DQM.SiPixelCommon.SiPixelP5DQM_source_cff")
process.SiPixelDigiSource.layOn = True
process.SiPixelDigiSource.diskOn = True
process.load("DQM.SiPixelCommon.SiPixelP5DQM_client_cff")

process.qTester = cms.EDAnalyzer("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/SiPixelMonitorClient/test/sipixel_tier0_qualitytest_heavyions.xml'),
    prescaleFactor = cms.untracked.int32(1),
    getQualityTestsFromFile = cms.untracked.bool(True),
    verboseQT = cms.untracked.bool(False),
    qtestOnEndLumi = cms.untracked.bool(True),
    qtestOnEndRun = cms.untracked.bool(True)
)

#--------------------------
# Web Service
#--------------------------
process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")
process.AdaptorConfig = cms.Service("AdaptorConfig")

#--------------------------
# Filters
#--------------------------
# HLT Filter
process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1
#--------------------------
# Scheduling
#--------------------------
process.Reco = cms.Sequence(process.siPixelDigis*process.siPixelClusters)
process.DQMmodules = cms.Sequence(process.dqmEnv*process.qTester*process.dqmSaver)

process.p = cms.Path(process.Reco*process.DQMmodules*process.SiPixelRawDataErrorSource*process.SiPixelDigiSource*process.SiPixelClusterSource*process.PixelP5DQMClientWithDataCertification)
####process.p = cms.Path(process.hltTriggerTypeFilter*process.Reco*process.DQMmodules*process.SiPixelRawDataErrorSource*process.SiPixelDigiSource*process.SiPixelClusterSource*process.PixelP5DQMClientWithDataCertification)
