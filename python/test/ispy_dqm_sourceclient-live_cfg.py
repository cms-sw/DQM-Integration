import FWCore.ParameterSet.Config as cms
import datetime as dt
process = cms.Process("iSpy EVD")
####### Event processor configuration
process.options=cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring(["FatalRootError",
    		"Root_Error:  CosmicClusterProducer:cosmicBasicClusters",
		"Root_Error: ",
		"CosmicClusterProducer:cosmicBasicClusters",
    		"Root_Error:  CosmicClusterProducer:cosmicBasicClusters  TUnixSystem::DispatchSignals()",
		"TUnixSystem::DispatchSignals()",
		"DataCorrupt"])
  )

####### Components
Cosmics=True
if Cosmics:
  process.load('Configuration/StandardSequences/ReconstructionCosmics_cff') 
  BaseName="MWGR" 
else:
  process.load('Configuration/StandardSequences/Reconstruction_cff')
  BaseName="BEAM"
# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryExtended_cff')
process.load("Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
process.load('Configuration/StandardSequences/L1Reco_cff')
process.load("DQM/Integration/test/FrontierCondition_GT_cfi")
process.load("ISpy/Analyzers/ISpy_Online_Producer_cff")
from FWCore.MessageLogger.MessageLogger_cfi import *

####### Event Source
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'ISpy Event Display hltOutputDQM stream'
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_MinBiasBSC','HLT_MinBiasPixel*'))

####### DQM Default File Location
process.load("DQM.Integration.test.environment_cfi")
if process.dqmSaver.producer.value() == "DQM":
  igFileOutput=True
  igDebug=False
else:
  igFileOutput=False
  igDebug=True
  
####### ISpy Service
process.add_(
    cms.Service("ISpyService",
    outputFileName = cms.untracked.string('%s/iSpy_%s%d_%s__hltOutputDQM_.ig' % (process.dqmSaver.dirName.value(),BaseName,int(dt.date.today().strftime("%W"))+1,dt.date.today().strftime("%Y%m%d"))),
    outputESFileName=cms.untracked.string('/tmp/iSpy_ES.ig'),
    bufferSize = cms.untracked.uint32(1),
    outputHost = cms.untracked.string('localhost'),
    outputPort = cms.untracked.uint32(9000),
    outputMaxEvents = cms.untracked.int32(100),
    outputMaxTime = cms.untracked.int32(600),
    outputIg = cms.untracked.bool(igFileOutput),
    online = cms.untracked.bool(True),
    debug = cms.untracked.bool(igDebug)
    )
)

####### Producers input tags
process.ISpyCSCSegment.iSpyCSCSegmentTag = cms.InputTag("cscSegments")
process.ISpyCSCStripDigi.iSpyCSCStripDigiTag = cms.InputTag("muonCSCDigis:MuonCSCStripDigi")
process.ISpyCSCWireDigi.iSpyCSCWireDigiTag = cms.InputTag("muonCSCDigis:MuonCSCWireDigi")
process.ISpyDTRecHit.iSpyDTRecHitTag = cms.InputTag("dt1DRecHits")
process.ISpyRPCRecHit.iSpyRPCRecHitTag = cms.InputTag("rpcRecHits")
process.ISpyMuon.iSpyMuonTag = cms.InputTag('muons')
process.ISpySiStripDigi.iSpySiStripDigiTag = cms.InputTag('siStripDigis:ZeroSuppressed')
process.ISpyTrackingRecHit.iSpyTrackingRecHitTag = cms.InputTag('generalTracks')
process.ISpyTrack.iSpyTrackTags = cms.VInputTag(cms.InputTag('cosmicMuons'),
                                                cms.InputTag('cosmictrackfinderP5'),
                                                cms.InputTag('generalTracks')
                                               )

#####################################################################################################
####
####  Top level replaces for handling strange scenarios of early collisions
####

## TRACKING:
process.globalPixelLessSeeds.RegionFactoryPSet.RegionPSet.ptMin = 0.5
process.pixelLessCkfTrajectoryFilter = process.ckfBaseTrajectoryFilter.clone(
    ComponentName = 'pixelLessCkfTrajectoryFilter',
    filterPset = process.ckfBaseTrajectoryFilter.filterPset.clone(minPt = 0.5)
    )
process.pixelLessCkfTrajectoryBuilder = process.GroupedCkfTrajectoryBuilder.clone(
    ComponentName = 'pixelLessCkfTrajectoryBuilder',
    trajectoryFilterName = 'pixelLessCkfTrajectoryFilter',
    )
process.ckfTrackCandidatesPixelLess.TrajectoryBuilder = 'pixelLessCkfTrajectoryBuilder'
process.globalPixelLessSeeds.RegionFactoryPSet.RegionPSet.originHalfLength = 40
process.globalPixelLessSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters = 5000
## Skip events with HV off
process.fourthPLSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters = 20000
process.fifthSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters = 5000
## Seeding: increase the region
process.fifthSeeds.RegionFactoryPSet.RegionPSet.originHalfLength = 100
process.fifthSeeds.RegionFactoryPSet.RegionPSet.originRadius     =  20
## Seeding: add TOB3 to the list, allow unmatched hits
process.fifthlayerpairs.TOB.useSimpleRphiHitsCleaner = cms.bool(False)
process.fifthlayerpairs.TOB.rphiRecHits = cms.InputTag("fifthStripRecHits","rphiRecHitUnmatched")
process.fifthlayerpairs.TOB.stereoRecHits = cms.InputTag("fifthStripRecHits","stereoRecHitUnmatched")
process.fifthlayerpairs.layerList += [ 'TOB1+TOB3', 'TOB2+TOB3' ]
#, 'TOB3+TOB4' ]
## Pattern recognition: lower the cut on the number of hits
process.fifthCkfTrajectoryFilter.filterPset.minimumNumberOfHits = 5
process.fifthCkfTrajectoryFilter.filterPset.maxLostHits = 3
process.fifthCkfTrajectoryFilter.filterPset.maxConsecLostHits = 1
process.fifthCkfInOutTrajectoryFilter.filterPset.minimumNumberOfHits = 3
process.fifthCkfInOutTrajectoryFilter.filterPset.maxLostHits = 3
process.fifthCkfInOutTrajectoryFilter.filterPset.maxConsecLostHits = 1
process.fifthCkfTrajectoryBuilder.minNrOfHitsForRebuild = 3
## Pattern recognition: enlarge a lot the search window, as the true momentum is very small while the tracking assumes p=5 GeV if B=0
#process.Chi2MeasurementEstimator.MaxChi2 = 200
process.Chi2MeasurementEstimator.nSigma  = 3
## Fitter-smoother: lower the cut on the number of hits
process.fifthRKTrajectorySmoother.minHits = 4
process.fifthRKTrajectoryFitter.minHits = 4
process.fifthFittingSmootherWithOutlierRejection.MinNumberOfHits = 5
## Fitter-smoother: loosen outlier rejection
process.fifthFittingSmootherWithOutlierRejection.BreakTrajWith2ConsecutiveMissing = False
process.fifthFittingSmootherWithOutlierRejection.EstimateCut = 1000
## Quality filter
process.tobtecStepLoose.minNumberLayers = 3
process.tobtecStepLoose.minNumber3DLayers = 0
process.tobtecStepLoose.maxNumberLostLayers = 4
process.tobtecStepLoose.dz_par1 = cms.vdouble(100.5, 4.0)
process.tobtecStepLoose.dz_par2 = cms.vdouble(100.5, 4.0)
process.tobtecStepLoose.d0_par1 = cms.vdouble(100.5, 4.0)
process.tobtecStepLoose.d0_par2 = cms.vdouble(100.5, 4.0)
process.tobtecStepLoose.chi2n_par = cms.double(10.0)
process.tobtecStepLoose.keepAllTracks = False
process.tobtecStepTight = process.tobtecStepLoose.clone(
    keepAllTracks = True,
    qualityBit = cms.string('tight'),
    src = cms.InputTag("tobtecStepLoose"),
    minNumberLayers = 5,
    minNumber3DLayers = 0
    )
process.tobtecStep = process.tobtecStepLoose.clone(
    keepAllTracks = True,
    qualityBit = cms.string('highPurity'),
    src = cms.InputTag("tobtecStepTight"),
    minNumberLayers = 4,
    minNumber3DLayers = 2,
    )

## PV temporary fixes
process.offlinePrimaryVertices.PVSelParameters.maxDistanceToBeam = 10
process.offlinePrimaryVertices.TkFilterParameters.maxNormalizedChi2 = 500
process.offlinePrimaryVertices.TkFilterParameters.minSiliconHits = 5
process.offlinePrimaryVertices.TkFilterParameters.maxD0Significance = 100
process.offlinePrimaryVertices.TkFilterParameters.minPixelHits = -1
process.offlinePrimaryVertices.TkClusParameters.zSeparation = 10

## ECAL temporary fixes
process.load('RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi')
#process.ecalLocalRecoSequence.replace(process.ecalGlobalUncalibRecHit,process.ecalFixedAlphaBetaFitUncalibRecHit)
process.ecalFixedAlphaBetaFitUncalibRecHit.alphaEB = 1.138
process.ecalFixedAlphaBetaFitUncalibRecHit.betaEB = 1.655
process.ecalFixedAlphaBetaFitUncalibRecHit.alphaEE = 1.890
process.ecalFixedAlphaBetaFitUncalibRecHit.betaEE = 1.400
process.ecalRecHit.EBuncalibRecHitCollection = 'ecalFixedAlphaBetaFitUncalibRecHit:EcalUncalibRecHitsEB'
process.ecalRecHit.EEuncalibRecHitCollection = 'ecalFixedAlphaBetaFitUncalibRecHit:EcalUncalibRecHitsEE'
process.ecalRecHit.ChannelStatusToBeExcluded = [ 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 78, 142 ]
#process.ecalBarrelCosmicTask.EcalUncalibratedRecHitCollection = 'ecalFixedAlphaBetaFitUncalibRecHit:EcalUncalibRecHitsEB'
#process.ecalEndcapCosmicTask.EcalUncalibratedRecHitCollection = 'ecalFixedAlphaBetaFitUncalibRecHit:EcalUncalibRecHitsEE'
#process.ecalBarrelTimingTask.EcalUncalibratedRecHitCollection = 'ecalFixedAlphaBetaFitUncalibRecHit:EcalUncalibRecHitsEB'
#process.ecalEndcapTimingTask.EcalUncalibratedRecHitCollection = 'ecalFixedAlphaBetaFitUncalibRecHit:EcalUncalibRecHitsEE'

## HCAL temporary fixes
process.hfreco.firstSample  = 3
process.hfreco.samplesToAdd = 4

## Beamspot temporary fix
#from CondCore.DBCommon.CondDBSetup_cfi import *
#process.firstCollBeamspot = cms.ESSource(
#    "PoolDBESSource",CondDBSetup,
#    connect = cms.string("frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)(failovertoserver=no)/CMS_COND_31X_BEAMSPOT"),
#    toGet = cms.VPSet(cms.PSet(record = cms.string("BeamSpotObjectsRcd"),
#                               tag = cms.string("firstcollisions"))
#                      )
#    )
#process.es_prefer_firstCollBeamspot = cms.ESPrefer("PoolDBESSource","firstCollBeamspot")

###
###  end of top level replacements
###
###############################################################################################

####### Trigger Filters for physics events
process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1

####### Path
if Cosmics:
  process.p= cms.Path(process.hltTriggerTypeFilter*
                     process.RawToDigi*
                     process.reconstructionCosmics*
                     process.iSpy_online_sequence
                    )
else:
  process.p= cms.Path(process.hltTriggerTypeFilter*
                     process.RawToDigi*
                     process.reconstruction_withPixellessTk*
                     process.iSpy_online_sequence
                    )
