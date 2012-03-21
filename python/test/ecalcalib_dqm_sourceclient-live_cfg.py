import FWCore.ParameterSet.Config as cms
import os, sys, socket

process = cms.Process("DQM")


### RECONSTRUCTION MODULES ###

process.load("EventFilter.EcalRawToDigi.EcalUnpackerMapping_cfi")

process.load("EventFilter.EcalRawToDigi.EcalUnpackerData_cfi")

import RecoLocalCalo.EcalRecProducers.ecalGlobalUncalibRecHit_cfi
process.ecalUncalibHit = RecoLocalCalo.EcalRecProducers.ecalGlobalUncalibRecHit_cfi.ecalGlobalUncalibRecHit.clone()

process.load("RecoLocalCalo.EcalRecProducers.ecalDetIdToBeRecovered_cfi")

process.load("RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi")

process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")

process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")

process.load("Geometry.CaloEventSetup.CaloTopology_cfi")

process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("Geometry.EcalMapping.EcalMapping_cfi")

process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

process.load("RecoEcal.EgammaClusterProducers.ecalClusteringSequence_cff")

process.load("CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi")

process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_cfi")

process.load("EventFilter.L1GlobalTriggerRawToDigi.l1GtEvmUnpack_cfi")

import RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi
process.ecalUncalibHit1 = RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi.ecalFixedAlphaBetaFitUncalibRecHit.clone()

import RecoLocalCalo.EcalRecProducers.ecalMaxSampleUncalibRecHit_cfi
process.ecalUncalibHit2 = RecoLocalCalo.EcalRecProducers.ecalMaxSampleUncalibRecHit_cfi.ecalMaxSampleUncalibRecHit.clone()


### ECAL DQM MODULES ###

process.load("DQM.EcalBarrelMonitorModule.EcalBarrelMonitorModule_cfi")
process.load("DQM.EcalEndcapMonitorModule.EcalEndcapMonitorModule_cfi")
process.load("DQM.EcalBarrelMonitorTasks.EcalBarrelMonitorTasks_cfi")
process.load("DQM.EcalEndcapMonitorTasks.EcalEndcapMonitorTasks_cfi")

process.load("DQM.EcalBarrelMonitorTasks.EBTrendTask_cfi")
process.load("DQM.EcalBarrelMonitorClient.EBTrendClient_cfi")
process.load("DQM.EcalEndcapMonitorTasks.EETrendTask_cfi")
process.load("DQM.EcalEndcapMonitorClient.EETrendClient_cfi")

import DQM.EcalBarrelMonitorClient.EcalBarrelMonitorDbClient_cfi
process.ecalBarrelMonitorClient = DQM.EcalBarrelMonitorClient.EcalBarrelMonitorDbClient_cfi.ecalBarrelMonitorDbClient.clone()
import DQM.EcalEndcapMonitorClient.EcalEndcapMonitorDbClient_cfi
process.ecalEndcapMonitorClient = DQM.EcalEndcapMonitorClient.EcalEndcapMonitorDbClient_cfi.ecalEndcapMonitorDbClient.clone()


### DQM COMMON MODULES ###

process.load("DQMServices.Core.DQM_cfg")

process.dqmQTestEB = cms.EDAnalyzer("QualityTester",
  reportThreshold = cms.untracked.string("red"),
  prescaleFactor = cms.untracked.int32(0),
  qtList = cms.untracked.FileInPath("DQM/EcalBarrelMonitorModule/test/data/EcalBarrelQualityTests.xml"),
  getQualityTestsFromFile = cms.untracked.bool(True),
  qtestOnEndLumi = cms.untracked.bool(True),
  qtestOnEndRun = cms.untracked.bool(True)
)

process.dqmQTestEE = cms.EDAnalyzer("QualityTester",
  reportThreshold = cms.untracked.string("red"),
  prescaleFactor = cms.untracked.int32(0),
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

process.ecalLaserFilter = cms.EDFilter("EcalMonitorPrescaler")
process.ecalLedFilter = cms.EDFilter("EcalMonitorPrescaler")
process.ecalPedestalFilter = cms.EDFilter("EcalMonitorPrescaler")
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
    process.hltTriggerTypeFilter +
    process.ecalEBunpacker
)

process.ecalDataSequence = cms.Sequence(
    process.ecalUncalibHit *
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

process.ecalLaserPath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalLaserFilter *    
    process.ecalDataSequence *
    process.ecalUncalibHit1 *
    (
    process.ecalMonitorBaseSequence +
    process.ecalBarrelLaserTask +
    process.ecalEndcapLaserTask
    )
)

process.ecalLedPath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalLedFilter *
    process.ecalDataSequence *
    process.ecalUncalibHit1 *
    (
    process.ecalMonitorBaseSequence +    
    process.ecalEndcapLedTask
    )
)

process.ecalPedestalPath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalPedestalFilter *    
    process.ecalDataSequence *
    (
    process.ecalMonitorBaseSequence +    
    process.ecalBarrelPedestalTask +
    process.ecalEndcapPedestalTask
    )
)    

process.ecalTestPulsePath = cms.Path(
    process.ecalPreRecoSequence *
    process.ecalTestPulseFilter *    
    process.ecalDataSequence *
    process.ecalUncalibHit2 *
    (
    process.ecalMonitorBaseSequence +    
    process.ecalBarrelTestPulseTask +
    process.ecalEndcapTestPulseTask
    )
)

process.ecalClientPath = cms.Path(
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
    process.ecalLaserPath,
    process.ecalLedPath,
    process.ecalPedestalPath,
    process.ecalTestPulsePath,
    process.ecalClientPath,
    process.ecalMonitorEndPath,
    process.dqmEndPath
)


### SOURCE ###

process.load("DQM.Integration.test.inputsource_cfi")


### CUSTOMIZATIONS ###
 ## Reconstruction Modules ##

process.ecalUncalibHit.EBdigiCollection = "ecalEBunpacker:ebDigis"
process.ecalUncalibHit.EEdigiCollection = "ecalEBunpacker:eeDigis"

process.ecalDetIdToBeRecovered.ebSrFlagCollection = "ecalEBunpacker"
process.ecalDetIdToBeRecovered.eeSrFlagCollection = "ecalEBunpacker"
process.ecalDetIdToBeRecovered.ebIntegrityGainErrors = "ecalEBunpacker:EcalIntegrityGainErrors"
process.ecalDetIdToBeRecovered.ebIntegrityGainSwitchErrors = "ecalEBunpacker:EcalIntegrityGainSwitchErrors"
process.ecalDetIdToBeRecovered.ebIntegrityChIdErrors = "ecalEBunpacker:EcalIntegrityChIdErrors"
process.ecalDetIdToBeRecovered.eeIntegrityGainErrors = "ecalEBunpacker:EcalIntegrityGainErrors"
process.ecalDetIdToBeRecovered.eeIntegrityGainSwitchErrors = "ecalEBunpacker:EcalIntegrityGainSwitchErrors"
process.ecalDetIdToBeRecovered.eeIntegrityChIdErrors = "ecalEBunpacker:EcalIntegrityChIdErrors"
process.ecalDetIdToBeRecovered.integrityTTIdErrors = "ecalEBunpacker:EcalIntegrityTTIdErrors"
process.ecalDetIdToBeRecovered.integrityBlockSizeErrors = "ecalEBunpacker:EcalIntegrityBlockSizeErrors"

process.ecalRecHit.killDeadChannels = True
process.ecalRecHit.ChannelStatusToBeExcluded = [ 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 78, 142 ]
process.ecalRecHit.EBuncalibRecHitCollection = "ecalUncalibHit:EcalUncalibRecHitsEB"
process.ecalRecHit.EEuncalibRecHitCollection = "ecalUncalibHit:EcalUncalibRecHitsEE"

process.ecalUncalibHit1.MinAmplBarrel = 12.
process.ecalUncalibHit1.MinAmplEndcap = 16.
process.ecalUncalibHit1.EBdigiCollection = "ecalEBunpacker:ebDigis"
process.ecalUncalibHit1.EEdigiCollection = "ecalEBunpacker:eeDigis"

process.ecalUncalibHit2.EBdigiCollection = "ecalEBunpacker:ebDigis"
process.ecalUncalibHit2.EEdigiCollection = "ecalEBunpacker:eeDigis"

 ## Filters ##

process.ecalLaserFilter.EcalRawDataCollection = cms.InputTag("ecalEBunpacker")
process.ecalLaserFilter.laserPrescaleFactor = cms.untracked.int32(1)

process.ecalLedFilter.EcalRawDataCollection = cms.InputTag("ecalEBunpacker")
process.ecalLedFilter.ledPrescaleFactor = cms.untracked.int32(1)

process.ecalPedestalFilter.EcalRawDataCollection = cms.InputTag("ecalEBunpacker")
process.ecalPedestalFilter.pedestalPrescaleFactor = cms.untracked.int32(1)

process.ecalTestPulseFilter.EcalRawDataCollection = cms.InputTag("ecalEBunpacker")
process.ecalTestPulseFilter.testpulsePrescaleFactor = cms.untracked.int32(1)

process.hltTriggerTypeFilter.SelectedTriggerType = 2 # 0=random, 1=physics, 2=calibration, 3=technical

 ## Ecal DQM modules ##

process.ecalBarrelLaserTask.EcalUncalibratedRecHitCollection = "ecalUncalibHit1:EcalUncalibRecHitsEB"
process.ecalBarrelTestPulseTask.EcalUncalibratedRecHitCollection = "ecalUncalibHit2:EcalUncalibRecHitsEB"
process.ecalEndcapLaserTask.EcalUncalibratedRecHitCollection = "ecalUncalibHit1:EcalUncalibRecHitsEE"
process.ecalEndcapLedTask.EcalUncalibratedRecHitCollection = "ecalUncalibHit1:EcalUncalibRecHitsEE"
process.ecalEndcapTestPulseTask.EcalUncalibratedRecHitCollection = "ecalUncalibHit2:EcalUncalibRecHitsEE"

process.ecalBarrelLaserTask.laserWavelengths = [ 1, 4 ]
process.ecalEndcapLaserTask.laserWavelengths = [ 1, 4 ]
process.ecalEndcapLedTask.ledWavelengths = [ 1, 2 ]
process.ecalBarrelMonitorClient.laserWavelengths = [ 1, 4 ]
process.ecalEndcapMonitorClient.laserWavelengths = [ 1, 4 ]
process.ecalEndcapMonitorClient.ledWavelengths = [ 1, 2 ]

process.ecalBarrelIntegrityTask.subfolder = "Calibration"
process.ecalBarrelOccupancyTask.subfolder = "Calibration"
process.ecalBarrelStatusFlagsTask.subfolder = "Calibration"
process.ecalBarrelRawDataTask.subfolder = "Calibration"
process.ecalEndcapIntegrityTask.subfolder = "Calibration"
process.ecalEndcapOccupancyTask.subfolder = "Calibration"
process.ecalEndcapStatusFlagsTask.subfolder = "Calibration"
process.ecalEndcapRawDataTask.subfolder = "Calibration"

process.ecalBarrelPedestalTask.MGPAGains = [ 12 ]
process.ecalBarrelPedestalTask.MGPAGainsPN = [ 16 ]
process.ecalBarrelTestPulseTask.MGPAGains = [ 12 ]
process.ecalBarrelTestPulseTask.MGPAGainsPN = [ 16 ]
process.ecalEndcapPedestalTask.MGPAGains = [ 12 ]
process.ecalEndcapPedestalTask.MGPAGainsPN = [ 16 ]
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

process.ecalBarrelMonitorClient.enabledClients = ["Integrity", "Occupancy", "Pedestal", "TestPulse", "Laser", "Summary"]
process.ecalEndcapMonitorClient.enabledClients = ["Integrity", "Occupancy", "Pedestal", "TestPulse", "Laser", "Led", "Summary"]

process.ecalBarrelMonitorClient.produceReports = False
process.ecalEndcapMonitorClient.produceReports = False

process.ecalBarrelMonitorClient.subfolder = "Calibration"
process.ecalEndcapMonitorClient.subfolder = "Calibration"

os.environ["TNS_ADMIN"] = "/etc"
dbName = ""
dbHostName = ""
dbHostPort = 1521
dbUserName = ""
dbPassword = ""

try :
    file = open("/nfshome0/ecalpro/DQM/online-DQM/.cms_tstore.conf", "r")
    for line in file :
        if line.find("dbName") >= 0 :
            dbName = line.split()[2]
        if line.find("dbHostName") >= 0 :
            dbHostName = line.split()[2]
        if line.find("dbHostPort") >= 0 :
            dbHostPort = int(line.split()[2])
        if line.find("dbUserName") >= 0 :
            dbUserName = line.split()[2]
        if line.find("dbPassword") >= 0 :
            dbPassword = line.split()[2]
    file.close()
except IOError :
    pass

process.ecalBarrelMonitorClient.dbName = dbName
process.ecalBarrelMonitorClient.dbHostName = dbHostName
process.ecalBarrelMonitorClient.dbHostPort = dbHostPort
process.ecalBarrelMonitorClient.dbUserName = dbUserName
process.ecalBarrelMonitorClient.dbPassword = dbPassword

process.ecalEndcapMonitorClient.dbName = dbName
process.ecalEndcapMonitorClient.dbHostName = dbHostName
process.ecalEndcapMonitorClient.dbHostPort = dbHostPort
process.ecalEndcapMonitorClient.dbUserName = dbUserName
process.ecalEndcapMonitorClient.dbPassword = dbPassword

process.ecalBarrelMonitorClient.dbUpdateTime = 120
process.ecalBarrelMonitorClient.dbUpdateTime = 120
process.ecalBarrelMonitorClient.dbTagName = "CMSSW-online-central"
process.ecalEndcapMonitorClient.dbTagName = "CMSSW-online-central"

 ## DQM common modules ##

process.DQMStore.referenceFileName = "/dqmdata/dqm/reference/ecalcalib_reference.root"

process.dqmEnvEB.subSystemFolder = cms.untracked.string("EcalBarrel")
process.dqmEnvEE.subSystemFolder = cms.untracked.string("EcalEndcap")

 ## Source ##
process.source.consumerName = cms.untracked.string("EcalCalibration DQM Consumer")
process.source.SelectHLTOutput = cms.untracked.string("hltOutputCalibration")

 ## Run type specific ##
if process.runType.getRunType() == process.runType.cosmic_run :
    process.ecalMonitorEndPath.remove(process.dqmQTestEB)
    process.ecalMonitorEndPath.remove(process.dqmQTestEE)
elif process.runType.getRunType() == process.runType.hpu_run:
    process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring("*"))

 ## FEDRawDataCollection name ##
FedRawData = "hltEcalCalibrationRaw"
if process.runType.getRunType() == process.runType.hi_run:
    FedRawData = "rawDataRepacker"

process.ecalEBunpacker.InputLabel = cms.InputTag(FedRawData)
process.ecalBarrelRawDataTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.ecalEndcapRawDataTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.l1GtEvmUnpack.EvmGtInputTag = cms.InputTag(FedRawData)
process.ecalBarrelTrendTask.FEDRawDataCollection = cms.InputTag(FedRawData)
process.ecalEndcapTrendTask.FEDRawDataCollection = cms.InputTag(FedRawData)
