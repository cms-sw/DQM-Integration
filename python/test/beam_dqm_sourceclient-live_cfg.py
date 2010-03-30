import FWCore.ParameterSet.Config as cms

process = cms.Process("BeamMonitor")

#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_MinBia*','HLT_L1*'))
#process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('HLT_MinBiasBSC','HLT_L1_BSC'))

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
process.hltLevel1GTSeed.L1SeedsLogicalExpression = cms.string('40 OR 41')

#----------------------------
# DQM Live Environment
#-----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'BeamMonitor'

import DQMServices.Components.DQMEnvironment_cfi
process.dqmEnvPixelLess = DQMServices.Components.DQMEnvironment_cfi.dqmEnv.clone()
process.dqmEnvPixelLess.subSystemFolder = 'BeamMonitor_PixelLess'

#----------------------------
# BeamMonitor
#-----------------------------
process.load("DQM.BeamMonitor.BeamMonitor_cff")
process.load("DQM.BeamMonitor.BeamMonitor_PixelLess_cff")
process.load("DQM.BeamMonitor.BeamConditionsMonitor_cff")
process.dqmBeamMonitor.resetEveryNLumi = 40
process.dqmBeamMonitor.resetPVEveryNLumi = 20
####  SETUP TRACKING RECONSTRUCTION ####

#-------------------------------------------------
# GEOMETRY
#-------------------------------------------------
process.load("Configuration.StandardSequences.Geometry_cff")

#-----------------------------
# Magnetic Field
#-----------------------------
#process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

#--------------------------
# Calibration
#--------------------------
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

#-----------------------
#  Reconstruction Modules
#-----------------------
## Collision Reconstruction
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")

## Pixelless Tracking
process.load('RecoTracker/Configuration/RecoTrackerNotStandard_cff')
process.MeasurementTracker.pixelClusterProducer = cms.string("")

# Offline Beam Spot
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

## Offline PrimaryVertices
import RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi
process.offlinePrimaryVertices = RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi.offlinePrimaryVertices.clone()
## Input track for PrimaryVertex reconstruction, uncomment the following line to use pixelLess tracks
#process.offlinePrimaryVertices.TrackLabel = cms.InputTag("ctfPixelLess")
process.dqmBeamMonitor.BeamFitter.TrackCollection = cms.untracked.InputTag('firstStepTracksWithQuality')
process.offlinePrimaryVertices.TrackLabel = cms.InputTag("firstStepTracksWithQuality")
 
## Skip events with HV off/beam gas scraping events
process.newSeedFromTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=2000
process.newSeedFromPairs.ClusterCheckPSet.MaxNumberOfCosmicClusters=10000
process.secTriplets.ClusterCheckPSet.MaxNumberOfPixelClusters=2000
process.fifthSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters = 10000
process.fourthPLSeeds.ClusterCheckPSet.MaxNumberOfCosmicClusters=10000
### 0th step of iterative tracking
#---- replaces ----
process.newSeedFromTriplets.RegionFactoryPSet.ComponentName = 'GlobalRegionProducerFromBeamSpot' # was GlobalRegionProducer
#---- new parameters ----
process.newSeedFromTriplets.RegionFactoryPSet.RegionPSet.nSigmaZ = cms.double(4.06) # was originHalfLength = 15.9; translated assuming sigmaZ ~ 3.8
process.newSeedFromTriplets.RegionFactoryPSet.RegionPSet.beamSpot = cms.InputTag("offlineBeamSpot")

#### END OF TRACKING RECONSTRUCTION ####

# Change Beam Monitor variables
if process.dqmSaver.producer.value() is "Playback":
  process.dqmBeamMonitor.BeamFitter.WriteAscii = False
  process.dqmBeamMonitor.BeamFitter.AsciiFileName = '/nfshome0/yumiceva/BeamMonitorDQM/BeamFitResults.txt'
  process.dqmBeamMonitor.BeamFitter.WriteDIPAscii = True
  process.dqmBeamMonitor.BeamFitter.DIPFileName = '/nfshome0/dqmdev/BeamMonitorDQM/BeamFitResults.txt'
else:
  process.dqmBeamMonitor.BeamFitter.WriteAscii = True
  process.dqmBeamMonitor.BeamFitter.AsciiFileName = '/nfshome0/yumiceva/BeamMonitorDQM/BeamFitResults.txt'
  process.dqmBeamMonitor.BeamFitter.WriteDIPAscii = True
  process.dqmBeamMonitor.BeamFitter.DIPFileName = '/nfshome0/dqmpro/BeamMonitorDQM/BeamFitResults.txt'
#process.dqmBeamMonitor.BeamFitter.SaveFitResults = False
#process.dqmBeamMonitor.BeamFitter.OutputFileName = '/nfshome0/yumiceva/BeamMonitorDQM/BeamFitResults.root'

#--------------------------
# Scheduling
#--------------------------
process.phystrigger = cms.Sequence(process.hltTriggerTypeFilter*process.gtDigis*process.hltLevel1GTSeed)
process.dqmcommon = cms.Sequence(process.dqmEnv*process.dqmSaver)
process.tracking = cms.Sequence(process.siPixelDigis*process.siStripDigis*process.trackerlocalreco*process.offlineBeamSpot*process.recopixelvertexing*process.ckftracks)
process.monitor = cms.Sequence(process.dqmBeamMonitor)
process.tracking_pixelless = cms.Sequence(process.siPixelDigis*process.siStripDigis*process.trackerlocalreco*process.offlineBeamSpot*process.ctfTracksPixelLess)
process.monitor_pixelless = cms.Sequence(process.dqmBeamMonitor_pixelless*process.dqmEnvPixelLess)
process.tracking_FirstStep = cms.Sequence(process.siPixelDigis*process.siStripDigis*process.trackerlocalreco*process.offlineBeamSpot*process.recopixelvertexing*process.firstStep)

process.p = cms.Path(process.scalersRawToDigi*process.phystrigger*process.dqmcommon*process.tracking_FirstStep*process.offlinePrimaryVertices*process.monitor)
#process.p = cms.Path(process.gtDigis*process.scalersRawToDigi*process.tracking_FirstStep*process.offlinePrimaryVertices*process.monitor*process.dqmSaver)
#process.p = cms.Path(process.gtDigis*process.tracking*process.offlinePrimaryVertices*process.monitor*process.dqmSaver)
#process.p = cms.Path(process.phystrigger*process.tracking*process.offlinePrimaryVertices*process.monitor*process.dqmSaver)
#process.p = cms.Path(process.phystrigger*process.tracking_pixelless*process.offlinePrimaryVertices*process.monitor_pixelless*process.dqmSaver)

