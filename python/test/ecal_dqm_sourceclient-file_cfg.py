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

process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")

process.load("Geometry.EcalMapping.EcalMapping_cfi")

process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

process.load("DQM.EcalBarrelMonitorModule.EcalBarrelMonitorModule_cfi")

process.load("DQM.EcalBarrelMonitorTasks.EcalBarrelMonitorTasks_cfi")

process.load("Geometry.CaloEventSetup.EcalTrigTowerConstituents_cfi")

process.load("SimCalorimetry.EcalTrigPrimProducers.ecalTriggerPrimitiveDigis_cff")

process.load("DQM.EcalBarrelMonitorClient.EcalBarrelMonitorClient_cfi")

process.load("RecoEcal.EgammaClusterProducers.ecalClusteringSequence_cff")

process.load("CondCore.DBCommon.CondDBSetup_cfi")

process.load("CalibCalorimetry.EcalLaserCorrection.ecalLaserCorrectionService_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.preScaler = cms.EDFilter("Prescaler",
    prescaleFactor = cms.int32(1)
)

process.dqmInfoEB = cms.EDFilter("DQMEventInfo",
    subSystemFolder = cms.untracked.string('EcalBarrel')
)

process.dqmQTestEB = cms.EDFilter("QualityTester",
    reportThreshold = cms.untracked.string('red'),
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/Integration/test/EcalBarrelQualityTests.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True)
)

process.dqmSaverEB = cms.EDFilter("DQMFileSaver",
    saveByRun = cms.untracked.int32(1),
    dirName = cms.untracked.string('.'),
    saveAtJobEnd = cms.untracked.bool(True),
    fileName = cms.untracked.string('EcalBarrel'),
    convention = cms.untracked.string('Online')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("NewEventStreamFileReader",
    fileNames = cms.untracked.vstring('file:/data1/lookarea/GlobalAug07.00017220.0001.A.storageManager.0.0000.dat')
)

process.ecalConditions = cms.ESSource("PoolDBESSource",
    process.CondDBSetup,
    siteLocalConfig = cms.untracked.bool(False),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('EcalPedestalsRcd'),
        tag = cms.string('EcalPedestals_v2_online')
    ), 
        cms.PSet(
            record = cms.string('EcalADCToGeVConstantRcd'),
            tag = cms.string('EcalADCToGeVConstant_CosmGain200')
        ), 
        cms.PSet(
            record = cms.string('EcalChannelStatusRcd'),
            tag = cms.string('EcalChannelStatus_FromCruzet_v3_online')
        ), 
        cms.PSet(
            record = cms.string('EcalGainRatiosRcd'),
            tag = cms.string('EcalGainRatios_TestPulse_online')
        ), 
        cms.PSet(
            record = cms.string('EcalIntercalibConstantsRcd'),
            tag = cms.string('EcalIntercalibConstants_CosmGain200')
        ), 
        cms.PSet(
            record = cms.string('EcalWeightXtalGroupsRcd'),
            tag = cms.string('EcalWeightXtalGroups_mc')
        ), 
        cms.PSet(
            record = cms.string('EcalTBWeightsRcd'),
            tag = cms.string('EcalTBWeights_mc')
        ), 
        cms.PSet(
            record = cms.string('EcalLaserAlphasRcd'),
            tag = cms.string('EcalLaserAlphas_mc')
        ), 
        cms.PSet(
            record = cms.string('EcalLaserAPDPNRatiosRcd'),
            tag = cms.string('EcalLaserAPDPNRatios_mc')
        ), 
        cms.PSet(
            record = cms.string('EcalLaserAPDPNRatiosRefRcd'),
            tag = cms.string('EcalLaserAPDPNRatiosRef_mc')
        )),
    messagelevel = cms.untracked.uint32(0),
    timetype = cms.string('runnumber'),
    connect = cms.string('frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_20X_ECAL'),
#    connect = cms.string("frontier://FrontierProd/CMS_COND_20X_ECAL"),
    authenticationMethod = cms.untracked.uint32(1)
)

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        EcalRawToDigiDevTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        threshold = cms.untracked.string('WARNING'),
        EcalRawToDigiDevTCC = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevSRP = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalDCCHeaderRuntypeDecoder = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDev = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemGain = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemBlock = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevDccBlockSize = cms.untracked.PSet(
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
        EcalBarrelMonitorModule = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        EcalRawToDigiDevMemTowerId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevGainSwitch = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevTowerSize = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevMemChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        noTimeStamps = cms.untracked.bool(True),
        EcalRawToDigiDevChId = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        EcalRawToDigiDevGainZero = cms.untracked.PSet(
            limit = cms.untracked.int32(1000)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        noLineBreaks = cms.untracked.bool(True)
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
        'EcalBarrelMonitorModule'),
    destinations = cms.untracked.vstring('cout')
)

process.ecalDataSequence = cms.Sequence(process.preScaler*process.ecalEBunpacker*process.ecalUncalibHit*process.ecalUncalibHit2*process.ecalRecHit*process.simEcalTriggerPrimitiveDigis*process.islandBasicClusters*process.islandSuperClusters*process.hybridSuperClusters)

process.ecalBarrelMonitorSequence = cms.Sequence(process.ecalBarrelMonitorModule*process.dqmInfoEB*process.ecalBarrelMonitorClient*process.dqmQTestEB*process.dqmSaverEB)

process.ecalBarrelCosmicTasksSequenceP5 = cms.Sequence(process.ecalBarrelOccupancyTask*process.ecalBarrelIntegrityTask*process.ecalBarrelStatusFlagsTask*process.ecalBarrelPedestalOnlineTask*process.ecalBarrelTriggerTowerTask*process.ecalBarrelTimingTask*process.ecalBarrelCosmicTask)

process.p = cms.Path(process.ecalDataSequence*process.ecalBarrelMonitorSequence)
process.q = cms.EndPath(process.ecalBarrelCosmicTasksSequenceP5*process.ecalBarrelClusterTask)

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
process.ecalBarrelMonitorClient.enabledClients = ['Integrity', 'StatusFlags', 'Occupancy', 'PedestalOnline', 'Timing', 'Cosmic', 'Cluster', 'Summary']

process.islandBasicClusters.IslandBarrelSeedThr = 0.150
process.islandBasicClusters.IslandEndcapSeedThr = 0.150

process.hybridSuperClusters.HybridBarrelSeedThr = 0.150
process.hybridSuperClusters.step = 1
process.hybridSuperClusters.eseed = 0.150

process.islandSuperClusters.seedTransverseEnergyThreshold = 0.150

process.DQM.collectorHost = 'srv-c2d05-16'
process.DQMStore.verbose = 0
#process.DQMStore.referenceFileName = '/home/dqmprolocal/reference/DQM_EcalBarrel_R000046798.root'

