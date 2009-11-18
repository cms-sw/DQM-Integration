import FWCore.ParameterSet.Config as cms

process = cms.Process("Beam Monitor")

#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")

#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

#----------------------------
# DQM Live Environment
#-----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'BeamMonitor'

#----------------------------
# BeamMonitor
#-----------------------------
process.load("DQM.BeamMonitor.BeamMonitor_Cosmics_cff") # need input track collection in the event
process.load("DQM.BeamMonitor.BeamConditionsMonitor_cff") # need beam spot collection in the event

####  SETUP TRACKING RECONSTRUCTION ####

#-------------------------------------------------
# GEOMETRY
#-------------------------------------------------
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.GeometryPilot2_cff")

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
# Real data raw to digi
process.load("EventFilter.SiStripRawToDigi.SiStripDigis_cfi")
process.siStripDigis.ProductLabel = 'source'
process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
process.siPixelDigis.InputLabel = 'source'

# Local and Track Reconstruction
process.load("RecoLocalTracker.Configuration.RecoLocalTracker_Cosmics_cff")
process.load("RecoTracker.Configuration.RecoTrackerP5_cff")

# offline beam spot
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")

#### END OF TRACKING RECONSTRUCTION ####



process.tracking = cms.Path(process.siPixelDigis*process.siStripDigis*process.offlineBeamSpot*process.trackerlocalreco*process.ctftracksP5*process.cosmictracksP5)
process.monitor = cms.Path(process.dqmBeamMonitor+process.dqmBeamCondMonitor+process.dqmEnv+process.dqmSaver)


# # summary
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string('test.root'),
#			       outputCommands = cms.untracked.vstring(
#				'drop *',
#				'keep *_offlineBeamSpot_*_*',
#				'keep *_ctfWithMaterialTracksP5_*_*',
#				'keep *_cosmictrackfinderP5_*_*'
#			       )
#                              )
#process.end = cms.EndPath(process.out)

process.schedule = cms.Schedule(process.tracking, process.monitor)

