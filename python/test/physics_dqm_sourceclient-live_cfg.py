# $Id: physics_dqm_sourceclient-live_cfg.py,v 1.2 2009/11/19 17:04:15 ameyer Exp $

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

process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_AutoFromDBCurrent_cff')
process.load('DQM/Physics/qcdLowPtDQM_cfi')

#process.dump = cms.EDAnalyzer('EventContentAnalyzer')

process.p = cms.Path(
    process.myRecoSeq1  *
    process.myRecoSeq2  *
#    process.dump *
    process.QcdLowPtDQM *
    process.dqmEnv *
    process.dqmSaver
)
