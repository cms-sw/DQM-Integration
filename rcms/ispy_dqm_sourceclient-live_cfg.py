import FWCore.ParameterSet.Config as cms

process = cms.Process("IGUANA")

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")
process.GlobalTag.globaltag = 'CRAFT_V2H::All'
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"


process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'iSpy Event Display'
#process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(-1)
#)
#process.source = cms.Source("EventStreamHttpReader",
#	sourceURL = cms.string("http://localhost:5000/urn:xdaq-application:lid=29"),
#	sourceURL = cms.string('http://srv-c2d05-05.cms:50082/urn:xdaq-application:lid=29'),
#	sourceURL = cms.string('http://srv-c2d05-14.cms:22100/urn:xdaq-application:lid=30'),
#	consumerPriority = cms.untracked.string('normal'),
#	max_event_size = cms.int32(7000000),
#	consumerName = cms.untracked.string('Event Display'),
#	max_queue_depth = cms.int32(5),
#	SelectHLTOutput = cms.untracked.string("hltOutputDQM"),
#	maxEventRequestRate = cms.untracked.double(35.0),
#	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('*')),
#	headerRetryInterval = cms.untracked.int32(3)
#)

from FWCore.MessageLogger.MessageLogger_cfi import *

process.add_(
    cms.Service("IguanaService",
    outputFileName = cms.untracked.string('/home/dqmprolocal/output/Higgs200ChargedTaus.ig'),
    outputESFileName = cms.untracked.string('/home/dqmprolocal/output/iggi_FrontierConditions_GlobalTag_STARTUP_V5.ig'),
    outputMaxEvents = cms.untracked.int32(3000),
    outputHost = cms.untracked.string('localhost'),
    outputPort = cms.untracked.uint32(9000),
    online = cms.untracked.bool(True),
    debug = cms.untracked.bool(False)
    )
)


process.load("VisReco.Analyzer.VisBasicCluster_cfi")
process.load("VisReco.Analyzer.VisCaloTower_cfi")
process.load("VisReco.Analyzer.VisCSCSegment_cfi")
process.load("VisReco.Analyzer.VisDTDigi_cfi")
process.load("VisReco.Analyzer.VisDTRecHit_cfi")
process.load("VisReco.Analyzer.VisDTRecSegment4D_cfi")
process.load("VisReco.Analyzer.VisEcalRecHit_cfi")
process.load("VisReco.Analyzer.VisEvent_cfi")
process.load("VisReco.Analyzer.VisEventSetup_cfi")
process.load("VisReco.Analyzer.VisHBRecHit_cfi")
process.load("VisReco.Analyzer.VisHERecHit_cfi")
process.load("VisReco.Analyzer.VisHFRecHit_cfi")
process.load("VisReco.Analyzer.VisHORecHit_cfi")
process.load("VisReco.Analyzer.VisJet_cfi")
process.load("VisReco.Analyzer.VisMET_cfi")
process.load("VisReco.Analyzer.VisMuon_cfi")
process.load("VisReco.Analyzer.VisPixelDigi_cfi")
process.load("VisReco.Analyzer.VisRPCRecHit_cfi")
process.load("VisReco.Analyzer.VisSiPixelCluster_cfi")
process.load("VisReco.Analyzer.VisSiPixelRecHit_cfi")
process.load("VisReco.Analyzer.VisSiStripCluster_cfi")
process.load("VisReco.Analyzer.VisSiStripDigi_cfi")
process.load("VisReco.Analyzer.VisTrack_cfi")
process.load("VisReco.Analyzer.VisTrackingRecHit_cfi")

process.VisTrack.visTrackTag = cms.InputTag("globalCosmicMuons")
process.VisTrackingRecHit.visTrackingRecHitTag = cms.InputTag("globalCosmicMuons")
process.VisSiStripDigi.visSiStripDigiTag = cms.InputTag("siStripDigis","ZeroSuppressed")
process.VisMuon.visMuonTag = cms.InputTag("muons")
process.VisBasicCluster.visBasicClusterTag = cms.InputTag("cosmicBasicClusters","CosmicBarrelBasicClusters")
process.VisPixelDigi.VisPixelDigiTag = cms.InputTag("siPixelDigis","")

process.p1 = cms.Path(process.RawToDigi_woGCT*
                      process.reconstructionCosmics*
                      process.VisEvent*
                      process.VisEventSetup*
                      process.VisTrack*
                      process.VisTrackingRecHit*
                      process.VisCSCSegment*
                      process.VisCaloTower*
                      process.VisDTRecSegment4D*
                      process.VisDTRecHit*
                      process.VisDTDigi*
                      process.VisRPCRecHit*
                      process.VisEcalRecHit*
                      process.VisHBRecHit*
                      process.VisHERecHit*
                      process.VisHFRecHit*
                      process.VisHORecHit*
                      process.VisMET*
                      process.VisMuon*
                      process.VisPixelDigi*
                      process.VisSiPixelCluster*
                      process.VisSiPixelRecHit*
                      process.VisSiStripCluster*
                      process.VisSiStripDigi*
                      process.VisJet)

