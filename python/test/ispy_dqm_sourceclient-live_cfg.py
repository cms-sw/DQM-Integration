import FWCore.ParameterSet.Config as cms
import datetime as dt
process = cms.Process("IGUANA")

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.DigiToRaw_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load('Configuration.StandardSequences.VtxSmearedEarly10TeVCollision_cff')


process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'iSpy Event Display'

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MC_31X_V1::All'
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"


#from FWCore.MessageLogger.MessageLogger_cfi import *
process.MessageLogger = cms.Service("MessageLogger",
                           	destinations = cms.untracked.vstring('cout'),
                            cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
                            )

process.add_(
    cms.Service("IguanaService",
    outputFileName = cms.untracked.string('/home/dqmprolocal/output/iSpy_%d_%s.ig' % (int(dt.date.today().strftime("%W"))+1,dt.date.today().strftime("%Y%m%d"))),
    outputMaxEvents = cms.untracked.int32(3000),
    outputHost = cms.untracked.string('localhost'),
    outputPort = cms.untracked.uint32(9000),
    online = cms.untracked.bool(True),
    debug = cms.untracked.bool(True)
    )
)

process.load("VisReco.Analyzer.VisCaloTower_cfi")
process.load("VisReco.Analyzer.VisCSCSegment_cfi")
process.load('VisReco.Analyzer.VisCSCStripDigi_cfi')
process.load('VisReco.Analyzer.VisCSCWireDigi_cfi')
process.load("VisReco.Analyzer.VisDTRecSegment4D_cfi")
process.load('VisReco.Analyzer.VisDTDigi_cfi')
process.load('VisReco.Analyzer.VisDTRecHit_cfi')
process.load('VisReco.Analyzer.VisRPCRecHit_cfi')
process.load("VisReco.Analyzer.VisEcalRecHit_cfi")
process.load("VisReco.Analyzer.VisEvent_cfi")
process.load("VisReco.Analyzer.VisHBRecHit_cfi")
process.load("VisReco.Analyzer.VisHERecHit_cfi")
process.load("VisReco.Analyzer.VisHFRecHit_cfi")
process.load("VisReco.Analyzer.VisHORecHit_cfi")
process.load("VisReco.Analyzer.VisJet_cfi")
process.load("VisReco.Analyzer.VisMET_cfi")
process.load("VisReco.Analyzer.VisMuon_cfi")
process.load("VisReco.Analyzer.VisPixelDigi_cfi")
process.load("VisReco.Analyzer.VisSiPixelCluster_cfi")
process.load("VisReco.Analyzer.VisSiPixelRecHit_cfi")
process.load("VisReco.Analyzer.VisSiStripCluster_cfi")
process.load("VisReco.Analyzer.VisSiStripDigi_cfi")
process.load("VisReco.Analyzer.VisTrack_cfi")
process.load("VisReco.Analyzer.VisTrackingRecHit_cfi")
process.load('VisReco.Analyzer.VisSimTrack_cfi')
process.load('VisReco.Analyzer.VisTrackingParticle_cfi')
process.load('VisReco.Analyzer.VisTriggerEvent_cfi')
process.load('VisReco.Analyzer.VisL1GlobalTriggerReadoutRecord_cfi')

process.VisCSCSegment.visCSCSegmentTag = cms.InputTag("muonCSCSegments")
process.VisDTRecHit.visDTRecHitTag = cms.InputTag("dt1DRecHits")
process.VisRPCRecHit.visRPCRecHitTag = cms.InputTag("rpcRecHits")
process.VisMET.visMETTag = cms.InputTag('genMetIC5GenJets')
process.VisMuon.visMuonTag = cms.InputTag('muons')
process.VisSiStripDigi.visSiStripDigiTag = cms.InputTag('siStripDigis:ZeroSuppressed')
process.VisTrack.visTrackTag = cms.InputTag('generalTracks')
process.VisTrackingRecHit.visTrackingRecHitTag = cms.InputTag('generalTracks')

process.vis = cms.Path(process.VisEvent*
                       process.VisTrack*
                       process.VisSimTrack*
                       process.VisTrackingRecHit*
                       process.VisCSCSegment*
                       process.VisCSCWireDigi*
                       process.VisCSCStripDigi*
                       process.VisCaloTower*
                       process.VisDTRecSegment4D*
                       process.VisDTDigi*
                       process.VisDTRecHit*
                       process.VisRPCRecHit*
                       process.VisEcalRecHit*
                       process.VisHBRecHit*
                       process.VisHERecHit*
                       process.VisHFRecHit*
                       process.VisHORecHit*
                       process.VisMET*
                       process.VisMuon*
                       process.VisSiPixelCluster*
                       process.VisSiPixelRecHit*
                       process.VisSiStripCluster*
                       process.VisSiStripDigi*
                       process.VisJet*
                       process.VisTrackingParticle*
                       process.VisTriggerEvent*
                       process.VisL1GlobalTriggerReadoutRecord)

process.p3= cms.Path(process.RawToDigi)
process.p4= cms.Path(process.reconstruction)
process.schedule = cms.Schedule(process.p3,process.p4,process.vis)
