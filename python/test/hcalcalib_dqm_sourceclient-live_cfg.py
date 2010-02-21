import FWCore.ParameterSet.Config as cms
from DQM.HcalMonitorModule.HcalMonitorModule_cfi import * # Can this be done better?
from DQM.HcalMonitorClient.HcalMonitorClient_cfi import *

process = cms.Process("HCALDQM")

subsystem="HcalCalib"

#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'Hcal Orbit Gap DQM Consumer'
process.EventStreamHttpReader.SelectEvents =  cms.untracked.PSet(SelectEvents = cms.vstring('HLT_HcalCalibration'))
process.EventStreamHttpReader.sourceURL = cms.string('http://srv-c2c05-09.cms:23100/urn:xdaq-application:lid=30')


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

# Corrections to HF timing
process.hfreco.firstSample = 3
process.hfreco.samplesToAdd = 4

# Allow all rechits in mark&pass events
process.hfreco.dropZSmarkedPassed=False
process.horeco.dropZSmarkedPassed=False
process.hbhereco.dropZSmarkedPassed=False


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

# hcalMonitor configurable values -----------------------
process.hcalMonitor.debug = 0
process.hcalMonitor.pedestalsInFC = True
process.hcalMonitor.showTiming = False
process.hcalMonitor.checkNevents=1000
process.hcalMonitor.Online = True

process.hcalMonitor.subSystemFolder = cms.untracked.string(subsystem)

# Turn on/off individual hcalMonitor modules ------------
process.hcalMonitor.DetDiagPedestalMonitor = True
process.hcalMonitor.DetDiagLaserMonitor    = True

process.hcalMonitor.DataFormatMonitor   = True
process.hcalMonitor.DataIntegrityTask   = False
process.hcalMonitor.DigiMonitor         = False
process.hcalMonitor.RecHitMonitor       = True
process.hcalMonitor.TrigPrimMonitor     = False
process.hcalMonitor.DeadCellMonitor     = False
process.hcalMonitor.HotCellMonitor      = False
process.hcalMonitor.BeamMonitor         = False
process.hcalMonitor.ReferencePedestalMonitor     = False
process.hcalMonitor.DetDiagNoiseMonitor = False
process.hcalMonitor.LEDMonitor          = False
process.hcalMonitor.CaloTowerMonitor    = False
process.hcalMonitor.MTCCMonitor         = False
process.hcalMonitor.HcalAnalysis        = False

# This takes the default cfg values from the hcalMonitor base class and applies them to the subtasks.
setHcalTaskValues(process.hcalMonitor)

# Set individual Task values here (otherwise they will remain set to the values specified for the hcalMonitor.)

process.hcalMonitor.RecHitMonitor_AllowedCalibTypes = [1] # only pedestal events allowed for rechit monitor

process.hcalMonitor.DataFormatMonitor_AllowedCalibTypes=[1,2,3,4,5,6] # all calib types allowed for DataFormatMonitor

#-----------------------------
# Hcal DQM Client
#-----------------------------
process.load("DQM.HcalMonitorClient.HcalMonitorClient_cfi")
process.hcalClient.subSystemFolder = cms.untracked.string(subsystem)
process.hcalClient.prefixME = cms.untracked.string(subsystem)

# hcalClient configurable values ------------------------
# suppresses html output from HCalClient  
process.hcalClient.baseHtmlDir = ''  # set to '' to prevent html output

# Set client settings to the same as monitor.  At the moment, this doesn't affect client minErrorFlag
# Summary Client is also unaffected
setHcalClientValuesFromMonitor(process.hcalClient,process.hcalMonitor, debug=False)  # turn debug to True to dump out client settings

process.hcalClient.SummaryClient        = True
process.hcalClient.DataFormatClient_minErrorFlag = 2. # ignore errors from dataformat client

#-----------------------------
# Scheduling
#-----------------------------
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound', 
        'TooManyProducts', 
        'TooFewProducts')
)

process.p = cms.Path(process.hcalDigis
                     *process.horeco
                     *process.hfreco
                     *process.hbhereco
                     *process.hcalMonitor*process.hcalClient*process.dqmEnv*process.dqmSaver)


#-----------------------------
# Quality Tester 
# will add switch to select histograms to be saved soon
#-----------------------------
process.qTester = cms.EDFilter("QualityTester",
    prescaleFactor = cms.untracked.int32(1),
    qtList = cms.untracked.FileInPath('DQM/HcalMonitorClient/data/hcal_qualitytest_config.xml'),
    getQualityTestsFromFile = cms.untracked.bool(True),
    qtestOnEndLumi = cms.untracked.bool(True),
    qtestOnEndRun = cms.untracked.bool(True)
)

