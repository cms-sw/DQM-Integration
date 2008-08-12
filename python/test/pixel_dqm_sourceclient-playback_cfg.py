import FWCore.ParameterSet.Config as cms

process = cms.Process("SIPIXELDQM")

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
process.load("DQM.Integration.test.inputsource_playback_cfi")
process.EventStreamHttpReader.consumerName = 'Pixel DQM Consumer'

#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.DQMStore.referenceFileName = '/home/dqmdevlocal/reference/pixel_reference.root'

process.load("DQMServices.Components.DQMEnvironment_cfi")

#----------------------------
# DQM Playback Environment
#-----------------------------
process.load("DQM.Integration.test.environment_playback_cfi")
process.dqmEnv.subSystemFolder    = "Pixel"

#-----------------------------
# Magnetic Field
#-----------------------------
process.load("Configuration.GlobalRuns.ForceZeroTeslaField_cff")

#-------------------------------------------------
# GEOMETRY
#-------------------------------------------------
process.load("Configuration.StandardSequences.Geometry_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect ="frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_PIXEL"
process.GlobalTag.globaltag = "CRZT210_V1C::All"
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
process.SiPixelRawDataErrorSource.saveFile = False
process.SiPixelRawDataErrorSource.isPIB = False
process.SiPixelRawDataErrorSource.slowDown = False
process.load("DQM.SiPixelMonitorDigi.SiPixelMonitorDigi_cfi")
process.SiPixelDigiSource.saveFile = False
process.SiPixelDigiSource.isPIB = False
process.SiPixelDigiSource.slowDown = False
process.SiPixelDigiSource.modOn = True
process.SiPixelDigiSource.ladOn = False
process.SiPixelDigiSource.layOn = False
process.SiPixelDigiSource.phiOn = False
process.SiPixelDigiSource.bladeOn = False
process.SiPixelDigiSource.diskOn = False
process.SiPixelDigiSource.ringOn = False
process.load("DQM.SiPixelMonitorCluster.SiPixelMonitorCluster_cfi")
process.SiPixelClusterSource.saveFile = False
process.SiPixelClusterSource.isPIB = False
process.SiPixelClusterSource.slowDown = False
process.SiPixelClusterSource.modOn = True
process.SiPixelClusterSource.ladOn = False
process.SiPixelClusterSource.layOn = False
process.SiPixelClusterSource.phiOn = False
process.SiPixelClusterSource.bladeOn = False
process.SiPixelClusterSource.diskOn = False
process.SiPixelClusterSource.ringOn = False

process.sipixelEDAClient = cms.EDFilter("SiPixelEDAClient",
    FileSaveFrequency = cms.untracked.int32(50),
    StaticUpdateFrequency = cms.untracked.int32(10)
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
process.Reco = cms.Sequence(process.siPixelDigis*process.siPixelClusters)
process.RAWmonitor = cms.Sequence(process.SiPixelRawDataErrorSource)
process.DIGImonitor = cms.Sequence(process.SiPixelDigiSource)
process.CLUmonitor = cms.Sequence(process.SiPixelClusterSource)
process.DQMmodules = cms.Sequence(process.qTester*process.dqmEnv*process.dqmSaver)
process.p = cms.Path(process.Reco*process.DQMmodules*process.RAWmonitor*process.DIGImonitor*process.CLUmonitor*process.sipixelEDAClient)

