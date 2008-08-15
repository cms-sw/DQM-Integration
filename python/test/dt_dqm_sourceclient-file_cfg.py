import FWCore.ParameterSet.Config as cms

process = cms.Process("DTDQM")

# the source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/CRUZET1/BarrelMuon/RAW/v1/000/043/566/30028895-E52C-DD11-BF34-000423D6B444.root',
            '/store/data/CRUZET1/BarrelMuon/RAW/v1/000/043/566/428BAAE4-AA2D-DD11-A2DA-001617C3B710.root',
            '/store/data/CRUZET1/BarrelMuon/RAW/v1/000/043/566/903B66E2-E42C-DD11-AEE7-001617C3B706.root',
            '/store/data/CRUZET1/BarrelMuon/RAW/v1/000/043/566/98FF846A-E52C-DD11-B972-000423D98804.root',
            '/store/data/CRUZET1/BarrelMuon/RAW/v1/000/043/566/EC672090-E52C-DD11-8328-000423D6CA02.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

process.load("DQMServices.Core.DQM_cfg")

# official DQMCollector
# srv-c2d05-16
process.DQM.collectorHost = 'localhost'
# 9090
process.DQM.collectorPort = 9190

################# BEGIN DQM Online Environment #######################
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.dqmSaver.convention = "Online"
# /cms/mon/data/dropbox
process.dqmSaver.dirName = "."
process.dqmSaver.producer = "Playback"
process.dqmSaver.saveByRun         =  1
process.dqmSaver.saveAtJobEnd      = True

process.dqmEnv.subSystemFolder = "DT"

process.load("DQM.Integration.test.dt_dqm_sourceclient_common_cff")



# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
                                    )


process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)

process.dtDQMPath = cms.Path(process.calibrationEventsFilter * process.dqmmodules + process.reco + process.dtDQMTask + process.dtDQMTest)


