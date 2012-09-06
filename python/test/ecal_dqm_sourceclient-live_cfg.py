import FWCore.ParameterSet.Config as cms
import os, sys, socket

process = cms.Process("DQM")


### RECONSTRUCTION MODULES ###

process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")

process.load("Geometry.CaloEventSetup.CaloTopology_cfi")

process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("Geometry.EcalMapping.EcalMapping_cfi")

process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

from EventFilter.EcalRawToDigi.EcalUnpackerData_cfi import ecalEBunpacker
process.ecalDigis = ecalEBunpacker.clone()

process.load("RecoLocalCalo.EcalRecProducers.ecalGlobalUncalibRecHit_cfi")

process.load("RecoLocalCalo.EcalRecProducers.ecalDetIdToBeRecovered_cfi")

process.load("RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi")

process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")

process.load("RecoEcal.EgammaClusterProducers.ecalClusteringSequence_cff")

process.load("CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi")

process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_cfi")

process.load("EventFilter.L1GlobalTriggerRawToDigi.l1GtEvmUnpack_cfi")

    
### ECAL DQM MODULES ###

process.load("DQM.EcalBarrelMonitorModule.EcalBarrelMonitorModule_cfi")
process.load("DQM.EcalEndcapMonitorModule.EcalEndcapMonitorModule_cfi")
process.load("DQM.EcalBarrelMonitorTasks.EcalBarrelMonitorTasks_cfi")
process.load("DQM.EcalEndcapMonitorTasks.EcalEndcapMonitorTasks_cfi")

process.load("DQM.EcalBarrelMonitorTasks.EBTrendTask_cfi")
process.load("DQM.EcalBarrelMonitorClient.EBTrendClient_cfi")
process.load("DQM.EcalEndcapMonitorTasks.EETrendTask_cfi")
process.load("DQM.EcalEndcapMonitorClient.EETrendClient_cfi")

process.load("DQM.EcalBarrelMonitorClient.EcalBarrelMonitorClient_cfi")
process.load("DQM.EcalEndcapMonitorClient.EcalEndcapMonitorClient_cfi")


### DQM COMMON MODULES ###

process.load("DQMServices.Core.DQM_cfg")

process.dqmQTestEB = cms.EDAnalyzer("QualityTester",
  reportThreshold = cms.untracked.string("red"),
  prescaleFactor = cms.untracked.int32(1),
  qtList = cms.untracked.FileInPath("DQM/EcalBarrelMonitorModule/test/data/EcalBarrelQualityTests.xml"),
  getQualityTestsFromFile = cms.untracked.bool(True),
  qtestOnEndLumi = cms.untracked.bool(True),
  qtestOnEndRun = cms.untracked.bool(True)
)
process.dqmQTestEE = cms.EDAnalyzer("QualityTester",
  reportThreshold = cms.untracked.string("red"),
  prescaleFactor = cms.untracked.int32(1),
  qtList = cms.untracked.FileInPath("DQM/EcalEndcapMonitorModule/test/data/EcalEndcapQualityTests.xml"),
  getQualityTestsFromFile = cms.untracked.bool(True),
  qtestOnEndLumi = cms.untracked.bool(True),
  qtestOnEndRun = cms.untracked.bool(True)
)

process.load("DQM.Integration.test.environment_cfi")
process.dqmEnvEB = process.dqmEnv.clone()
process.dqmEnvEE = process.dqmEnv.clone()


### FILTERS ###

process.load("FWCore.Modules.preScaler_cfi")

process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")

process.ecalPhysicsFilter = cms.EDFilter("EcalMonitorPrescaler")



### JOB PARAMETERS ###

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(-1)
)

process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(
        record = cms.string("EcalDQMChannelStatusRcd"),
        tag = cms.string("EcalDQMChannelStatus_v1_hlt"),
        connect = cms.untracked.string("frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_34X_ECAL")
    ),
    cms.PSet(
        record = cms.string("EcalDQMTowerStatusRcd"),
        tag = cms.string("EcalDQMTowerStatus_v1_hlt"),
        connect = cms.untracked.string("frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_34X_ECAL")
    )
)


### MESSAGE LOGGER ###

process.MessageLogger = cms.Service("MessageLogger",
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string("WARNING"),
    noLineBreaks = cms.untracked.bool(True),
    noTimeStamps = cms.untracked.bool(True),
    default = cms.untracked.PSet(
      limit = cms.untracked.int32(0)
    )
  ),
  destinations = cms.untracked.vstring("cout")
)


### SEQUENCES AND PATHS ###

process.ecalPreRecoSequence = cms.Sequence(
    process.preScaler +
#    process.hltTriggerTypeFilter +
    process.ecalDigis
)

process.ecalRecoSequence = cms.Sequence(
    process.ecalGlobalUncalibRecHit *
    process.ecalDetIdToBeRecovered *
    process.ecalRecHit
)

process.ecalClusterSequence = cms.Sequence(
    process.hybridClusteringSequence +
    process.multi5x5ClusteringSequence
)
process.ecalClusterSequence.remove(process.multi5x5SuperClustersWithPreshower)

process.ecalMonitorBaseSequence = cms.Sequence(
    process.ecalBarrelMonitorModule +
    process.ecalEndcapMonitorModule +
    process.ecalBarrelOccupancyTask +
    process.ecalBarrelIntegrityTask +
    process.ecalEndcapOccupancyTask +
    process.ecalEndcapIntegrityTask +
    process.ecalBarrelStatusFlagsTask +
    process.ecalBarrelRawDataTask +
    process.ecalEndcapStatusFlagsTask +
    process.ecalEndcapRawDataTask +
    process.ecalBarrelPedestalOnlineTask +
    process.ecalEndcapPedestalOnlineTask
)

process.ecalMonitorSequence = cms.Sequence(
    process.ecalBarrelTrendTask +
    process.ecalEndcapTrendTask +
    process.ecalBarrelCosmicTask +
    process.ecalBarrelClusterTask +
    process.ecalBarrelTriggerTowerTask +
    process.ecalBarrelTimingTask +
    process.ecalBarrelSelectiveReadoutTask +
    process.ecalEndcapCosmicTask +
    process.ecalEndcapClusterTask +
    process.ecalEndcapTriggerTowerTask +
    process.ecalEndcapTimingTask +
    process.ecalEndcapSelectiveReadoutTask
)

process.ecalMonitorPath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalPhysicsFilter *
    process.ecalRecoSequence *
    (
    process.ecalClusterSequence +
    process.l1GtEvmUnpack +    
    process.simEcalTriggerPrimitiveDigis
    ) *
    (
    process.ecalMonitorBaseSequence +
    process.ecalMonitorSequence
    )
)

process.ecalClientPath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalPhysicsFilter +
    process.ecalBarrelTrendClient +
    process.ecalEndcapTrendClient +
    process.ecalBarrelMonitorClient +
    process.ecalEndcapMonitorClient
)

process.ecalMonitorEndPath = cms.EndPath(
    process.dqmEnvEB +
    process.dqmEnvEE +
    process.dqmQTestEB +
    process.dqmQTestEE
)
process.dqmEndPath = cms.EndPath(
    process.dqmSaver
)

process.schedule = cms.Schedule(
    process.ecalMonitorPath,
    process.ecalClientPath,
    process.ecalMonitorEndPath,
    process.dqmEndPath
)


### SOURCE ###

process.load("DQM.Integration.test.inputsource_cfi")


### CUSTOMIZATIONS ###

 ## Reconstruction Modules ##

process.ecalRecHit.killDeadChannels = True
process.ecalRecHit.ChannelStatusToBeExcluded = [ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 78, 142 ]

process.simEcalTriggerPrimitiveDigis.Label = "ecalDigis"
process.simEcalTriggerPrimitiveDigis.InstanceEB = "ebDigis"
process.simEcalTriggerPrimitiveDigis.InstanceEE = "eeDigis"

 ## Filters ##

process.ecalPhysicsFilter.EcalRawDataCollection = cms.InputTag("ecalDigis")
process.ecalPhysicsFilter.clusterPrescaleFactor = cms.untracked.int32(1)

process.hltTriggerTypeFilter.SelectedTriggerType = 1 # 0=random, 1=physics, 2=calibration, 3=technical

 ## Ecal DQM modules ##

process.ecalBarrelMonitorClient.enabledClients = ["Integrity", "StatusFlags", "Occupancy", "PedestalOnline", "Timing", "Cosmic", "TriggerTower", "Cluster", "Summary"]
process.ecalEndcapMonitorClient.enabledClients = ["Integrity", "StatusFlags", "Occupancy", "PedestalOnline", "Timing", "Cosmic", "TriggerTower", "Cluster", "Summary"]

process.ecalBarrelMonitorClient.reducedReports = False
process.ecalEndcapMonitorClient.reducedReports = False

process.ecalBarrelTimingTask.useBeamStatus = cms.untracked.bool(True)
process.ecalEndcapTimingTask.useBeamStatus = cms.untracked.bool(True)

process.ecalBarrelMonitorClient.location = "P5_Co"
process.ecalEndcapMonitorClient.location = "P5_Co"
process.ecalBarrelMonitorClient.verbose = False
process.ecalEndcapMonitorClient.verbose = False

process.ecalBarrelMonitorClient.updateTime = 4
process.ecalEndcapMonitorClient.updateTime = 4

 ## DQM common modules ##

process.dqmEnvEB.subSystemFolder = cms.untracked.string("EcalBarrel")
process.dqmEnvEE.subSystemFolder = cms.untracked.string("EcalEndcap")

process.DQMStore.referenceFileName = "/dqmdata/dqm/reference/ecal_reference.root"

 ## Source ##
process.source.consumerName = cms.untracked.string("Ecal DQM Consumer")

 ## Run type specific ##

if process.runType.getRunType() == process.runType.cosmic_run :
    process.ecalMonitorEndPath.remove(process.dqmQTestEB)
    process.ecalMonitorEndPath.remove(process.dqmQTestEE)
elif process.runType.getRunType() == process.runType.hpu_run:
    process.source.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("*"))

 ## FEDRawDataCollection name ##
FedRawData = "rawDataCollector"

if process.runType.getRunType() == process.runType.hi_run:
    FedRawData = "rawDataRepacker"

process.ecalDigis.InputLabel = cms.InputTag(FedRawData)

process.ecalBarrelRawDataTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.ecalEndcapRawDataTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.ecalBarrelSelectiveReadoutTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.ecalEndcapSelectiveReadoutTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.l1GtEvmUnpack.EvmGtInputTag = cms.InputTag(FedRawData)
process.ecalBarrelTrendTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.ecalEndcapTrendTask.FEDRawDataCollection = cms.InputTag(FedRawData)
