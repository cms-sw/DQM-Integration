import FWCore.ParameterSet.Config as cms
from DQM.HcalMonitorModule.HcalMonitorModule_cfi import * # Can this be done better?
from DQM.HcalMonitorClient.HcalMonitorClient_cfi import * 

subsystem="Hcal"

process = cms.Process("HCALDQM")
#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_playback_cfi")
process.EventStreamHttpReader.consumerName = 'Hcal DQM Consumer'


# Specify event source here (use PoolSource if running on castor data from lxplus, etc.)

# process.maxEvents = cms.untracked.PSet(
#     input = cms.untracked.int32(-1)
#     )
# 
# process.source = cms.Source("EventStreamHttpReader",
#                             sourceURL = cms.string('http://srv-C2D05-05:50082/urn:xdaq-application:lid=29'),
#                             consumerPriority = cms.untracked.string('normal'),
#                             max_event_size = cms.int32(7000000),
#                             consumerName = cms.untracked.string('Playback Source'),
#                             max_queue_depth = cms.int32(5),
#                             maxEventRequestRate = cms.untracked.double(12.0),
#                             SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('*')
#                                                               ),
#                             headerRetryInterval = cms.untracked.int32(3)
#                             )

#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
#process.DQMStore.referenceFileName = '/home/dqmdevlocal/reference/hcal_reference.root'

#----------------------------
# DQM Playback Environment
#-----------------------------
process.load("DQM.Integration.test.environment_playback_cfi")
process.dqmEnv.subSystemFolder    = subsystem

# process.DQM.collectorHost = 'hcaldqm01.cms' # specify machine you're using
# process.DQM.collectorPort = 9190
# process.dqmSaver.dirName = '/tmp/stjohn/dqmdata' # specify output directory

#-----------------------------
# Hcal Conditions: from Global Conditions Tag 
#-----------------------------
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = 'GR09_31X_V6H::All' # or any other appropriate
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')

process.load("FWCore.MessageLogger.MessageLogger_cfi")


#-----------------------------
# Hcal DQM Source, including SimpleReconstrctor
#-----------------------------
process.load("DQM.HcalMonitorModule.HcalMonitorModule_cfi")
process.load("EventFilter.HcalRawToDigi.HcalRawToDigi_cfi")
process.load("RecoLocalCalo.HcalRecProducers.HcalHitReconstructor_hbhe_cfi")
process.load("RecoLocalCalo.HcalRecProducers.HcalHitReconstructor_ho_cfi")
process.load("RecoLocalCalo.HcalRecProducers.HcalHitReconstructor_hf_cfi")
process.load("RecoLocalCalo.HcalRecProducers.HcalHitReconstructor_zdc_cfi")

# Set expected orbit time to 6
process.hcalDigis.ExpectedOrbitMessageTime=cms.untracked.int32(6)
# Allow even bad-quality digis
#process.hcalDigis.FilterDataQuality=False

# Cosmics Corrections to reconstruction
process.hbhereco.firstSample = 1
process.hbhereco.samplesToAdd = 8
process.hbhereco.correctForTimeslew = True
process.hbhereco.correctForPhaseContainment = True
process.hbhereco.correctionPhaseNS = 10.0
process.horeco.firstSample = 1
process.horeco.samplesToAdd = 8
process.horeco.correctForTimeslew = True
process.horeco.correctForPhaseContainment = True
process.horeco.correctionPhaseNS = 10.
process.hfreco.firstSample = 1
process.hfreco.samplesToAdd = 8
process.hfreco.correctForTimeslew = True
process.hfreco.correctForPhaseContainment = True
process.hfreco.correctionPhaseNS = 10.
process.zdcreco.firstSample = 1
process.zdcreco.samplesToAdd = 8
process.zdcreco.correctForTimeslew = True
process.zdcreco.correctForPhaseContainment = True
process.zdcreco.correctionPhaseNS = 10.

process.essourceSev =  cms.ESSource("EmptyESSource",
                                    recordName = cms.string("HcalSeverityLevelComputerRcd"),
                                    firstValid = cms.vuint32(1),
                                    iovIsRunNotTime = cms.bool(True)
                                    )


process.hcalRecAlgos = cms.ESProducer("HcalRecAlgoESProducer",
                                      SeverityLevels = cms.VPSet(
    cms.PSet( Level = cms.int32(0),
              RecHitFlags = cms.vstring(''),
              ChannelStatus = cms.vstring('')
              ),
    cms.PSet( Level = cms.int32(5),
              RecHitFlags = cms.vstring('HSCP_R1R2','HSCP_FracLeader','HSCP_OuterEnergy',
                                        'HSCP_ExpFit','ADCSaturationBit'),
              ChannelStatus = cms.vstring('')
              ),
    cms.PSet( Level = cms.int32(8),
              RecHitFlags = cms.vstring('HBHEHpdHitMultiplicity', 'HBHEPulseShape', 'HOBit',
                                        'HFDigiTime', 'HFLongShort', 'ZDCBit', 'CalibrationBit',
                                        'TimingErrorBit'),
              ChannelStatus = cms.vstring('')
              ),
    cms.PSet( Level = cms.int32(10),
              RecHitFlags = cms.vstring(''),
              ChannelStatus = cms.vstring('HcalCellHot')
              ),
    cms.PSet( Level = cms.int32(20),
              RecHitFlags = cms.vstring(''),
              ChannelStatus = cms.vstring('HcalCellOff', 'HcalCellDead')
              )
    ),
                                      RecoveredRecHitBits = cms.vstring('TimingAddedBit','TimingSubtractedBit'),
                                      DropChannelStatusBits = cms.vstring('HcalCellOff',) #'HcalCellDead' had also been present
                                      )
#----------------------------
# Trigger Emulator
#----------------------------
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')
process.valHcalTriggerPrimitiveDigis = process.simHcalTriggerPrimitiveDigis.clone()
process.valHcalTriggerPrimitiveDigis.inputLabel = cms.VInputTag('hcalDigis', 'hcalDigis')
process.HcalTPGCoderULUT.LUTGenerationMode = cms.bool(False)

# -------------------------------
# hcalMonitor configurable values
# -------------------------------
process.hcalMonitor.debug = 0
#process.hcalMonitor.DigiOccThresh = -999999999 ##Temporary measure while DigiOcc is reworked.
process.hcalMonitor.pedestalsInFC = True
process.hcalMonitor.showTiming = False
process.hcalMonitor.checkNevents=1000
process.hcalMonitor.dump2database = False

# Turn on/off individual hcalMonitor modules ------------
process.hcalMonitor.subSystemFolder = cms.untracked.string(subsystem)

process.hcalMonitor.DataFormatMonitor   = True
process.hcalMonitor.DataIntegrityTask   = False
process.hcalMonitor.DigiMonitor         = True # disabled until we find why it crashes
process.hcalMonitor.RecHitMonitor       = True
process.hcalMonitor.TrigPrimMonitor     = True
process.hcalMonitor.DetDiagNoiseMonitor = True
process.hcalMonitor.DeadCellMonitor     = True
process.hcalMonitor.HotCellMonitor      = True
process.hcalMonitor.BeamMonitor         = True
process.hcalMonitor.PedestalMonitor     = True
process.hcalMonitor.DetDiagNoiseMonitor = True
process.hcalMonitor.DetDiagTimingMonitor = True
process.hcalMonitor.LEDMonitor          = False
process.hcalMonitor.CaloTowerMonitor    = False
process.hcalMonitor.MTCCMonitor         = False
process.hcalMonitor.HcalAnalysis        = False

# This takes the default cfg values from the hcalMonitor base class and applies them to the subtasks.
setHcalTaskValues(process.hcalMonitor)

# Set individual Task values here (otherwise they will remain set to the values specified for the hcalMonitor.)

#-----------------------------
# Hcal DQM Client
#-----------------------------
process.load("DQM.HcalMonitorClient.HcalMonitorClient_cfi")

# hcalClient configurable values ------------------------
# suppresses html output from HCalClient  
process.hcalClient.baseHtmlDir = ''  # set to '' to prevent html output
process.hcalClient.subSystemFolder  = cms.untracked.string(subsystem)
process.hcalClient.prefixME = cms.untracked.string(subsystem)

# Set client settings to the same as monitor.  At the moment, this doesn't affect client minErrorFlag
# Summary Client is also unaffected
setHcalClientValuesFromMonitor(process.hcalClient,process.hcalMonitor, debug=False)  # turn debug to True to dump out client settings

process.hcalClient.SummaryClient        = True


# ----------------------
# Trigger Unpacker Stuff
# ----------------------
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("L1Trigger.Configuration.L1DummyConfig_cff")
process.load("EventFilter.L1GlobalTriggerRawToDigi.l1GtUnpack_cfi")
process.l1GtUnpack.DaqGtInputTag = 'source'


#-----------------------------
# Scheduling
#-----------------------------
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound', 
        'TooManyProducts', 
        'TooFewProducts')
)

process.p = cms.Path(process.hcalDigis
                     *process.valHcalTriggerPrimitiveDigis
                     *process.horeco
                     *process.hfreco
                     *process.hbhereco
                     *process.zdcreco
                     *process.hcalMonitor
                     *process.hcalClient
                     *process.dqmEnv
                     *process.dqmSaver)


#-----------------------------
# Quality Tester 
# will add switch to select histograms to be saved soon
#-----------------------------
process.qTester = cms.EDFilter("QualityTester",
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/HcalMonitorClient/data/hcal_qualitytest_config.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True)
)

