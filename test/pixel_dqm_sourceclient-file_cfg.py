import FWCore.ParameterSet.Config as cms

process = cms.Process("SIPIXELDQM")

##----## Geometry and other global parameters:
#process.load("Geometry.TrackerSimData.trackerSimGeometryXML_cfi")
#process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")
#process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
#process.load("Configuration.GlobalRuns.ForceZeroTeslaField_cff")
process.load("CondCore.DBCommon.CondDBSetup_cfi")

##----## Reco:
##process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")

process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
process.siPixelDigis.InputLabel = 'source'
process.siPixelDigis.IncludeErrors = True

#process.load("RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi")

#process.load("RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi")
#process.load("RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff")

#process.load("EventFilter.SiStripRawToDigi.SiStripRawToDigis_standard_cff")
#process.siStripDigis.ProductLabel = 'source'

#process.load("RecoLocalTracker.SiStripClusterizer.SiStripClusterizer_cfi")
#process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitConverter_cfi")
#process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitMatcher_cfi")
#process.load("RecoLocalTracker.SiStripRecHitConverter.StripCPEfromTrackAngle_cfi")
#process.load("RecoLocalTracker.SiStripZeroSuppression.SiStripZeroSuppression_cfi")

#process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
#process.load("RecoPixelVertexing.Configuration.RecoPixelVertexing_cff")
#process.load("RecoTracker.Configuration.RecoTrackerP5_cff")



##----## Central DQM:
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.DQM.collectorHost = ''
process.dqmSaver.convention = 'Online'
process.dqmSaver.producer = 'DQM'
process.dqmEnv.subSystemFolder = 'Pixel'
process.dqmSaver.dirName = '/tmp/merkelp/'
process.dqmSaver.saveByLumiSection = -1
process.dqmSaver.saveByRun = 1
process.dqmSaver.saveAtJobEnd = True
process.qTester = cms.EDFilter("QualityTester",
    qtList = cms.untracked.FileInPath('DQM/SiPixelMonitorClient/test/sipixel_qualitytest_config.xml'),
    QualityTestPrescaler = cms.untracked.int32(1),
    getQualityTestsFromFile = cms.untracked.bool(True),
    verboseQT = cms.untracked.bool(False)
)

##----## Pixel DQM P5/OFFLINE:
#process.load("DQM.SiPixelCommon.SiPixelOfflineDQM_source_cff")
#process.load("DQM.SiPixelCommon.SiPixelOfflineDQM_client_cff")
process.load("DQM.SiPixelCommon.SiPixelP5DQM_source_cff")
process.load("DQM.SiPixelCommon.SiPixelP5DQM_client_cff")
## the following sequences are declared therein:
## siPixelOfflineDQM_source, siPixelOfflineDQM_cosmics_source, siPixelOfflineDQM_source_woTrack
## PixelOfflineDQMClient, PixelOfflineDQMClientWithDataCertification
## siPixelP5DQM_source, siPixelP5DQM_cosmics_source, siPixelP5DQM_source_woTrack
## PixelP5DQMClient, PixelP5DQMClientWithDataCertification



##----## Other stuff:
process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelDigis', 
        'SiPixelRawDataErrorSource', 
        'SiPixelDigiSource', 
        'SiPixelClusterSource', 
        'SiPixelRecHitSource', 
        'sipixelEDAClient'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    ),
    destinations = cms.untracked.vstring('cout')
)
process.AdaptorConfig = cms.Service("AdaptorConfig")
process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")
process.LockService = cms.Service("LockService",
    labels = cms.untracked.vstring('source')
)


##----## Global tag and input data:
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.connect ="sqlite_file:/afs/cern.ch/user/m/malgeri/public/globtag/CRZT210_V1.db"
#process.GlobalTag.connect = "frontier://FrontierProd/CMS_COND_21X_GLOBALTAG"
process.GlobalTag.globaltag = "CRAFT_30X::All"
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')
## this next line is needed for xdaq running outside P5 network:
process.SiteLocalConfigService = cms.Service("SiteLocalConfigService")
process.source = cms.Source("PoolSource",
    debugFlag = cms.untracked.bool(True),
    debugVebosity = cms.untracked.uint32(1),
    #fileNames = cms.untracked.vstring('rfio:/castor/cern.ch/user/c/chiochia/cmssw/Muon_FullValidation_150pre3.root')
    #fileNames = cms.untracked.vstring('rfio:/castor/cern.ch/cms/store/relval/2008/6/6/RelVal-RelValTTbar-1212531852-IDEAL_V1-2nd-02/0000/081018D5-EC33-DD11-A623-000423D6CA42.root')
    fileNames = cms.untracked.vstring(
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/FE3C036B-81AF-DD11-8757-000423D98FBC.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/F2C23817-7BAF-DD11-B975-000423D98FBC.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/E8ACBD46-78AF-DD11-B8DB-000423D944F8.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/E22EB0AB-77AF-DD11-BBB1-000423D6CA02.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/E0B037EE-7DAF-DD11-9D1D-000423D174FE.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/DEBFC79B-7EAF-DD11-AF9D-000423D9989E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/DA079052-7FAF-DD11-BB79-001617C3B5E4.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/D2FC07B7-79AF-DD11-861B-000423D98844.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/C4ECF19A-7EAF-DD11-A3A2-0019DB29C5FC.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/C412B95E-78AF-DD11-843D-000423D996C8.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/C034A46C-7AAF-DD11-B4EF-000423D6B444.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/BCD0C6A5-77AF-DD11-B0F2-000423D94494.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/B4D3677D-7CAF-DD11-A32A-000423D99F3E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/B4B29107-80AF-DD11-BFDD-001617C3B6CE.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/B2718D6D-7AAF-DD11-84D8-000423D6CAF2.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/AEDD2731-7DAF-DD11-BE14-000423D9863C.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/AA638E9E-77AF-DD11-9755-000423D99896.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/A6D449B8-80AF-DD11-B3CD-000423D99A8E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/A234CD3B-7DAF-DD11-BFA7-001617C3B70E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/98F1E8B6-79AF-DD11-998F-000423D98EC4.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/984CF9B4-79AF-DD11-9178-000423D99F3E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/945A746E-81AF-DD11-A571-000423D99F1E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/908E0E4C-7FAF-DD11-8C31-001617DBCF6A.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/8C32D31B-82AF-DD11-88FA-001617C3B78C.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/8A00ADB8-80AF-DD11-B311-001617C3B66C.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/72E4B51E-82AF-DD11-B2D2-001617DBD5AC.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/6E064680-7CAF-DD11-A44A-000423D99614.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/6CF6DD00-80AF-DD11-A8CF-001617DBD332.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/6C641668-81AF-DD11-9DDF-001617DBCF1E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/6A8EDD15-7BAF-DD11-9EC2-000423D9997E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/6698746A-7AAF-DD11-8A69-001617DC1F70.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/64BA0C83-7CAF-DD11-AB92-000423D998BA.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/60165933-7DAF-DD11-8293-001617C3B76E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/50C5876D-7AAF-DD11-BC99-000423D6B48C.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/4A37C504-80AF-DD11-82D8-000423D9870C.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/4803ADE3-76AF-DD11-9E02-000423D985B0.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/4006A970-7AAF-DD11-8F8B-000423D6B5C4.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/3A88B39A-7EAF-DD11-A752-001617C3B5F4.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/3A6C6567-7BAF-DD11-B7B1-000423D985B0.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/34A69819-7BAF-DD11-9FFC-000423D174FE.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/32D44ECD-7BAF-DD11-8F52-000423D94494.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/2E056EB8-80AF-DD11-90B1-001617C3B77C.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/28B22747-78AF-DD11-83BF-001617C3B706.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/2485314E-7FAF-DD11-888E-000423D94A20.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/20D1A92C-77AF-DD11-A0B0-000423D98FBC.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/20A57DB9-79AF-DD11-95AB-000423D99BF2.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/1AEEBAE6-76AF-DD11-B639-000423D98834.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/18875C20-82AF-DD11-BA95-001617E30CA4.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/149A6203-80AF-DD11-B1EB-001617C3B70E.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/14916BEC-7DAF-DD11-9256-000423D98844.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/06FBE585-7CAF-DD11-8BC3-000423D94700.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/062A2888-7CAF-DD11-BB4F-000423D99160.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/060397EE-7DAF-DD11-A075-001617DBD5B2.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/024B68B5-79AF-DD11-8101-000423D944F8.root',
	'/store/data/Commissioning08/Cosmics/RAW/v1/000/070/664/0042899F-7EAF-DD11-9036-001617DF785A.root'



    )
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

##----## Sequences and Paths:
#process.Reco = cms.Sequence(process.siPixelRecHits)
process.Reco = cms.Sequence(process.siPixelDigis*process.siPixelClusters*process.siPixelRecHits)
process.RAWmonitor = cms.Sequence(process.SiPixelRawDataErrorSource)
process.DIGImonitor = cms.Sequence(process.SiPixelDigiSource)
process.CLUmonitor = cms.Sequence(process.SiPixelClusterSource)
process.HITmonitor = cms.Sequence(process.SiPixelRecHitSource)
process.DQMmodules = cms.Sequence(process.qTester*process.dqmEnv*process.dqmSaver)
process.CERTmodules = cms.Sequence(process.sipixelDaqInfo*process.sipixelDcsInfo*process.sipixelCertification)
#process.siPixelLocalReco = cms.Sequence(process.siPixelRecHits) 
#process.siStripLocalReco = cms.Sequence(process.siStripMatchedRecHits)
#process.trackerLocalReco = cms.Sequence(process.siPixelLocalReco*process.siStripLocalReco)
#process.trackReconstruction = cms.Sequence(process.trackerLocalReco*process.offlineBeamSpot*process.recopixelvertexing*process.tracksP5) #*process.rstracks 
#process.monitorTrack = cms.Sequence(process.SiPixelTrackResidualSource)
#process.monitors = cms.Sequence(process.SiPixelRawDataErrorSource*process.SiPixelDigiSource*process.SiPixelClusterSource*process.SiPixelRecHitSource*process.SiPixelTrackResidualSource)

#process.p = cms.Path(process.Reco*process.dqmEnv*process.siPixelP5DQM_source_woTrack*process.qTester*process.PixelP5DQMClientWithDataCertification*process.dqmSaver)
#process.pathTrack = cms.Path(process.trackReconstruction*process.DQMmodules*process.monitors*process.sipixelEDAClient) 
#process.p = cms.Path(process.Reco*process.dqmEnv*process.siPixelOfflineDQM_source_woTrack*process.PixelOfflineDQMClientWithDataCertification*process.dqmSaver)
#process.p = cms.Path(process.Reco*process.dqmEnv*process.siPixelOfflineDQM_source_woTrack*process.qTester*process.PixelOfflineDQMClientWithDataCertification*process.dqmSaver)
process.p = cms.Path(process.Reco*process.dqmEnv*process.DIGImonitor*process.PixelP5DQMClientWithDataCertification*process.dqmSaver)

