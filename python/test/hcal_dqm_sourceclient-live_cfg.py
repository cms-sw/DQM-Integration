import FWCore.ParameterSet.Config as cms
from DQM.HcalMonitorModule.HcalMonitorModule_cfi import * # Can this be done better?
from DQM.HcalMonitorClient.HcalMonitorClient_cfi import * 

process = cms.Process("HCALDQM")
subsystem="Hcal" # specify subsystem name here

#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'Hcal DQM Consumer'

# process.maxEvents = cms.untracked.PSet(
#     input = cms.untracked.int32(-1)
#     )
# 
# process.source = cms.Source("EventStreamHttpReader",
#                             sourceURL = cms.string('http://cmsmon:50082/urn:xdaq-application:lid=29'),
#                             consumerPriority = cms.untracked.string('normal'),
#                             max_event_size = cms.int32(7000000),
#                             consumerName = cms.untracked.string('DQM Source'),
#                             max_queue_depth = cms.int32(5),
#                             maxEventRequestRate = cms.untracked.double(15.0),
#                             SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('*DQM')
#                                                               ),
#                             headerRetryInterval = cms.untracked.int32(3)
#                             )

#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = subsystem
process.DQMStore.referenceFileName = '/dqmdata/dqm/reference/hcal_reference.root'

#-----------------------------
# Hcal Conditions: from Global Conditions Tag 
#-----------------------------
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")

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

# Turn off default blocking of dead channels from rechit reconstructor
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
process.hcalMonitor.Online = True
process.hcalMonitor.showTiming = False
process.hcalMonitor.checkNevents=1000
process.hcalMonitor.dump2database = False

# Turn on/off individual hcalMonitor modules ------------
process.hcalMonitor.subSystemFolder = cms.untracked.string(subsystem)

process.hcalMonitor.DataFormatMonitor   = True
process.hcalMonitor.DataIntegrityTask   = False
process.hcalMonitor.DigiMonitor         = True # set false until we learn why it crashes
process.hcalMonitor.RecHitMonitor       = True
process.hcalMonitor.TrigPrimMonitor     = True
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

#process.hcalClient.BeamClient_minErrorFlag = 0.05
process.hcalClient.SummaryClient        = True

# Set expected idle BCN time to correct value
#(6 for runs < 116401; 3560 for runs > c. 117900, 3563 for runs between)
#
idle=3560
process.hcalDigis.ExpectedOrbitMessageTime=cms.untracked.int32(idle)
process.hcalMonitor.DigiMonitor_ExpectedOrbitMessageTime = idle

# Allow even bad-quality digis
#process.hcalDigis.FilterDataQuality=False

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
                     *process.l1GtUnpack
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

