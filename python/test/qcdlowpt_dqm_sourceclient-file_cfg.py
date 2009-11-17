# $Id:$

import FWCore.ParameterSet.Config as cms

process = cms.Process("QcdLowPtDQM")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('DQM/Physics/qcdLowPtDQM_cfi')

process.GlobalTag.globaltag = 'GR09_P_V5::All'

process.dqmSaver.workflow = cms.untracked.string('/Physics/QCD/LowPt')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.dump = cms.EDAnalyzer('EventContentAnalyzer')

process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring(
        'file:/opt/data/cms/CMSSW_3_3_2/Data.00120962.0057.A.storageManager.04.0001.dat'
    )
)				      

process.p = cms.Path(
#    process.dump *
    process.myRecoSeq1  *
    process.dump *
    process.myRecoSeq2  *
#    process.dump *
    process.QcdLowPtDQM +
    process.dqmSaver
)

process.DQM.collectorHost = ''

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


