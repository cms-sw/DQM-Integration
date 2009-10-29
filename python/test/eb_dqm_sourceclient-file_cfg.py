import FWCore.ParameterSet.Config as cms

process = cms.Process("ECALDQM")

process.load("EventFilter.EcalRawToDigi.EcalUnpackerMapping_cfi")

process.load("EventFilter.EcalRawToDigi.EcalUnpackerData_cfi")

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

#process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_cff")
process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_craft_cff")

process.load("DQM.EcalBarrelMonitorClient.EcalBarrelMonitorClient_cfi")

process.load("RecoEcal.EgammaClusterProducers.ecalClusteringSequence_cff")

process.load("CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi")

process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("FWCore.Modules.preScaler_cfi")

process.ecalPrescaler0 = cms.EDFilter("EcalMonitorPrescaler",
    EcalRawDataCollection = cms.InputTag("ecalEBunpacker"),
    cosmicPrescaleFactor = cms.untracked.int32(6),
    laserPrescaleFactor = cms.untracked.int32(1),
    ledPrescaleFactor = cms.untracked.int32(1),
    pedestalPrescaleFactor = cms.untracked.int32(2),
    testpulsePrescaleFactor = cms.untracked.int32(2)
)

# 0=random, 1=physics, 2=calibration, 3=technical
process.hltTriggerTypeFilter.SelectedTriggerType = 1

process.dqmInfoEB = cms.EDAnalyzer("DQMEventInfo",
    subSystemFolder = cms.untracked.string('EcalBarrel')
)

process.dqmQTestEB = cms.EDAnalyzer("QualityTester",
#    reportThreshold = cms.untracked.string('red'),
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/EcalBarrelMonitorModule/test/data/EcalBarrelQualityTests.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True)
)

process.dqmSaver = cms.EDAnalyzer("DQMFileSaver",
    saveByRun = cms.untracked.int32(1),
    dirName = cms.untracked.string('.'),
    saveAtJobEnd = cms.untracked.bool(True),
    convention = cms.untracked.string('Online'),
    referenceHandling = cms.untracked.string('qtests')
    #referenceHandling = cms.untracked.string('all')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('file:/data1/lookarea/GlobalAug07.00017220.0001.A.storageManager.0.0000.dat')
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = "GR09_H_V4::All"

process.load("CalibCalorimetry.EcalTrivialCondModules.EcalTrivialCondRetriever_cfi")

process.EcalTrivialConditionRetriever.producedChannelStatus = False
process.EcalTrivialConditionRetriever.weightsForTB = False
process.EcalTrivialConditionRetriever.producedEcalPedestals = False
process.EcalTrivialConditionRetriever.getWeightsFromFile = False
process.EcalTrivialConditionRetriever.producedEcalIntercalibConstants = False
process.EcalTrivialConditionRetriever.producedEcalIntercalibConstantsMC = False
process.EcalTrivialConditionRetriever.producedEcalIntercalibErrors = False
process.EcalTrivialConditionRetriever.producedEcalTimeCalibConstants = False
process.EcalTrivialConditionRetriever.producedEcalTimeCalibErrors = False
process.EcalTrivialConditionRetriever.producedEcalLaserCorrection = False
process.EcalTrivialConditionRetriever.producedEcalGainRatios = False
process.EcalTrivialConditionRetriever.producedEcalADCToGeVConstant = True
process.EcalTrivialConditionRetriever.producedEcalClusterCrackCorrParameters = False
process.EcalTrivialConditionRetriever.producedEcalMappingElectronics = False
process.EcalTrivialConditionRetriever.producedEnergyUncertaintyParameters = False
process.EcalTrivialConditionRetriever.produceEnergyCorrectionParameters = False

process.EcalTrivialConditionRetriever.adcToGeVEBConstant = cms.untracked.double(0.00875)
process.EcalTrivialConditionRetriever.adcToGeVEEConstant = cms.untracked.double(0.060)
process.EcalTrivialConditionRetriever.pedWeights = cms.untracked.vdouble(0.333, 0.333, 0.333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
process.EcalTrivialConditionRetriever.pedWeightsAft = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
process.EcalTrivialConditionRetriever.amplWeights = cms.untracked.vdouble(-0.333, -0.333, -0.333, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0)
process.EcalTrivialConditionRetriever.amplWeightsAftGain = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0)
process.EcalTrivialConditionRetriever.jittWeights = cms.untracked.vdouble(0.041, 0.041, 0.041, 0.0, 1.325, -0.050, -0.504, -0.502, -0.390, 0.0)
process.EcalTrivialConditionRetriever.jittWeightsAft = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0, 1.098, -0.046, -0.416, -0.419, -0.337, 0.0)

#process.prefer("GlobalTag")
process.prefer("EcalTrivialConditionRetriever")

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING'),
        noLineBreaks = cms.untracked.bool(True),
        noTimeStamps = cms.untracked.bool(True),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        EcalRawToDigi = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTriggerType = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTpg = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiNumTowerBlocks = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTowerSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiGainZero = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiGainSwitch = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDccBlockSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiMemBlock = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiMemTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiMemChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiMemGain = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiTCC = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiSRP = cms.untracked.PSet(
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
    categories = cms.untracked.vstring('EcalRawToDigi',
                                       'EcalRawToDigiTriggerType',
                                       'EcalRawToDigiTpg',
                                       'EcalRawToDigiNumTowerBlocks',
                                       'EcalRawToDigiTowerId',
                                       'EcalRawToDigiTowerSize',
                                       'EcalRawToDigiChId',
                                       'EcalRawToDigiGainZero',
                                       'EcalRawToDigiGainSwitch',
                                       'EcalRawToDigiDccBlockSize',
                                       'EcalRawToDigiMemBlock',
                                       'EcalRawToDigiMemTowerId',
                                       'EcalRawToDigiMemChId',
                                       'EcalRawToDigiMemGain',
                                       'EcalRawToDigiTCC',
                                       'EcalRawToDigiSRP',
                                       'EcalDCCHeaderRuntypeDecoder',
                                       'EcalBarrelMonitorModule',
                                       'EcalEndcapMonitorModule'),
    destinations = cms.untracked.vstring('cout')
)

process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")

process.preScaler.prescaleFactor = 1

process.ecalDataSequence = cms.Sequence(process.preScaler*process.ecalEBunpacker*process.ecalPrescaler0*process.ecalUncalibHit*process.ecalUncalibHit2*process.ecalRecHit)

process.ecalBarrelMonitorSequence = cms.Sequence(process.ecalBarrelMonitorModule*process.ecalBarrelMonitorClient)

process.ecalBarrelTasksSequenceP5 = cms.Sequence(process.ecalBarrelOccupancyTask*process.ecalBarrelIntegrityTask*process.ecalBarrelStatusFlagsTask*process.ecalBarrelRawDataTask*process.ecalBarrelLaserTask*process.ecalBarrelPedestalTask*process.ecalBarrelTestPulseTask*process.ecalBarrelCosmicTask*process.ecalBarrelClusterTask)

process.p = cms.Path(process.ecalDataSequence*process.ecalBarrelMonitorSequence)
process.q = cms.Path(process.ecalDataSequence*process.hltTriggerTypeFilter*process.hybridSuperClusters*process.correctedHybridSuperClusters*process.multi5x5BasicClusters*process.multi5x5SuperClusters*process.ecalBarrelPedestalOnlineTask*process.simEcalTriggerPrimitiveDigis*process.ecalBarrelTriggerTowerTask*process.ecalBarrelTimingTask*process.ecalBarrelSelectiveReadoutTask)
process.r = cms.EndPath(process.dqmEnv*process.ecalBarrelTasksSequenceP5*process.dqmQTestEB*process.dqmSaver)

process.ecalUncalibHit2.MinAmplBarrel = 12.
process.ecalUncalibHit2.MinAmplEndcap = 16.
process.ecalUncalibHit2.EBdigiCollection = 'ecalEBunpacker:ebDigis'
process.ecalUncalibHit2.EEdigiCollection = 'ecalEBunpacker:eeDigis'

process.ecalUncalibHit.EBdigiCollection = 'ecalEBunpacker:ebDigis'
process.ecalUncalibHit.EEdigiCollection = 'ecalEBunpacker:eeDigis'

process.ecalRecHit.killDeadChannels = False
process.ecalRecHit.EBuncalibRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEB'
process.ecalRecHit.EEuncalibRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEE'

process.ecalBarrelCosmicTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEB'

process.ecalBarrelLaserTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEB'
#process.ecalBarrelLaserTask.laserWavelengths = [ 1, 2, 3, 4 ]
process.ecalBarrelLaserTask.laserWavelengths = [ 1, 4 ]

#process.ecalBarrelPedestalTask.MGPAGains = [ 1, 6, 12 ]
process.ecalBarrelPedestalTask.MGPAGains = [ 12 ]
#process.ecalBarrelPedestalTask.MGPAGainsPN = [ 1, 16 ]
process.ecalBarrelPedestalTask.MGPAGainsPN = [ 16 ]

#process.ecalBarrelTestPulseTask.MGPAGains = [ 1, 6, 12 ]
process.ecalBarrelTestPulseTask.MGPAGains = [ 12 ]
#process.ecalBarrelTestPulseTask.MGPAGainsPN = [ 1, 16 ]
process.ecalBarrelTestPulseTask.MGPAGainsPN = [ 16 ]

process.ecalBarrelTimingTask.EcalUncalibratedRecHitCollection = 'ecalUncalibHit2:EcalUncalibRecHitsEB'

process.simEcalTriggerPrimitiveDigis.Label = 'ecalEBunpacker'
process.simEcalTriggerPrimitiveDigis.InstanceEB = 'ebDigis'
process.simEcalTriggerPrimitiveDigis.InstanceEE = 'eeDigis'

#process.EcalTrigPrimESProducer.DatabaseFile = 'TPG_startup.txt.gz'
process.EcalTrigPrimESProducer.DatabaseFile = 'TPG_craft.txt.gz'

process.ecalBarrelMonitorClient.maskFile = ''
process.ecalBarrelMonitorClient.location = 'P5_Co'
#process.ecalBarrelMonitorClient.laserWavelengths = [ 1, 2, 3, 4 ]
process.ecalBarrelMonitorClient.laserWavelengths = [ 1, 4 ]
#process.ecalBarrelMonitorClient.MGPAGains = [ 1, 6, 12 ]
process.ecalBarrelMonitorClient.MGPAGains = [ 12 ]
#process.ecalBarrelMonitorClient.MGPAGainsPN = [ 1, 16 ]
process.ecalBarrelMonitorClient.MGPAGainsPN = [ 16 ]
process.ecalBarrelMonitorClient.enabledClients = ['Integrity', 'StatusFlags', 'Occupancy', 'PedestalOnline', 'Pedestal', 'TestPulse', 'Laser', 'Timing', 'Cosmic', 'Cluster', 'TriggerTower', 'Summary']

process.hybridSuperClusters.HybridBarrelSeedThr = 0.150
process.hybridSuperClusters.step = 1
process.hybridSuperClusters.eseed = 0.150

process.multi5x5BasicClusters.IslandBarrelSeedThr = 0.150
process.multi5x5BasicClusters.IslandEndcapSeedThr = 0.150

process.multi5x5SuperClusters.seedTransverseEnergyThreshold = 0.150

process.DQM.collectorHost = 'srv-c2d05-16'
process.DQMStore.verbose = 0

