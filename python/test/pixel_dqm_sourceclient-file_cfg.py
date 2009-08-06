import FWCore.ParameterSet.Config as cms

process = cms.Process("SIPIXELDQM")

##----## Geometry and other global parameters:
#process.load("Geometry.TrackerSimData.trackerSimGeometryXML_cfi")
#process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")
#process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
#process.load("Configuration.GlobalRuns.ForceZeroTeslaField_cff")
#process.load("CondCore.DBCommon.CondDBSetup_cfi")

##----## Reco:
process.load("Configuration.StandardSequences.Reconstruction_cff")
##process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")

#process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.siPixelDigis.InputLabel = 'source'
process.siPixelDigis.IncludeErrors = True

process.load("RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi")

#process.load("RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi")
#process.load("RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff")

process.load("EventFilter.SiStripRawToDigi.SiStripRawToDigis_standard_cff")
process.siStripDigis.ProductLabel = 'source'

process.load("RecoLocalTracker.SiStripClusterizer.SiStripClusterizer_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitConverter_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitMatcher_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.StripCPEfromTrackAngle_cfi")
process.load("RecoLocalTracker.SiStripZeroSuppression.SiStripZeroSuppression_cfi")

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("RecoPixelVertexing.Configuration.RecoPixelVertexing_cff")
##process.load("RecoLocalTracker.Configuration.RecoLocalTracker_Cosmics_cff")
process.load("RecoTracker.Configuration.RecoTrackerP5_cff")


#----------------------------
# Event Source
#-----------------------------
#process.load("DQM.Integration.test.inputsource_playback_cfi")
#process.EventStreamHttpReader.consumerName = 'Pixel DQM Consumer'
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_TrackerCosmics_CTF'))
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('*'))

process.source = cms.Source("NewEventStreamFileReader",
        fileNames = cms.untracked.vstring('file:/lookarea_SM/CRAFT2_2009.00108239.0036.A.storageManager.07.0000.dat')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
    )


#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
#process.DQMStore.referenceFileName = '/home/dqmprolocal/reference/pixel_reference.root'
process.load("DQMServices.Components.DQMEnvironment_cfi")
#process.DQM.filter = '^(Pixel)(/[^/]+){0,4}$'

#----------------------------
# DQM Live Environment
#-----------------------------
process.load("DQM.Integration.test.environment_playback_cfi")
process.dqmEnv.subSystemFolder    = "Pixel"

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
##process.SiPixelTrackResidualSource.TrackCandidateProducer = cms.string('newTrackCandidateMaker')
##process.SiPixelTrackResidualSource.trajectoryInput = cms.InputTag('TrackRefitterP5')


##----## Other stuff:
process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('siPixelDigis', 
        'siPixelClusters',
        'SiPixelRawDataErrorSource', 
        'SiPixelDigiSource', 
        'SiPixelClusterSource',  
        'sipixelEDAClient'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    ),
    destinations = cms.untracked.vstring('cout')
)
process.AdaptorConfig = cms.Service("AdaptorConfig")
process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")


##----## Global tag and input data:
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.connect ="sqlite_file:/home/dqmdevlocal/input/CRAFT0831X_V1H.db"
#process.GlobalTag.connect = "frontier://FrontierProd/CMS_COND_21X_GLOBALTAG"
process.GlobalTag.connect ="frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"
#process.GlobalTag.globaltag = "CRAFT_31X::All"
#process.GlobalTag.globaltag = "CRAFT0831X_V1H::All"
process.GlobalTag.globaltag = "GR09_31X_V4H::All"
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')
## this next line is needed for xdaq running outside P5 network:
#process.SiteLocalConfigService = cms.Service("SiteLocalConfigService")

##----## Sequences and Paths:
process.Reco = cms.Sequence(process.siPixelDigis
#                           *process.siPixelClusters
#			   *process.siPixelRecHits
			   )
##process.Reco = cms.Sequence(process.siPixelDigis*process.siPixelClusters)
process.RecoStrips = cms.Sequence(process.siStripDigis*process.siStripClusters)
process.siPixelLocalReco = cms.Sequence(process.siPixelRecHits) 
process.siStripLocalReco = cms.Sequence(process.siStripMatchedRecHits)
process.trackerLocalReco = cms.Sequence(process.siPixelLocalReco*process.siStripLocalReco)
process.trackReco = cms.Sequence(process.trackerLocalReco*process.offlineBeamSpot*process.recopixelvertexing*process.tracksP5) #*process.rstracks 
#process.trackReco = cms.Sequence(process.siStripDigis*process.offlineBeamSpot*process.recopixelvertexing*process.trackerlocalreco*process.ctftracksP5) #*process.rstracks 

#process.p = cms.Path(process.Reco*process.dqmEnv*process.siPixelP5DQM_source_woTrack*process.qTester*process.PixelP5DQMClientWithDataCertification*process.dqmSaver)
#process.pathTrack = cms.Path(process.trackReconstruction*process.DQMmodules*process.monitors*process.sipixelEDAClient) 
#process.p = cms.Path(process.Reco*process.dqmEnv*process.siPixelOfflineDQM_source_woTrack*process.PixelOfflineDQMClientWithDataCertification*process.dqmSaver)
#process.p = cms.Path(process.Reco*process.dqmEnv*process.siPixelOfflineDQM_source_woTrack*process.qTester*process.PixelOfflineDQMClientWithDataCertification*process.dqmSaver)
#process.p = cms.Path(process.trackReco*process.dqmEnv*process.siPixelP5DQM_cosmics_source*process.PixelP5DQMClientWithDataCertification*process.dqmSaver)

#put proces.dump in the path where you want to print all event content
#process.dump=cms.EDAnalyzer('EventContentAnalyzer')

#process.p = cms.Path(process.Reco*process.RecoStrips*process.trackReco*process.dqmEnv*process.siPixelP5DQM_cosmics_source*process.qTester*process.PixelP5DQMClientWithDataCertification*process.dqmSaver)
process.p = cms.Path(process.Reco
#                    *process.RecoStrips
#		    *process.trackReco
		    *process.dqmEnv
		    *process.siPixelP5DQM_cosmics_source
		    *process.qTester
		    *process.PixelP5DQMClientWithDataCertification
		    *process.dqmSaver)
