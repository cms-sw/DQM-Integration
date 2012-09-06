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

from RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi import ecalFixedAlphaBetaFitUncalibRecHit
process.ecalLaserLedUncalibRecHit = ecalFixedAlphaBetaFitUncalibRecHit.clone()

from RecoLocalCalo.EcalRecProducers.ecalMaxSampleUncalibRecHit_cfi import ecalMaxSampleUncalibRecHit
process.ecalTestPulseUncalibRecHit = ecalMaxSampleUncalibRecHit.clone()

    
### ECAL DQM MODULES ###

process.load("DQM.EcalBarrelMonitorModule.EcalBarrelMonitorModule_cfi")
process.load("DQM.EcalEndcapMonitorModule.EcalEndcapMonitorModule_cfi")
process.load("DQM.EcalBarrelMonitorTasks.EcalBarrelMonitorTasks_cfi")
process.load("DQM.EcalEndcapMonitorTasks.EcalEndcapMonitorTasks_cfi")

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

process.ecalCalibrationFilter = cms.EDFilter("EcalMonitorPrescaler")
process.ecalLaserLedFilter = cms.EDFilter("EcalMonitorPrescaler")
process.ecalTestPulseFilter = cms.EDFilter("EcalMonitorPrescaler")


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

process.ecalLaserLedPath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalLaserLedFilter *    
    process.ecalRecoSequence *
    process.ecalLaserLedUncalibRecHit *
    (
    process.ecalMonitorBaseSequence +
    process.ecalBarrelLaserTask +
    process.ecalEndcapLaserTask +
    process.ecalEndcapLedTask
    )
)

process.ecalTestPulsePath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalTestPulseFilter *    
    process.ecalRecoSequence *
    process.ecalTestPulseUncalibRecHit *
    (
    process.ecalMonitorBaseSequence +    
    process.ecalBarrelTestPulseTask +
    process.ecalEndcapTestPulseTask
    )
)

process.ecalClientPath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalCalibrationFilter +
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
    process.ecalLaserLedPath,
    process.ecalTestPulsePath,
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

process.ecalTestPulseUncalibRecHit.EBdigiCollection = "ecalDigis:ebDigis"
process.ecalTestPulseUncalibRecHit.EEdigiCollection = "ecalDigis:eeDigis"
    
process.ecalLaserLedUncalibRecHit.MinAmplBarrel = 12.
process.ecalLaserLedUncalibRecHit.MinAmplEndcap = 16.

 ## Filters ##

process.ecalCalibrationFilter.EcalRawDataCollection = cms.InputTag("ecalDigis")
process.ecalCalibrationFilter.laserPrescaleFactor = cms.untracked.int32(1)
process.ecalCalibrationFilter.ledPrescaleFactor = cms.untracked.int32(1)
process.ecalCalibrationFilter.pedestalPrescaleFactor = cms.untracked.int32(1)
process.ecalCalibrationFilter.testpulsePrescaleFactor = cms.untracked.int32(1)

process.ecalLaserLedFilter.EcalRawDataCollection = cms.InputTag("ecalDigis")
process.ecalLaserLedFilter.laserPrescaleFactor = cms.untracked.int32(1)
process.ecalLaserLedFilter.ledPrescaleFactor = cms.untracked.int32(1)

process.ecalTestPulseFilter.EcalRawDataCollection = cms.InputTag("ecalDigis")
process.ecalTestPulseFilter.testpulsePrescaleFactor = cms.untracked.int32(1)

process.hltTriggerTypeFilter.SelectedTriggerType = 2 # 0=random, 1=physics, 2=calibration, 3=technical

 ## Ecal DQM modules ##

process.ecalBarrelLaserTask.EcalUncalibratedRecHitCollection = "ecalLaserLedUncalibRecHit:EcalUncalibRecHitsEB"
process.ecalBarrelTestPulseTask.EcalUncalibratedRecHitCollection = "ecalTestPulseUncalibRecHit:EcalUncalibRecHitsEB"
process.ecalEndcapLaserTask.EcalUncalibratedRecHitCollection = "ecalLaserLedUncalibRecHit:EcalUncalibRecHitsEE"
process.ecalEndcapLedTask.EcalUncalibratedRecHitCollection = "ecalLaserLedUncalibRecHit:EcalUncalibRecHitsEE"
process.ecalEndcapTestPulseTask.EcalUncalibratedRecHitCollection = "ecalTestPulseUncalibRecHit:EcalUncalibRecHitsEE"

process.ecalBarrelLaserTask.laserWavelengths = [ 1, 2, 3, 4 ]
process.ecalEndcapLaserTask.laserWavelengths = [ 1, 2, 3, 4 ]
process.ecalEndcapLedTask.ledWavelengths = [ 1, 2 ]
process.ecalBarrelMonitorClient.laserWavelengths = [ 1, 2, 3, 4 ]
process.ecalEndcapMonitorClient.laserWavelengths = [ 1, 2, 3, 4 ]
process.ecalEndcapMonitorClient.ledWavelengths = [ 1, 2 ]

process.ecalBarrelMonitorClient.enabledClients = ["Integrity", "StatusFlags", "Occupancy", "PedestalOnline", "TestPulse", "Laser", "Summary"]
process.ecalEndcapMonitorClient.enabledClients = ["Integrity", "StatusFlags", "Occupancy", "PedestalOnline", "TestPulse", "Laser", "Led", "Summary"]

process.ecalBarrelMonitorClient.produceReports = False
process.ecalEndcapMonitorClient.produceReports = False

process.ecalBarrelTestPulseTask.MGPAGains = [ 12 ]
process.ecalBarrelTestPulseTask.MGPAGainsPN = [ 16 ]
process.ecalEndcapTestPulseTask.MGPAGains = [ 12 ]
process.ecalEndcapTestPulseTask.MGPAGainsPN = [ 16 ]
process.ecalBarrelMonitorClient.MGPAGains = [ 12 ]
process.ecalBarrelMonitorClient.MGPAGainsPN = [ 16 ]
process.ecalEndcapMonitorClient.MGPAGains = [ 12 ]
process.ecalEndcapMonitorClient.MGPAGainsPN = [ 16 ]

process.ecalBarrelMonitorClient.location = "P5_Co"
process.ecalEndcapMonitorClient.location = "P5_Co"
process.ecalBarrelMonitorClient.verbose = False
process.ecalEndcapMonitorClient.verbose = False

process.ecalBarrelMonitorClient.updateTime = 4
process.ecalEndcapMonitorClient.updateTime = 4

 ## DQM common modules ##

process.dqmEnvEB.subSystemFolder = cms.untracked.string("EcalBarrel/Calibration")
process.dqmEnvEE.subSystemFolder = cms.untracked.string("EcalEndcap/Calibration")

process.DQMStore.referenceFileName = "/dqmdata/dqm/reference/ecalcalib_reference.root"

 ## Source ##
process.source.consumerName = cms.untracked.string("EcalCalibration DQM Consumer")
process.source.SelectHLTOutput = cms.untracked.string("hltOutputCalibration")
process.source.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("HLT_EcalCalibration_v*"))

 ## Run type specific ##

if process.runType.getRunType() == process.runType.cosmic_run :
    process.ecalMonitorEndPath.remove(process.dqmQTestEB)
    process.ecalMonitorEndPath.remove(process.dqmQTestEE)
elif process.runType.getRunType() == process.runType.hpu_run:
    process.source.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("*"))

 ## FEDRawDataCollection name ##
FedRawData = "hltEcalCalibrationRaw"

process.ecalDigis.InputLabel = cms.InputTag(FedRawData)

process.ecalBarrelRawDataTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.ecalEndcapRawDataTask.FEDRawDataCollection = cms.InputTag(FedRawData)

 ## Avoid plot name clashes ##
process.ecalBarrelIntegrityTask.subfolder = "Calibration"
process.ecalBarrelOccupancyTask.subfolder = "Calibration"
process.ecalBarrelStatusFlagsTask.subfolder = "Calibration"
process.ecalBarrelRawDataTask.subfolder = "Calibration"
process.ecalBarrelPedestalOnlineTask.subfolder = "Calibration"
process.ecalEndcapIntegrityTask.subfolder = "Calibration"
process.ecalEndcapOccupancyTask.subfolder = "Calibration"
process.ecalEndcapStatusFlagsTask.subfolder = "Calibration"
process.ecalEndcapRawDataTask.subfolder = "Calibration"
process.ecalEndcapPedestalOnlineTask.subfolder = "Calibration"
process.ecalBarrelMonitorClient.subfolder = "Calibration"
process.ecalEndcapMonitorClient.subfolder = "Calibration"
