import FWCore.ParameterSet.Config as cms

process = cms.Process("DTDQM")

# the source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/data/Commissioning08/Monitor/RAW/v1/000/066/286/02FDBCC0-B89A-DD11-97E3-000423D94700.root',
        '/store/data/Commissioning08/Monitor/RAW/v1/000/066/286/3A83F71C-B99A-DD11-B040-000423D6CA42.root',
        '/store/data/Commissioning08/Monitor/RAW/v1/000/066/286/84904CC1-B89A-DD11-BCEC-000423D6CA02.root',
        '/store/data/Commissioning08/Monitor/RAW/v1/000/066/286/9AF0CFBD-B89A-DD11-A763-000423D992DC.root',
        '/store/data/Commissioning08/Monitor/RAW/v1/000/066/286/B472EDD1-B89A-DD11-A3C2-001617C3B6CC.root',
        '/store/data/Commissioning08/Monitor/RAW/v1/000/066/286/E2F292EC-C29A-DD11-A9AA-000423D6AF24.root'
    )
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
#process.DTDataIntegrityTask.debug = True


# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    debugModules = cms.untracked.vstring('*'),
                                    destinations = cms.untracked.vstring('cout'),
                                    categories = cms.untracked.vstring('DTOccupancyTest'), 
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'),
                                                              noLineBreaks = cms.untracked.bool(False),
                                                              DEBUG = cms.untracked.PSet(
                                                                      limit = cms.untracked.int32(0)),
                                                              INFO = cms.untracked.PSet(
                                                                      limit = cms.untracked.int32(0)),
                                                              DTOccupancyTest = cms.untracked.PSet(
                                                                                 limit = cms.untracked.int32(100000000))
                                                              )
                                    )


process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)


process.dtDQMPathPhys = cms.Path(process.unpackers + process.dqmmodules + process.physicsEventsFilter * process.reco + process.dtDQMTask + process.dtDQMTest)

#process.dtDQMPathCalib = cms.Path(process.unpackers + process.dqmmodules + process.calibrationEventsFilter * process.dtDQMCalib)

# f = file('aNewconfigurationFile.cfg', 'w')
# f.write(process.dumpConfig())
# f.close()


