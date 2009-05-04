import FWCore.ParameterSet.Config as cms

process = cms.Process("ECALDQM")

process.load("EventFilter.EcalRawToDigiDev.EcalUnpackerMapping_cfi")

process.load("EventFilter.EcalRawToDigiDev.EcalUnpackerData_cfi")

import RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi
process.ecalUncalibHit2 = RecoLocalCalo.EcalRecProducers.ecalFixedAlphaBetaFitUncalibRecHit_cfi.ecalFixedAlphaBetaFitUncalibRecHit.clone()

import RecoLocalCalo.EcalRecProducers.ecalWeightUncalibRecHit_cfi
process.ecalUncalibHit = RecoLocalCalo.EcalRecProducers.ecalWeightUncalibRecHit_cfi.ecalWeightUncalibRecHit.clone()

process.load("RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi")

process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")

process.load("Geometry.CaloEventSetup.CaloTopology_cfi")

process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("Geometry.EcalMapping.EcalMapping_cfi")

process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

process.load("DQM.EcalBarrelMonitorModule.EcalBarrelMonitorModule_cfi")

process.load("DQM.EcalBarrelMonitorTasks.EcalBarrelMonitorTasks_cfi")

process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_cff")

process.load("DQM.EcalBarrelMonitorClient.EcalBarrelMonitorClient_cfi")

process.load("RecoEcal.EgammaClusterProducers.ecalClusteringSequence_cff")

process.load("CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi")

process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.load("FWCore.Modules.preScaler_cfi")

process.ecalPrescaler = cms.EDFilter("EcalMonitorPrescaler",
    EcalRawDataCollection = cms.InputTag("ecalEBunpacker"),
    laserPrescaleFactor = cms.untracked.int32(1),
    ledPrescaleFactor = cms.untracked.int32(1),
    pedestalPrescaleFactor = cms.untracked.int32(1),
    testpulsePrescaleFactor = cms.untracked.int32(1)
)

# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1

process.dqmInfoEB = cms.EDAnalyzer("DQMEventInfo",
    subSystemFolder = cms.untracked.string('EcalBarrel')
)

process.dqmQTestEB = cms.EDAnalyzer("QualityTester",
#    reportThreshold = cms.untracked.string('red'),
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/Integration/test/EcalBarrelQualityTests.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True)
)

process.dqmSaver = cms.EDAnalyzer("DQMFileSaver",
    saveByRun = cms.untracked.int32(1),
    dirName = cms.untracked.string('.'),
    saveAtJobEnd = cms.untracked.bool(True),
    convention = cms.untracked.string('Online'),
    referenceHandling = cms.untracked.string('all')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('file:/data1/lookarea/GlobalAug07.00017220.0001.A.storageManager.0.0000.dat')
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"
process.GlobalTag.globaltag = "CRAFT_V14H::All"
process.prefer("GlobalTag")

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        noLineBreaks = cms.untracked.bool(True),
        noTimeStamps = cms.untracked.bool(True),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        EcalRawToDigiDev = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTriggerType = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTpg = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevNumTowerBlocks = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTowerSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevGainZero = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevGainSwitch = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevDccBlockSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemBlock = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemGain = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTCC = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevSRP = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalDCCHeaderRuntypeDecoder = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalBarrelMonitorModule = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalEndcapMonitorModule = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        )
    ),
    categories = cms.untracked.vstring('EcalRawToDigiDev',
                                       'EcalRawToDigiDevTriggerType',
                                       'EcalRawToDigiDevTpg',
                                       'EcalRawToDigiDevNumTowerBlocks',
                                       'EcalRawToDigiDevTowerId',
                                       'EcalRawToDigiDevTowerSize',
                                       'EcalRawToDigiDevChId',
                                       'EcalRawToDigiDevGainZero',
                                       'EcalRawToDigiDevGainSwitch',
                                       'EcalRawToDigiDevDccBlockSize',
                                       'EcalRawToDigiDevMemBlock',
                                       'EcalRawToDigiDevMemTowerId',
                                       'EcalRawToDigiDevMemChId',
                                       'EcalRawToDigiDevMemGain',
                                       'EcalRawToDigiDevTCC',
                                       'EcalRawToDigiDevSRP',
                                       'EcalDCCHeaderRuntypeDecoder',
                                       'EcalBarrelMonitorModule',
                                       'EcalEndcapMonitorModule'),
    destinations = cms.untracked.vstring('cout')
)

process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")

process.preScaler.prescaleFactor = 1

process.ecalDataSequence = cms.Sequence(process.preScaler*process.ecalEBunpacker*process.ecalUncalibHit*process.ecalUncalibHit2*process.ecalRecHit*process.simEcalTriggerPrimitiveDigis)

process.ecalBarrelMonitorSequence = cms.Sequence(process.ecalBarrelMonitorModule*process.dqmInfoEB*process.ecalBarrelMonitorClient*process.dqmQTestEB)

process.ecalBarrelCosmicTasksSequenceP5 = cms.Sequence(process.ecalBarrelOccupancyTask*process.ecalBarrelIntegrityTask*process.ecalBarrelStatusFlagsTask*process.ecalBarrelSelectiveReadoutTask*process.ecalBarrelRawDataTask*process.ecalBarrelLaserTask*process.ecalBarrelPedestalOnlineTask*process.ecalBarrelPedestalTask*process.ecalBarrelTestPulseTask*process.ecalBarrelTriggerTowerTask*process.ecalBarrelTimingTask*process.ecalBarrelCosmicTask)

process.ecalBarrelCosmicTasksSequenceP5.remove(process.ecalBarrelSelectiveReadoutTask)

process.p = cms.Path(process.ecalDataSequence*process.ecalBarrelMonitorSequence*process.dqmSaver)
process.q = cms.Path(process.ecalDataSequence*~process.ecalPrescaler*process.hltTriggerTypeFilter*process.hybridSuperClusters*process.correctedHybridSuperClusters*process.multi5x5BasicClusters*process.multi5x5SuperClusters*process.hltTriggerTypeFilter)
process.r = cms.EndPath(process.ecalBarrelCosmicTasksSequenceP5*process.ecalBarrelClusterTask)

process.r.remove(process.ecalBarrelPedestalOnlineTask)

process.ecalUncalibHit2.MinAmplBarrel = 12.
process.ecalUncalibHit2.MinAmplEndcap = 16.
process.ecalUncalibHit2.EBdigiCollection = 'ecalEBunpacker:ebDigis'
process.ecalUncalibHit2.EEdigiCollection = 'ecalEBunpacker:eeDigis'

process.ecalUncalibHit.EBdigiCollection = 'ecalEBunpacker:ebDigis'
process.ecalUncalibHit.EEdigiCollection = 'ecalEBunpacker:eeDigis'

process.ecalRecHit.EBuncalibRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEB'
process.ecalRecHit.EEuncalibRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEE'

process.ecalBarrelCosmicTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEB'

process.ecalBarrelLaserTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEB'

process.ecalBarrelTimingTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEB'

process.simEcalTriggerPrimitiveDigis.Label = 'ecalEBunpacker'
process.simEcalTriggerPrimitiveDigis.InstanceEB = 'ebDigis'
process.simEcalTriggerPrimitiveDigis.InstanceEE = 'eeDigis'

process.EcalTrigPrimESProducer.DatabaseFile = 'TPG_cosmics.txt.gz'
#process.EcalTrigPrimESProducer.DatabaseFile = 'TPG_startup.txt.gz'

process.ecalBarrelMonitorClient.maskFile = '/nfshome0/ecalpro/MASKING-DQM/maskfile-EB.dat'
process.ecalBarrelMonitorClient.location = 'P5'
process.ecalBarrelMonitorClient.enabledClients = ['Integrity', 'StatusFlags', 'Occupancy', 'PedestalOnline', 'Pedestal', 'TestPulse', 'Laser', 'Timing', 'Cosmic', 'Cluster', 'TriggerTower', 'Summary']

process.hybridSuperClusters.HybridBarrelSeedThr = 0.150
process.hybridSuperClusters.step = 1
process.hybridSuperClusters.eseed = 0.150

process.multi5x5BasicClusters.IslandBarrelSeedThr = 0.150
process.multi5x5BasicClusters.IslandEndcapSeedThr = 0.150

process.multi5x5SuperClusters.seedTransverseEnergyThreshold = 0.150

process.DQM.collectorHost = 'srv-c2d05-16'
process.DQMStore.verbose = 0

