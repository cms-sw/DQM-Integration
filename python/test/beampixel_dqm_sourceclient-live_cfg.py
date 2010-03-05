import FWCore.ParameterSet.Config as cms

process = cms.Process("BeamPixel")


#----------------------------
#### Event Source
#----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = "Beam Pixel DQM Consumer"
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("HLT_MinBiasBSC","HLT_L1_BSC")) # Uncomment to add a filter on data


#--------------------------
# Filters
#--------------------------
# HLT Filter
process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1
# L1 Filter
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMaskTechTrigConfig_cff")
process.load("HLTrigger/HLTfilters/hltLevel1GTSeed_cfi")
process.hltLevel1GTSeed.L1TechTriggerSeeding = cms.bool(True)
process.hltLevel1GTSeed.L1SeedsLogicalExpression = cms.string("(40 OR 41) AND NOT (36 OR 37 OR 38 OR 39) AND (NOT 42 OR 43) AND (42 OR NOT 43)")


#----------------------------
#### DQM Environment
#----------------------------
process.load("DQMServices.Core.DQM_cfg")
#----------------------------
#### DQM Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = "BeamPixel"
#-----------------------------


process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING')))


process.load("DQM.Integration.test.FrontierCondition_GT_cfi")


#### Sub-system configuration follows ###
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryExtended_cff')
process.load('Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration/StandardSequences/RawToDigi_Data_cff')
process.load('Configuration/StandardSequences/Reconstruction_cff')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration/EventContent/EventContent_cff')

process.pixelVertexDQM = cms.EDProducer("Vx3DHLTAnalyzer",
                                        vertexCollection = cms.InputTag("pixelVertices"),
                                        nLumiReset = cms.uint32(3),
                                        xRange = cms.double(4.0),
                                        xStep = cms.double(0.001),
                                        yRange = cms.double(4.0),
                                        yStep = cms.double(0.001),
                                        zRange = cms.double(40.0),
                                        zStep = cms.double(0.05))


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
        minPt = cms.double(0.9), # Default 0 @@@@@@
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
#---- replaces ----
process.pixelTracks.RegionFactoryPSet.ComponentName = 'GlobalRegionProducerFromBeamSpot' # It was GlobalRegionProducer
#---- new parameters ----
process.pixelTracks.RegionFactoryPSet.RegionPSet.nSigmaZ  = cms.double(4.06) # It was originHalfLength = 15.9; translated assuming sigmaZ ~3.8
process.pixelTracks.RegionFactoryPSet.RegionPSet.beamSpot = cms.InputTag("offlineBeamSpot")


### DQM Modules ###
process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)


### Define the path ###
process.phystrigger = cms.Sequence(process.hltTriggerTypeFilter*
                                   process.gtDigis*
                                   process.hltLevel1GTSeed)
process.reconstruction_step = cms.Path(
    process.siPixelDigis*
    process.offlineBeamSpot*
    process.siPixelClusters*
    process.siPixelRecHits*
    process.pixelTracks*
    process.pixelVertices*
    process.pixelVertexDQM)
process.evfDQMmodulesPath = cms.Path(process.dqmmodules)

### Uncomment to add a filter on data ###
#process.schedule = cms.Schedule(
#    process.phystrigger*
#    process.reconstruction_step,process.evfDQMmodulesPath)
process.schedule = cms.Schedule(process.reconstruction_step,process.evfDQMmodulesPath)
