import FWCore.ParameterSet.Config as cms

process = cms.Process("hlxdqmlive")

from FWCore.MessageLogger.MessageLogger_cfi import *

## Input source
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'HLX DQM Consumer'

## HLX configuration
process.load("DQM.HLXMonitor.hlx_dqm_sourceclient_cfi")

## Set up env and saver
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder    = "HLX"

## Lumi reference file
process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/hlx_reference.root'

process.hlxQualityTester = cms.EDFilter("QualityTester",
    # default is 1
    prescaleFactor = cms.untracked.int32(10000),
    # use eventloop for testing only ! default is false
    # untracked bool testInEventloop = false
    # use qtest on endRun or endJob
    # untracked bool qtestOnEndRun = false
    # untracked bool qtestOnEndJob = false
    qtList = cms.untracked.FileInPath('DQM/HLXMonitor/test/HLXQualityTests.xml')
)

process.p = cms.Path(process.hlxdqmsource*process.hlxQualityTester*process.dqmEnv*process.dqmSaver)

## Shouldn't need this anymore ...
##process.hlxdqmsource.outputDir = process.dqmSaver.dirName


