import FWCore.ParameterSet.Config as cms
import socket
maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
source = cms.Source("EventStreamHttpReader",
    #General porpouse SMProxy Server
    #sourceURL = cms.string('http://dqm-c2d07-30.cms:22100/urn:xdaq-application:lid=30'),
    
    #SMPlayback Server
    #sourceURL = cms.string('http://dqm-c2d07-30:50082/urn:xdaq-application:lid=29'),
    
    #local SMProxy Serve
    sourceURL = cms.string('http://%s:22100/urn:xdaq-application:lid=30' % socket.gethostname()),
    
    #Storage Manager
    #sourceURL = cms.string('http://srv-c2c06-13.cms:11100/urn:xdaq-application:lid=50'),
    consumerPriority = cms.untracked.string('normal'),
    max_event_size = cms.int32(7000000),
    consumerName = cms.untracked.string('DQM Source'),
    SelectHLTOutput = cms.untracked.string('hltOutputDQM'),
    max_queue_depth = cms.int32(5),
    maxEventRequestRate = cms.untracked.double(10.0),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('*')
    ),
    headerRetryInterval = cms.untracked.int32(3),
    dropOldLumisectionEvents = cms.untracked.bool(True)
)


