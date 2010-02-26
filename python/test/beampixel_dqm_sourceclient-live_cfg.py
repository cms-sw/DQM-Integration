import FWCore.ParameterSet.Config as cms

process = cms.Process("EvFDQM")

#----------------------------
#### Event Source
#----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'Beam Pixel DQM Consumer'
#process.EventStreamHttpReader.maxEventRequestRate = cms.untracked.double(50.0)



#----------------------------
#### DQM Environment
#----------------------------
process.load("DQMServices.Core.DQM_cfg")
#process.DQMStore.referenceFileName = "DT_reference.root"


#----------------------------
#### DQM Environment
#----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'BeamPixel'
#-----------------------------


# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
                                    )

# Global tag
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")


#-----------------------------
#### Sub-system configuration follows
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
                                        nLumiReset = cms.uint32(0))
)

process.pixelVertices = cms.EDProducer("PrimaryVertexProducer",
    PVSelParameters = cms.PSet(
        maxDistanceToBeam = cms.double(2), ## 2 cms in case there is no beamspot (ONLY FOR STARTUP!)
        minVertexFitProb = cms.double(0.01) ## 1% vertex fit probability

    ),
    verbose = cms.untracked.bool(False),
    algorithm = cms.string('AdaptiveVertexFitter'), ## 100 is for when the beamspot is not well known (ONLY FOR STARTUP)
    TkFilterParameters = cms.PSet(
        maxNormalizedChi2 = cms.double(100.0),
        minSiliconHits = cms.int32(2), ## hits > 2 - for when the beamspot is not well known (ONLY FOR STARTUP)

        maxD0Significance = cms.double(100.0), ## 100 is for when the beamspot is not well known (ONLY FOR STARTUP)

        minPt = cms.double(0.9), ## better for softish events

        minPixelHits = cms.int32(2) ## hits > 2

    ),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    # label of tracks to be used
    TrackLabel = cms.InputTag("pixelTracks"),
    useBeamConstraint = cms.bool(False),
    VtxFinderParameters = cms.PSet(
        ptCut = cms.double(0.0),
        vtxFitProbCut = cms.double(0.01), ## 1% vertex fit probability
        trackCompatibilityToSVcut = cms.double(0.01), ## 1%
        trackCompatibilityToPVcut = cms.double(0.05), ## 5%
        maxNbOfVertices = cms.int32(0) ## search all vertices in each cluster
    ),
    TkClusParameters = cms.PSet(
        zSeparation = cms.double(1.0) ## 1 cm max separation betw. clusters

    )
)

###### FIXES TRIPLETS FOR LARGE BS DISPLACEMENT ######

### pixelTracks
#---- replaces ----
process.pixelTracks.RegionFactoryPSet.ComponentName = 'GlobalRegionProducerFromBeamSpot' # was GlobalRegionProducer
#---- new parameters ----
process.pixelTracks.RegionFactoryPSet.RegionPSet.nSigmaZ  = cms.double(4.06) # was originHalfLength = 15.9; translated assuming sigmaZ ~ 3.8
process.pixelTracks.RegionFactoryPSet.RegionPSet.beamSpot = cms.InputTag("offlineBeamSpot")



# DQM Modules
process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)
#process.physicsEventsFilter = cms.EDFilter("HLTTriggerTypeFilter",
#                                  # 1=Physics, 2=Calibration, 3=Random, 4=Technical
#                                  SelectedTriggerType = cms.int32(1)
#                                  ) 
#-----------------------------
### Define the path
process.reconstruction_step = cms.Path(process.siPixelDigis*process.offlineBeamSpot*process.siPixelClusters*process.siPixelRecHits*process.pixelTracks*process.pixelVertices*process.pixelVertexDQM)

process.evfDQMmodulesPath = cms.Path(process.dqmmodules)

process.schedule = cms.Schedule(process.reconstruction_step,process.evfDQMmodulesPath)
