import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.SelectHLTOutput = cms.untracked.string('hltOutputHLTDQM')

process.load("DQMServices.Core.DQM_cfg")
process.DQMStore.referenceFileName = "/dqmdata/dqm/reference/hlt_reference.root"

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_cfi")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.EndOfProcess_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("RecoTracker.TkTrackingRegions.GlobalTrackingRegion_cfi")
process.load("RecoVertex.PrimaryVertexProducer.OfflinePixel3DPrimaryVertices_cfi")
#----------------------------
# Pixel-Tracks Configuration
#----------------------------
process.PixelTrackReconstructionBlock.RegionFactoryPSet.ComponentName = "GlobalRegionProducer"


#----------------------------
# Pixel-Vertices Configuration
#----------------------------
process.pixelVertices.useBeamConstraint = False
process.pixelVertices.TkFilterParameters.minPt = process.pixelTracks.RegionFactoryPSet.RegionPSet.ptMin

process.load("Configuration.StandardSequences.MagneticField_cff")
process.GlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" ) # for muon hlt dqm
#SiStrip Local Reco
process.SiStripDetInfoFileReader = cms.Service("SiStripDetInfoFileReader")
process.TkDetMap = cms.Service("TkDetMap")

#---- for P5 (online) DB access
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

process.load("DQM.HLTEvF.HLTMonitor_cff")
process.load("DQM.HLTEvF.HLTMonitorClient_cff")
# added for hlt scalars
process.load("DQM.TrigXMonitor.HLTSeedL1LogicScalers_cfi")
# added for hlt scalars
process.hltSeedL1Logic.l1GtData = cms.InputTag("l1GtUnpack","","DQM")
process.hltSeedL1Logic.dqmFolder =    cms.untracked.string("HLT/HLTSeedL1LogicScalers_SM")
process.load('DQM.BeamMonitor.PixelVTXMonitor_cfi')

process.reconstruction_step = cms.Sequence(
        process.siPixelDigis*
        process.offlineBeamSpot*
        process.siPixelClusters*
        process.siPixelRecHits*
        process.pixelTracks*
        process.pixelVertices)


#process.p = cms.EndPath(process.hlts+process.hltsClient)
process.p = cms.EndPath(process.hltSeedL1Logic)


process.pp = cms.Path(process.reconstruction_step *
                      process.pixelVTXMonitor*
                      process.dqmEnv*
                      process.dqmSaver)
process.EventStreamHttpReader.consumerName = 'HLT DQM Consumer'
process.dqmEnv.subSystemFolder = 'HLT'
#process.hltResults.plotAll = True

