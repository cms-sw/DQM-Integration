import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("DQMServices.Core.DQM_cfg")

process.load("DQM.HLTEvF.HLTMonitor_cff")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(100)
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    debugVerbosity = cms.untracked.uint32(1),
    debugVebosity = cms.untracked.bool(True),
    fileNames = cms.untracked.vstring('/store/data/Commissioning08/HLTDebug/RAW/CRUZET4_v1/000/058/042/0ECC6BE3-5F6F-DD11-A328-0019DB29C614.root')
)
#process.source = cms.Source("NewEventStreamFileReader",
#    fileNames = cms.untracked.vstring('file:/data1/lookarea/GlobalAug07.00017220.0001.A.storageManager.0.0000.dat')
#)

process.tsumm = cms.EDAnalyzer("TriggerSummaryAnalyzerAOD")
process.tsumm.inputTag = cms.InputTag("hltTriggerSummaryAOD","","HLT")

process.hltrep = cms.EDAnalyzer("HLTrigReport")
process.hltrep.HLTriggerResults = cms.InputTag("TriggerResults","","HLT")
process.ptsum = cms.Path(process.tsumm+process.hltrep)

process.p = cms.EndPath(process.hlts+process.hltsClient)


process.pp = cms.Path(process.dqmEnv+process.dqmSaver)
process.DQMStore.verbose = 0
process.DQM.collectorHost = 'srv-c2d05-16'
process.DQM.collectorPort = 9090
process.dqmSaver.dirName = '.'
process.dqmSaver.producer = 'Playback'
process.hltResults.plotAll = True
process.dqmSaver.convention = 'Online'
process.dqmEnv.subSystemFolder = 'HLT'
process.dqmSaver.saveByRun = 1
process.dqmSaver.saveAtJobEnd = True

# # Message Logger
# process.load("FWCore.MessageService.MessageLogger_cfi")
# #process.MessageLogger.categories = ['hltResults']
# process.MessageLogger.destinations = ['cout', 'detailedInfo', 'critical']
# process.MessageLogger.cout = cms.untracked.PSet(
#     #threshold = cms.untracked.string('ERROR'),
#     #threshold = cms.untracked.string('INFO'),
#     #INFO = cms.untracked.PSet(
#     # limit = cms.untracked.int32(-1)
#     #)#,
#     threshold = cms.untracked.string('DEBUG'),
#     DEBUG = cms.untracked.PSet(
#     limit = cms.untracked.int32(-1) ## DEBUG, all messages
#     )
#     )
# process.MessageLogger.categories = ['Status', 'Parameter']
# # copy stdout to a file
# process.MessageLogger.detailedInfo = process.MessageLogger.cout
# process.MessageLogger.debugModules = ['hltResults']
# process.MessageLogger.critical = cms.untracked.PSet(
#     threshold = cms.untracked.string('ERROR'),
#     #threshold = cms.untracked.string('INFO'),
#     #INFO = cms.untracked.PSet(
#     # limit = cms.untracked.int32(-1)
#     #)#,
#     #threshold = cms.untracked.string('DEBUG'),
#     ERROR = cms.untracked.PSet(
#     limit = cms.untracked.int32(-1) ## all messages
#     )
#     )
# # summary
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )
