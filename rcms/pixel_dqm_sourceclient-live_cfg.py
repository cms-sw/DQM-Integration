import FWCore.ParameterSet.Config as cms

process = cms.Process("PIXELDQMLIVE")

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelDigis', 
                                         'siPixelClusters', 
                                         'SiPixelRawDataErrorSource', 
                                         'SiPixelDigiSource', 
                                         'SiPixelClusterSource',
					 'sipixelEDAClient'),
    cout = cms.untracked.PSet(threshold = cms.untracked.string('ERROR')),
    destinations = cms.untracked.vstring('cout')
)

#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'Pixel DQM Consumer'
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_TrackerCosmics_CTF'))

#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
#process.DQMStore.referenceFileName = '/home/dqmprolocal/reference/pixel_reference.root'

process.load("DQMServices.Components.DQMEnvironment_cfi")

#----------------------------
# DQM Live Environment
#-----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder    = "Pixel"

#-----------------------------
# Magnetic Field
#-----------------------------
# 0T field
#process.load("Configuration.GlobalRuns.ForceZeroTeslaField_cff")
# 3.8T field
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.prefer("VolumeBasedMagneticFieldESProducer")

#-------------------------------------------------
# GEOMETRY
#-------------------------------------------------
process.load("Configuration.StandardSequences.Geometry_cff")

#-------------------------------------------------
# GLOBALTAG
#-------------------------------------------------
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.connect = "sqlite_file:/nfshome0/malgeri/public/globtag/CRZT210_V1H.db"
process.GlobalTag.connect ="frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"
#process.GlobalTag.globaltag = "CRZT210_V1C::All"
#process.GlobalTag.globaltag = "CRZT210_V3H::All"
#process.GlobalTag.globaltag = "CRUZET4_V5H::All"
process.GlobalTag.globaltag = "CRAFT_V3H::All"
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')

#If Frontier is used in xdaq environment use the following service
#    service = SiteLocalConfigService {}

#-----------------------
#  Reconstruction Modules
#-----------------------
# Real data raw to digi
process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
process.siPixelDigis.InputLabel = 'source'
process.siPixelDigis.IncludeErrors = True

# Local Reconstruction
process.load("RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi")

#--------------------------
# Pixel DQM Source and Client
#--------------------------
process.load("DQM.SiPixelMonitorRawData.SiPixelMonitorRawData_cfi")
process.SiPixelRawDataErrorSource.isPIB = False
process.SiPixelRawDataErrorSource.reducedSet = True
process.load("DQM.SiPixelMonitorDigi.SiPixelMonitorDigi_cfi")
process.SiPixelDigiSource.isPIB = False
process.SiPixelDigiSource.hiRes = False
process.load("DQM.SiPixelMonitorCluster.SiPixelMonitorCluster_cfi")
process.SiPixelClusterSource.reducedSet = True


process.sipixelEDAClient = cms.EDFilter("SiPixelEDAClient",
    EventOffsetForInit = cms.untracked.int32(10),
    ActionOnLumiSection = cms.untracked.bool(True),
    ActionOnRunEnd = cms.untracked.bool(True),
    HighResolutionOccupancy = cms.untracked.bool(False),
    NoiseRateCutValue = cms.untracked.double(-1.), #negative value means test is not run; default cut value is 0.001
    NEventsForNoiseCalculation = cms.untracked.int32(100),
    UseOfflineXMLFile = cms.untracked.bool(False)
)

process.qTester = cms.EDFilter("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/SiPixelMonitorClient/test/sipixel_qualitytest_config.xml'),
    QualityTestPrescaler = cms.untracked.int32(1),
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
#process.Reco = cms.Sequence(process.siPixelDigis)
process.Reco = cms.Sequence(process.siPixelDigis*process.siPixelClusters)
process.RAWmonitor = cms.Sequence(process.SiPixelRawDataErrorSource)
process.DIGImonitor = cms.Sequence(process.SiPixelDigiSource)
process.CLUmonitor = cms.Sequence(process.SiPixelClusterSource)
process.DQMmodules = cms.Sequence(process.dqmEnv*process.qTester*process.dqmSaver)
process.p = cms.Path(process.Reco*process.dqmEnv*process.RAWmonitor*process.DIGImonitor*process.CLUmonitor*process.sipixelEDAClient*process.dqmSaver)