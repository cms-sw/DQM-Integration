import FWCore.ParameterSet.Config as cms
import datetime as dt
import socket
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
process.EventStreamHttpReader.consumerName = 'ISpy Event Display wide selection'
process.EventStreamHttpReader.SelectHLTOutput = cms.untracked.string('hltOutputDQM')
process.EventStreamHttpReader.sourceURL=cms.string('http://dqm-c2d07-30:22100/urn:xdaq-application:lid=30')

####### DQM Default File Location
process.load("DQM.Integration.test.environment_cfi")
if process.dqmSaver.producer.value() == "DQM":
  igFileOutput=False
  igDebug=False
else:
  igFileOutput=False
  igDebug=True
####### ISpy Service
process.add_(cms.Service("ISpyService",
    outputFileName = cms.untracked.string('%s/iSpy_%s%d_%s__hltOutputDQMWide_.ig' % (process.dqmSaver.dirName.value(),BaseName,int(dt.date.today().strftime("%W"))+1,dt.date.today().strftime("%Y%m%d"))),
    #outputFileName = cms.untracked.string('/home/lilopera/CMSSW/output/iSpy_MWGR%d_%s__hltOutputDQM_.ig' % (int(dt.date.today().strftime("%W"))+1,dt.date.today().strftime("%Y%m%d"))),
    outputESFileName=cms.untracked.string('/tmp/iSpy_ES.ig'),
    bufferSize = cms.untracked.uint32(1),
    outputHost = cms.untracked.string('localhost'),
    outputPort = cms.untracked.uint32(9001),
    outputMaxEvents = cms.untracked.int32(100),
    outputMaxTime = cms.untracked.int32(600),
    outputIg = cms.untracked.bool(igFileOutput),
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
process.ISpyTrackingRecHit.iSpyTrackingRecHitTag = cms.InputTag('generalTracks')
process.ISpyTrack.iSpyTrackTags = cms.VInputTag(cms.InputTag('cosmicMuons'),
                                                cms.InputTag('cosmictrackfinderP5'),
                                                cms.InputTag('generalTracks')
                                               )

####### Trigger Filters for physics events
#process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
# 0=random, 1=physics, 2=calibration, 3=technical
#process.hltTriggerTypeFilter.SelectedTriggerType = 1

####### Path
if Cosmics:
  process.p= cms.Path(#process.hltTriggerTypeFilter*
                     process.RawToDigi*
                     process.reconstructionCosmics*
                     process.iSpy_online_sequence
                    )
else:
  process.p= cms.Path(#process.hltTriggerTypeFilter*
                     process.RawToDigi*
                     process.reconstruction_withPixellessTk*
                     process.iSpy_online_sequence
                    )
