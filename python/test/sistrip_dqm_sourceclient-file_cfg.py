import FWCore.ParameterSet.Config as cms

process = cms.Process("SiStrpDQMFire")

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
process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring('file:/home/dqmdevlocal/input/02D59D05-4151-DD11-9E79-001617DBD5AC.root')
)
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(50))

#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.DQMStore.referenceFileName = '/home/dqmdevlocal/reference/sistrip_reference.root'
process.DQM.filter = '^SiStrip(/[^/]+){0,5}$'

process.load("DQMServices.Components.DQMEnvironment_cfi")

#----------------------------
# DQM Playback Environment
#-----------------------------
process.load("DQM.Integration.test.environment_playback_cfi")
process.dqmEnv.subSystemFolder    = "SiStrip"

#-----------------------------
# Magnetic Field
#-----------------------------
process.load("Configuration.GlobalRuns.ForceZeroTeslaField_cff")

#-------------------------------------------------
# GEOMETRY
#-------------------------------------------------
process.load("Configuration.StandardSequences.Geometry_cff")

#--------------------------
# Calibration
#--------------------------
import CalibTracker.Configuration.Common.PoolDBESSource_cfi
process.siStripCond = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone()
process.siStripCond.toGet = cms.VPSet(
    cms.PSet(record = cms.string('SiStripPedestalsRcd'), tag = cms.string('SiStripPedestals_TKCC_21X_v3_hlt')), 
    cms.PSet(record = cms.string('SiStripNoisesRcd'),    tag = cms.string('SiStripNoise_TKCC_21X_v3_hlt')),
    cms.PSet(record = cms.string('SiStripBadChannelRcd'),tag = cms.string('SiStripBadChannel_TKCC_21X_v3_hlt')),
    cms.PSet(record = cms.string('SiStripFedCablingRcd'),tag = cms.string('SiStripFedCabling_TKCC_21X_v3_hlt'))
 )
process.siStripCond.connect = 'oracle://cms_orcon_prod/CMS_COND_21X_STRIP'
process.siStripCond.DBParameters.authenticationPath = '/nfshome0/xiezhen/conddb'

process.sistripconn = cms.ESProducer("SiStripConnectivity")

process.load("CalibTracker.SiStripESProducers.SiStripQualityESProducer_cfi")
process.SiStripQualityESProducer.ListOfRecordToMerge = cms.VPSet(
    cms.PSet(record = cms.string('SiStripDetCablingRcd'), tag = cms.string('')), 
    cms.PSet(record = cms.string('SiStripBadChannelRcd'), tag = cms.string(''))
 )

process.load("CalibTracker.Configuration.SiStripGain.SiStripGain_Fake_cff")

process.load("CalibTracker.Configuration.SiStripLorentzAngle.SiStripLorentzAngle_Fake_cff")

process.load("CalibTracker.Configuration.SiPixelLorentzAngle.SiPixelLorentzAngle_Fake_cff")

process.load("CalibTracker.Configuration.TrackerAlignment.TrackerAlignment_Fake_cff")

#If Frontier is used in xdaq environment use the following service
#    service = SiteLocalConfigService {}

#-----------------------
#  Reconstruction Modules
#-----------------------
# Real data raw to digi
process.load("EventFilter.SiStripRawToDigi.SiStripDigis_cfi")
process.siStripDigis.ProductLabel = 'source'

# Local and Track Reconstruction
process.load("RecoLocalTracker.Configuration.RecoLocalTracker_Cosmics_cff")
process.load("RecoTracker.Configuration.RecoTrackerP5_cff")
process.CTF_P5_MeasurementTracker.pixelClusterProducer = ''
process.RS_P5_MeasurementTracker.pixelClusterProducer = ''
# offline beam spot
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

#--------------------------
# Strip DQM Source and Client
#--------------------------
process.load("DQM.SiStripMonitorClient.SiStripSourceConfigP5_cff")

process.SiStripClient = cms.EDFilter("SiStripAnalyser",
    StaticUpdateFrequency = cms.untracked.int32(-1),
    TkMapCreationFrequency = cms.untracked.int32(-1),
    SummaryCreationFrequency = cms.untracked.int32(1),
    GlobalStatusFilling = cms.untracked.bool(True),                                     
    TkmapParameters = cms.PSet(
        loadFedCabling = cms.untracked.bool(True),
        trackerdatPath = cms.untracked.string('CommonTools/TrackerMap/data/'),
        trackermaptxtPath = cms.untracked.string('DQM/Integration/test/TkMap/')
    )
)

#--------------------------
# STRIP DQM Source and Client
#--------------------------
process.qTester = cms.EDFilter("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/SiStripMonitorClient/data/sistrip_qualitytest_config.xml'),
    prescaleFactor = cms.untracked.int32(1),                               
    getQualityTestsFromFile = cms.untracked.bool(True)
)

#--------------------------
# Web Service
#--------------------------
process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")

process.AdaptorConfig = cms.Service("AdaptorConfig")

#--------------------------
# Scheduling
#--------------------------
process.SiStripSources = cms.Sequence(process.HardwareMonitor*process.CondDataMonitoring*process.SiStripMonitorDigi*process.SiStripMonitorClusterReal*process.SiStripMonitorTrack_ckf*process.MonitorTrackResiduals_ckf*process.TrackMon_ckf)
process.DQMCommon = cms.Sequence(process.qTester*process.dqmEnv*process.dqmSaver)
process.RecoForDQM = cms.Sequence(process.siStripDigis*process.offlineBeamSpot*process.striptrackerlocalreco*process.ctftracksP5)
process.p = cms.Path(process.RecoForDQM*process.DQMCommon*process.SiStripSources*process.SiStripClient)

