# $Id: physics_dqm_sourceclient_live.py,v 1.1 2009/11/17 09:39:42 ameyer Exp $

import FWCore.ParameterSet.Config as cms

process = cms.Process("Physics")

#----------------------------
# Event Source
#-----------------------------

process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'Physics DQM Consumer'
#process.EventStreamHttpReader.sourceURL = "http://localhost:50082/urn:xdaq-application:lid=29"

#----------------------------
# DQM Environment
#-----------------------------

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'Physics'

#---- for P5 (online) DB access
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
#---- for offline DB ----

process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('DQM/Physics/qcdLowPtDQM_cfi')

#process.dump = cms.EDAnalyzer('EventContentAnalyzer')

process.p = cms.Path(
#    process.dump *
    process.myRecoSeq1  *
#    process.dump *
    process.myRecoSeq2  *
#    process.dump *
    process.QcdLowPtDQM +
    process.dqmSaver
)

#process.DQM.collectorHost = ''

#process.DQMStore.verbose = 0
#process.DQM.collectorHost = "srv-c2d05-12"
#process.DQM.collectorPort = 9190
#process.DQMStore.referenceFileName = "DQM_L1T_R000002467.root"
#process.DQMStore.referenceFileName = "/nfshome0/wteo/test/rctL1tDqm.root"
#process.DQMStore.verbose = 0
#process.dqmSaver.convention = 'Online'
#process.dqmSaver.dirName = '.'
#process.dqmSaver.producer = 'DQM'
#process.dqmEnv.subSystemFolder = 'L1T'
#process.dqmSaver.saveByRun = 1
#process.dqmSaver.saveAtJobEnd = True


