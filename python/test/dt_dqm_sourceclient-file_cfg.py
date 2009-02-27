import FWCore.ParameterSet.Config as cms

process = cms.Process("DTDQM")

# the source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/00482DCA-E1A4-DD11-99CB-001D09F2905B.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/004C4F06-DAA4-DD11-847F-001D09F2538E.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/00B2D109-B2A4-DD11-AB2D-001D09F2545B.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/00CC94F4-9EA4-DD11-BEA6-000423D94E1C.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0237302E-B2A4-DD11-811F-001D09F23A61.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/025D2244-DEA4-DD11-B8EE-001D09F248F8.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/02678F75-DBA4-DD11-892A-0030487A18A4.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0442F938-EAA4-DD11-8021-0030487C5CFA.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/04F75E9E-ABA4-DD11-BA2D-001617C3B5E4.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/068D48FD-DEA4-DD11-AD45-001D09F23A34.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/08B4E9E7-E3A4-DD11-A6EB-001D09F2538E.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/08CF25A2-BEA4-DD11-AFC8-000423D944DC.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0A0EF467-99A4-DD11-8E4C-000423D98844.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0C0A961B-E1A4-DD11-BCA1-000423D94E1C.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0C193B71-9BA4-DD11-A5F6-000423D6B42C.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0C62B2AA-8DA4-DD11-865D-000423D99AAA.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0C94ADC2-EDA4-DD11-9B86-001D09F28D4A.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0CD684DF-7BA4-DD11-AA29-000423D996B4.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0E8DC352-D9A4-DD11-B9F6-001D09F2525D.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0EC04BBE-DAA4-DD11-AD62-001617C3B73A.root',
    '/store/data/Commissioning08/Calo/RAW/v1/000/067/818/0EDA3B28-A3A4-DD11-BA01-001617E30CA4.root'
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
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
process.dqmSaver.producer = "DQM"
process.dqmSaver.saveByRun         =  1
process.dqmSaver.saveAtJobEnd      = True

process.dqmEnv.subSystemFolder = "DT"

process.load("Configuration.StandardSequences.Geometry_cff")
process.load("DQM.DTMonitorModule.dt_dqm_sourceclient_common_cff")
#---- for P5 (online) DB access
#process.GlobalTag.connect ="frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"
#process.GlobalTag.globaltag = "CRAFT_V4H::All"
#---- for offline DB
process.GlobalTag.globaltag = "CRAFT_ALL_V9::All"


# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    debugModules = cms.untracked.vstring('*'),
                                    destinations = cms.untracked.vstring('cout'),
                                    categories = cms.untracked.vstring('DTSegmentAnalysisTask'), 
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'),
                                                              noLineBreaks = cms.untracked.bool(False),
                                                              DEBUG = cms.untracked.PSet(
                                                                      limit = cms.untracked.int32(0)),
                                                              INFO = cms.untracked.PSet(
                                                                      limit = cms.untracked.int32(0)),
                                                              DTSegmentAnalysisTask = cms.untracked.PSet(
                                                                                 limit = cms.untracked.int32(-1))
                                                              )
                                    )


process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)


process.dtDQMPathPhys = cms.Path(process.unpackers + process.dqmmodules + process.physicsEventsFilter * process.reco + process.dtDQMTask + process.dtDQMTest)

#process.dtDQMPathCalib = cms.Path(process.unpackers + process.dqmmodules + process.calibrationEventsFilter * process.dtDQMCalib)

# f = file('aNewconfigurationFile.cfg', 'w')
# f.write(process.dumpConfig())
# f.close()

process.options = cms.untracked.PSet(
    fileMode = cms.untracked.string('FULLMERGE')
    )


