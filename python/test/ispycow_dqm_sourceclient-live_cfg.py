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
process.load("Configuration/StandardSequences/Geometry_cff")
process.load("Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff")
process.load('Configuration/StandardSequences/Reconstruction_cff')
process.load("Configuration/StandardSequences/RawToDigi_Data_cff")
process.load('Configuration/StandardSequences/L1Reco_cff')
process.load('Configuration/StandardSequences/VtxSmearedEarly10TeVCollision_cff')
process.load("DQM/Integration/test/FrontierCondition_GT_cfi")
process.load("ISpy/Analyzers/ISpy_Online_Producer_cff")
from FWCore.MessageLogger.MessageLogger_cfi import *
process.load('L1TriggerConfig.L1GtConfigProducers.L1GtTriggerMenuConfig_cff')
process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')
process.load('L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1031.L1Menu_MC2009_v2_L1T_Scales_20080922_Imp0_Unprescaled_cff')
####### Event Source
process.source = cms.Source("EventStreamHttpReader",
   sourceURL = cms.string('http://dvsrv-c2f37-01:43100/urn:xdaq-application:lid=50'),
   consumerPriority = cms.untracked.string('normal'),
   max_event_size = cms.int32(7000000),
   consumerName = cms.untracked.string('ISpy COW Event Display '),
   SelectHLTOutput = cms.untracked.string('outEVD'),
   max_queue_depth = cms.int32(5),
   maxEventRequestRate = cms.untracked.double(10.0),
   SelectEvents = cms.untracked.PSet(
       SelectEvents = cms.vstring('*')
   ),
   headerRetryInterval = cms.untracked.int32(3)
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

####### DQM Default File Location
process.load("DQM.Integration.test.environment_cfi")
####### ISpy Service
process.add_(
    cms.Service("ISpyService",
    outputFileName = cms.untracked.string('%s/iSpy_BEAM%d_%s__COW_.ig' % (process.dqmSaver.dirName.value(),int(dt.date.today().strftime("%W"))+1,dt.date.today().strftime("%Y%m%d"))),
    #outputFileName = cms.untracked.string('/home/lilopera/CMSSW/output/iSpy_MWGR%d_%s__hltOutputDQM_.ig' % (int(dt.date.today().strftime("%W"))+1,dt.date.today().strftime("%Y%m%d"))),
    outputESFileName=cms.untracked.string('/tmp/iSpy_ES.ig'),
    bufferSize = cms.untracked.uint32(1),
    outputHost = cms.untracked.string('localhost'),
    outputPort = cms.untracked.uint32(9003),
    outputMaxEvents = cms.untracked.int32(100),
    online = cms.untracked.bool(True),
    debug = cms.untracked.bool(False)
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
process.ISpyTrackingRecHit.iSpyTrackingRecHitTag = cms.InputTag('cosmicMuons')
process.ISpyTrack.iSpyTrackTag = cms.InputTag('cosmicMuons')
process.ISpyTrack.iSpyTrackTags = cms.VInputTag(cms.InputTag('cosmicMuons'),
                                                cms.InputTag('cosmictrackfinderP5'),
                                                cms.InputTag('ctfWithMaterialTracksP5'),
                                                cms.InputTag('generalTracks'),
                                                cms.InputTag('ctfPixelLess'),
                                                cms.InputTag('pixelTracks')
                                               )
####### Path                                             
process.p= cms.Path(process.iSpy_online_sequence)


