import FWCore.ParameterSet.Config as cms

process = cms.Process("SiStrpDQMLive")

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siStripDigis', 
                                         'siStripClusters', 
                                         'siStripZeroSuppression', 
                                        'SiStripClusterizer'),
    cout = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
    destinations = cms.untracked.vstring('cout')
)

#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'SiStrip DQM Consumer'
#process.EventStreamHttpReader.sourceURL = cms.string('http://dqm-c2d07-30.cms:22100/urn:xdaq-application:lid=30')

#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/sistrip_reference.root'
process.DQM.filter = '^(SiStrip|Tracking)(/[^/]+){0,5}$'

process.load("DQMServices.Components.DQMEnvironment_cfi")

#----------------------------
# DQM Live Environment
#-----------------------------
#from DQM.Integration.test.environment_cfi import HEAVYION

process.load("DQM.Integration.test.environment_cfi")


process.dqmEnv.subSystemFolder    = "SiStrip"
process.dqmSaver.producer = "Playback"
process.dqmSaver.saveByTime = 60
process.dqmSaver.saveByMinute = 60

process.dqmEnvTr = cms.EDAnalyzer("DQMEventInfo",
                 subSystemFolder = cms.untracked.string('Tracking'),
                 eventRateWindow = cms.untracked.double(0.5),
                 eventInfoFolder = cms.untracked.string('EventInfo')
)

#-----------------------------
# Magnetic Field
#-----------------------------
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

#-------------------------------------------------
# GEOMETRY
#-------------------------------------------------
process.load("Configuration.StandardSequences.Geometry_cff")

#--------------------------
# Calibration
#--------------------------
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
#--------------------------------------------
## Patch to avoid using Run Info information in reconstruction
#
process.siStripQualityESProducer.ListOfRecordToMerge = cms.VPSet(
   cms.PSet( record = cms.string("SiStripDetVOffRcd"),    tag    = cms.string("") ),
   cms.PSet( record = cms.string("SiStripDetCablingRcd"), tag    = cms.string("") ),
#  cms.PSet( record = cms.string("RunInfoRcd"),           tag    = cms.string("") ),
   cms.PSet( record = cms.string("SiStripBadChannelRcd"), tag    = cms.string("") ),
   cms.PSet( record = cms.string("SiStripBadFiberRcd"),   tag    = cms.string("") ),
   cms.PSet( record = cms.string("SiStripBadModuleRcd"),  tag    = cms.string("") )
   )
#-------------------------------------------
                                                                                           
#-----------------------
#  Reconstruction Modules
#-----------------------
## Collision Reconstruction
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
#process.siStripDigis.UnpackBadChannels = cms.bool(True)
process.load("Configuration.StandardSequences.Reconstruction_cff")
#process.load("Configuration.GlobalRuns.reco_TLR_42X")

## Cosmic Track Reconstruction
if (process.runType.getRunType() == process.runType.cosmic_run):
    process.load("RecoTracker.Configuration.RecoTrackerP5_cff")

# offline beam spot
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

#--------------------------
# Strip DQM Source and Client
#--------------------------
process.load("DQM.SiStripMonitorClient.SiStripSourceConfigP5_cff")
process.TrackMon_gentk.doLumiAnalysis = False
process.TrackMon_ckf.doLumiAnalysis = False

#--------------------------
# Quality Test
#--------------------------
process.qTester = cms.EDAnalyzer("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/SiStripMonitorClient/data/sistrip_qualitytest_config.xml'),
    prescaleFactor = cms.untracked.int32(3),                               
    getQualityTestsFromFile = cms.untracked.bool(True),
    qtestOnEndLumi = cms.untracked.bool(True),
    qtestOnEndRun = cms.untracked.bool(True)
)

#--------------------------
# Web Service
#--------------------------
process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")

process.AdaptorConfig = cms.Service("AdaptorConfig")

# Simple filter for event
process.eventFilter = cms.EDFilter("SimpleEventFilter",
                   EventsToSkip = cms.untracked.int32(5)
)

#--------------------------
# Producers
#--------------------------
# Event History Producer
process.load("DPGAnalysis.SiStripTools.eventwithhistoryproducerfroml1abc_cfi")

# APV Phase Producer
process.load("DPGAnalysis.SiStripTools.apvcyclephaseproducerfroml1ts2011_cfi")

#--------------------------
# Filters
#--------------------------
# HLT Filter
process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1

# L1 Trigger Bit Selection (bit 40 and 41 for BSC trigger)
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff')
process.load('HLTrigger/HLTfilters/hltLevel1GTSeed_cfi')
process.hltLevel1GTSeed.L1TechTriggerSeeding = cms.bool(True)
process.hltLevel1GTSeed.L1SeedsLogicalExpression = cms.string('NOT (36 OR 37 OR 38 OR 39)')

#--------------------------
# Scheduling
#--------------------------
process.SiStripSources_LocalReco = cms.Sequence(process.siStripFEDMonitor*process.SiStripMonitorDigi*process.SiStripMonitorClusterReal)
process.DQMCommon                = cms.Sequence(process.qTester*process.dqmEnv*process.dqmEnvTr*process.dqmSaver)
process.RecoForDQM_LocalReco     = cms.Sequence(process.siPixelDigis*process.siStripDigis*process.gtDigis*process.trackerlocalreco)

if (process.runType.getRunType() == process.runType.cosmic_run):
    # event selection for cosmic data
    process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_*Cosmic*','HLT_L1*'))
    # Source and Client config for cosmic data
    process.SiStripSources_TrkReco_cosmic = cms.Sequence(process.SiStripMonitorTrack_ckf*process.MonitorTrackResiduals_ckf*process.TrackMon_ckf)
    process.load("DQM.SiStripMonitorClient.SiStripClientConfigP5_Cosmic_cff")
    process.SiStripAnalyserCosmic.TkMapCreationFrequency  = -1
    process.SiStripAnalyserCosmic.ShiftReportFrequency = -1
    process.SiStripAnalyserCosmic.StaticUpdateFrequency = 5
    process.SiStripClients           = cms.Sequence(process.SiStripAnalyserCosmic)
    # Reco for cosmic data
    process.RecoForDQM_TrkReco_cosmic = cms.Sequence(process.offlineBeamSpot*process.ctftracksP5)

    process.qTester = cms.EDAnalyzer("QualityTester",
                                     qtList = cms.untracked.FileInPath('DQM/SiStripMonitorClient/data/sistrip_qualitytest_config_cosmic.xml'),
                                     prescaleFactor = cms.untracked.int32(2),
                                     getQualityTestsFromFile = cms.untracked.bool(True),
                                     qtestOnEndLumi = cms.untracked.bool(True),
                                     qtestOnEndRun = cms.untracked.bool(True)
                                     )

    process.p = cms.Path(process.scalersRawToDigi*
                         process.APVPhases*
                         process.consecutiveHEs*
                         process.hltTriggerTypeFilter*
                         process.RecoForDQM_LocalReco*
                         process.DQMCommon*
                         process.SiStripClients*
                         process.SiStripSources_LocalReco*
                         process.RecoForDQM_TrkReco_cosmic*
                         process.SiStripSources_TrkReco_cosmic
                         )



else : #if (process.runType.getRunType() == process.runType.pp_run):
    #event selection for pp collisions
    process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_L1*','HLT_Jet*','HLT_HT*','HLT_MinBias_*','HLT_Physics*', 'HLT_ZeroBias*'))
    # Source and Client config for pp collisions
    process.SiStripSources_TrkReco   = cms.Sequence(process.SiStripMonitorTrack_gentk*process.MonitorTrackResiduals_gentk*process.TrackMon_gentk)
    process.load("DQM.SiStripMonitorClient.SiStripClientConfigP5_cff")
    process.SiStripAnalyser.TkMapCreationFrequency  = -1
    process.SiStripAnalyser.ShiftReportFrequency = -1
    process.SiStripAnalyser.StaticUpdateFrequency = 5
    process.SiStripClients           = cms.Sequence(process.SiStripAnalyser)
    # Reco for pp collisions
    process.RecoForDQM_TrkReco       = cms.Sequence(process.offlineBeamSpot*process.recopixelvertexing*process.ckftracks)

    process.p = cms.Path(process.scalersRawToDigi*
                         process.APVPhases*
                         process.consecutiveHEs*
                         process.hltTriggerTypeFilter*
                         process.RecoForDQM_LocalReco*
                         process.DQMCommon*
                         process.SiStripClients*
                         process.SiStripSources_LocalReco*
                         process.RecoForDQM_TrkReco*
                         process.SiStripSources_TrkReco
                         )
#--------------------------------------------------
# For high PU run - no tracking in cmssw42x
#--------------------------------------------------
if (process.runType.getRunType() == process.runType.hpu_run):
    process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_600Tower*','HLT_L1*','HLT_Jet*','HLT_HT*','HLT_MinBias_*','HLT_Physics*', 'HLT_ZeroBias*'))
    process.p = cms.Path(process.scalersRawToDigi*
                         process.APVPhases*
                         process.consecutiveHEs*
                         process.hltTriggerTypeFilter*
                         process.RecoForDQM_LocalReco*
                         process.DQMCommon*
                         process.SiStripClients*
                         process.SiStripSources_LocalReco
                         )


#--------------------------------------------------
# Heavy Ion Specific Fed Raw Data Collection Label
#--------------------------------------------------

print "Running with run type = ", process.runType.getRunType()

if (process.runType.getRunType() == process.runType.hi_run):
    process.castorDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.csctfDigis.producer = cms.InputTag("rawDataRepacker")
    process.dttfDigis.DTTF_FED_Source = cms.InputTag("rawDataRepacker")
    process.ecalDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.ecalPreshowerDigis.sourceTag = cms.InputTag("rawDataRepacker")
    process.gctDigis.inputLabel = cms.InputTag("rawDataRepacker")
    process.gtDigis.DaqGtInputTag = cms.InputTag("rawDataRepacker")
    process.gtEvmDigis.EvmGtInputTag = cms.InputTag("rawDataRepacker")
    process.hcalDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.muonCSCDigis.InputObjects = cms.InputTag("rawDataRepacker")
    process.muonDTDigis.inputLabel = cms.InputTag("rawDataRepacker")
    process.muonRPCDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.scalersRawToDigi.scalersInputTag = cms.InputTag("rawDataRepacker")
    process.siPixelDigis.InputLabel = cms.InputTag("rawDataRepacker")
    process.siStripDigis.ProductLabel = cms.InputTag("rawDataRepacker")
    process.SiStripAnalyser.RawDataTag = cms.untracked.InputTag("rawDataRepacker")
    process.siStripFEDMonitor.RawDataTag = cms.untracked.InputTag("rawDataRepacker")
