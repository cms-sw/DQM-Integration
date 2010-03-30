import FWCore.ParameterSet.Config as cms

process = cms.Process("BeamPixel")


#----------------------------
#### Event Source
#----------------------------
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = "Beam Pixel DQM Consumer"
### @@@@@@ Comment when running locally @@@@@@ ###
process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("HLT_MinBiasBSC","HLT_L1_BSC")) # Uncomment to add a filter on data


#--------------------------
# Filters
#--------------------------
# HLT Filter
process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1
# L1 Filter
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff")
process.load("HLTrigger.HLTfilters.hltLevel1GTSeed_cfi")
process.hltLevel1GTSeed.L1TechTriggerSeeding = cms.bool(True)
process.hltLevel1GTSeed.L1SeedsLogicalExpression = cms.string("(40 OR 41) AND NOT (36 OR 37 OR 38 OR 39) AND (NOT 42 OR 43) AND (42 OR NOT 43)")


#### DQM Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
### @@@@@@ Un-comment when running locally @@@@@@ ###
#process.DQM.collectorHost = ''
### @@@@@@ Un-comment when running locally @@@@@@ ###
process.dqmEnv.subSystemFolder = "BeamPixel"
#-----------------------------


#### Sub-system configuration follows ###
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
### @@@@@@ Comment when running locally @@@@@@ ###
process.load("FWCore/MessageService/MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.EndOfProcess_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("RecoTracker.TkTrackingRegions.GlobalTrackingRegion_cfi")


### @@@@@@ Un-comment when running locally @@@@@@ ###
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# RECO data taking february 18th 2010
#process.GlobalTag.globaltag = "GR09_R_35X_V2::All"
###### Which data ######
#process.load("DataDec09_RecoMinBias_Feb18th_Skim_GoodRuns_cff")
#process.load("DataDec09_RecoMinBias_Feb18th_Skim_Run124120_cff")
#readFiles = cms.untracked.vstring()
#secFiles = cms.untracked.vstring()
#process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
#readFiles.extend([
#        "file:/tmp/jengbou/AC4043E8-A5ED-DE11-91FB-001A92971B32.root",
#        "file:/tmp/jengbou/461F7E44-AAED-DE11-B5A4-002618943932.root",
#        "file:/tmp/jengbou/D2F80F5F-ACED-DE11-B3B6-0018F3D09630.root"])
#secFiles.extend([])
#readFiles = cms.untracked.vstring()
#secFiles = cms.untracked.vstring()
#process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
#readFiles.extend([
#        "file:/tmp/dinardo/BEF77CC5-C71D-DF11-A707-00237DA15C7C.root",
#        "file:/tmp/dinardo/B6B3BCD7-C61D-DF11-9201-00237DA1CD92.root"])
#secFiles.extend([])
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
###### DQM Saver ######
#process.dqmSaver.dirName           = cms.untracked.string("/tmp/dinardo/")
#process.dqmSaver.dirName           = cms.untracked.string("/nfshome0/yumiceva/BeamMonitorDQM/")
#process.dqmSaver.saveAtJobEnd      = cms.untracked.bool(False)
#process.dqmSaver.saveByTime        = cms.untracked.int32(-1)
#process.dqmSaver.saveByRun         = cms.untracked.int32(-1)
#process.dqmSaver.forceRunNumber    = cms.untracked.int32(-1)
#process.dqmSaver.saveByLumiSection = cms.untracked.int32(-1)
#process.dqmSaver.saveByMinute      = cms.untracked.int32(-1)
###### Output file ######
#process.Output = cms.OutputModule("PoolOutputModule",
#                                  fileName = cms.untracked.string( "/tmp/dinardo/BeamPixelResults.root" ),
#                                  outputCommands = cms.untracked.vstring( "drop *",
#                                                                           "keep *_*_*_BeamPixel"))
### @@@@@@ Un-comment when running locally @@@@@@ ###


###### pixelVertexDQM Configuration ######
process.pixelVertexDQM = cms.EDProducer("Vx3DHLTAnalyzer",
                                        vertexCollection = cms.InputTag("pixelVertices"),
                                        debugMode        = cms.bool(True),
                                        nLumiReset       = cms.uint32(2),
                                        dataFromFit      = cms.bool(True),
                                        minNentries      = cms.int32(35),
                                        # If the histogram has at least "minNentries" then extract Mean and RMS,
                                        # or, if we are performing the fit, the number of vertices must be greater
                                        # than minNentries otherwise it waits for other nLumiReset
                                        xRange           = cms.double(4.0),
                                        xStep            = cms.double(0.001),
                                        yRange           = cms.double(4.0),
                                        yStep            = cms.double(0.001),
                                        zRange           = cms.double(40.0),
                                        zStep            = cms.double(0.05),
#                                        fileName         = cms.string("/tmp/dinardo/BeamPixelResults.txt"))
                                        fileName         = cms.string("/nfshome0/yumiceva/BeamMonitorDQM/BeamPixelResults.txt"))
if process.dqmSaver.producer.value() is "Playback":
  process.pixelVertexDQM.fileName = cms.string("/nfshome0/dqmdev/BeamMonitorDQM/BeamPixelResults.txt") 
else:
  process.pixelVertexDQM.fileName = cms.string("/nfshome0/dqmpro/BeamMonitorDQM/BeamPixelResults.txt")

###### Vertexin Configuration ######
process.pixelVertices = cms.EDProducer("PrimaryVertexProducer",
                                            PVSelParameters = cms.PSet(
        maxDistanceToBeam = cms.double(2.0), # Default 0.05 with respect to beam spot axes @@@@@@
        minVertexFitProb = cms.double(0.01)), # Default 0.01 = vertex fit probability
                                            verbose = cms.untracked.bool(False),
                                            algorithm = cms.string("AdaptiveVertexFitter"),
                                            TkFilterParameters = cms.PSet(
        maxNormalizedChi2 = cms.double(100.0), # Default 5 @@@@@@
        minSiliconHits = cms.int32(2), # Default 7
        maxD0Significance = cms.double(100.0), # Default 5 with respect to beam spot axes @@@@@@
        minPt = cms.double(0.1), # Default 0 @@@@@@
        minPixelHits = cms.int32(2)), # Default 2
                                            beamSpotLabel = cms.InputTag("offlineBeamSpot"),
                                            TrackLabel = cms.InputTag("pixelTracks"), # Default "generalTracks" @@@@@@
                                            useBeamConstraint = cms.bool(False),
                                            VtxFinderParameters = cms.PSet(
        ptCut = cms.double(0.0), # Default 0 @@@@@@
        vtxFitProbCut = cms.double(0.01), # Default 0.01 = vertex fit probability
        trackCompatibilityToSVcut = cms.double(0.01), # Default 0.01
        trackCompatibilityToPVcut = cms.double(0.05), # Default 0.05
        maxNbOfVertices = cms.int32(1)), # Default 0 = search all vertices in each cluster @@@@@@
                                            TkClusParameters = cms.PSet(zSeparation = cms.double(1.0))) # Default 0.1 = max separation betw. clusters @@@@@@
                                         # Very important: it's the distance between tracks in order to merge them into a cluster


### pixelTracks ###
process.PixelTrackReconstructionBlock.RegionFactoryPSet.ComponentName = "GlobalRegionProducer"
process.pixelTracks.FilterPSet.ptMin = 0.1
process.PixelTripletHLTGenerator.extraHitRPhitolerance = 0.06
process.PixelTripletHLTGenerator.extraHitRZtolerance = 0.06
#process.GlobalTrackingRegion.RregionPSetBlock.RegionPSet.originRadius = 0.2
#process.GlobalTrackingRegion.RregionPSetBlock.RegionPSet.originHalfLength = 15.9


### @@@@@@ Un-comment when running locally @@@@@@ ###
### Select the Lumisection ###
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange("124120:1-124120:51")
### @@@@@@ Un-comment when running locally @@@@@@ ###


### Define Sequence ###
process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)

process.phystrigger = cms.Sequence(process.hltTriggerTypeFilter*
                                   process.gtDigis*
                                   process.hltLevel1GTSeed)

### @@@@@@ Comment when running locally @@@@@@ ###
process.reconstruction_step = cms.Sequence(
    process.siPixelDigis*
    process.offlineBeamSpot*
    process.siPixelClusters*
    process.siPixelRecHits*
    process.pixelTracks*
    process.pixelVertices*
    process.pixelVertexDQM)
### @@@@@@ Un-comment when running locally @@@@@@ ###
#process.reconstruction_step = cms.Sequence(
#    process.siPixelRecHits*
#    process.pixelTracks*
#    process.pixelVertices*
#    process.pixelVertexDQM)

### Define Path ###
### Uncomment to add a filter on data ###
process.schedule = cms.Path(
    process.phystrigger*
    process.reconstruction_step*
    process.dqmmodules)
### @@@@@@ Comment when running locally @@@@@@ ###
#process.p = cms.Path(process.reconstruction_step * process.dqmmodules)
### @@@@@@ Un-comment when running locally @@@@@@ ###
#process.p = cms.Path(process.reconstruction_step * process.dqmmodules * process.Output)
