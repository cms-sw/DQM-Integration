import FWCore.ParameterSet.Config as cms

process = cms.Process("CASTORDQM")
#=================================
# Event Source
#================================+
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.consumerName = 'CASTOR DQM Consumer'

#================================
# DQM Environment
#================================
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
#process.DQMStore.referenceFileName = 'castor_reference.root'

process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = "Castor"

#============================================
# Castor Conditions: from Global Conditions Tag 
#============================================
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG"
process.GlobalTag.globaltag = 'GR09_H_V4::All' # or any other appropriate
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')


process.load("FWCore.MessageLogger.MessageLogger_cfi")


process.load("CondCore.DBCommon.CondDBSetup_cfi")
#process.load("CondCore.DBCommon.CondDBCommon_cfi")

process.CastorDbProducer = cms.ESProducer("CastorDbProducer")

process.es_hardcode = cms.ESSource("CastorHardcodeCalibrations",
   toGet = cms.untracked.vstring('Gains',
       'Pedestals',
       'PedestalWidths',
       'GainWidths',
       'QIEShape',
       'QIEData',
       'ChannelQuality',
       'RespCorrs',
       'ZSThresholds')
)

process.es_ascii = cms.ESSource("CastorTextCalibrations",
   input = cms.VPSet(cms.PSet(
       object = cms.string('ElectronicsMap'),
       file = cms.FileInPath('DQM/Integration/rcms/castor_cmssw_emap_3dcc_v1.txt')
    )
   )
) 



#-----------------------------
# Castor DQM Source + SimpleReconstrctor
#-----------------------------
process.load("EventFilter.CastorRawToDigi.CastorRawToDigi_cfi")
process.load("RecoLocalCalo.CastorReco.CastorSimpleReconstructor_cfi")


process.castorDigis = cms.EDFilter("CastorRawToDigi",
   CastorFirstFED = cms.untracked.int32(690),
   FilterDataQuality = cms.bool(True),
   ExceptionEmptyData = cms.untracked.bool(True),
   InputLabel = cms.InputTag("source"),
   UnpackCalib = cms.untracked.bool(False),
   FEDs = cms.untracked.vint32(690,691,692),
   lastSample = cms.int32(9),
   firstSample = cms.int32(0)
) 

process.castorMonitor = cms.EDFilter("CastorMonitorModule",
                           ### GLOBAL VARIABLES
                           debug = cms.untracked.int32(0), # make debug an int so that different
                                                           # values can trigger different levels of messaging
                           # Turn on/off timing diagnostic info
                           showTiming          = cms.untracked.bool(False),
                           dump2database       = cms.untracked.bool(False),
                           pedestalsInFC = cms.untracked.bool(False),
                           DigiMonitor = cms.untracked.bool(True),
                           digiLabel = cms.InputTag("castorDigis"),
                           CastorRecHitLabel = cms.InputTag("castorreco"),
                          
                           PedestalMonitor                  = cms.untracked.bool(True),
                           PedestalsPerChannel              = cms.untracked.bool(True), 
                           PedestalsInFC                    = cms.untracked.bool(False),
                          
                           RecHitMonitor = cms.untracked.bool(True), 
			   RecHitMonitorValid = cms.untracked.bool(True),     
                           DigisPerChannel = cms.untracked.bool(False),
                           RecHitsPerChannel = cms.untracked.bool(True),
                             
                           diagnosticPrescaleTime = cms.untracked.int32(-1),
                           diagnosticPrescaleUpdate = cms.untracked.int32(-1),
                           diagnosticPrescaleLS = cms.untracked.int32(-1),
                             
                           LEDMonitor = cms.untracked.bool(True),
                           LEDPerChannel = cms.untracked.bool(True),
                           FirstSignalBin = cms.untracked.int32(0),
                           LastSignalBin = cms.untracked.int32(9),
                           LED_ADC_Thresh = cms.untracked.double(-1000.0)      
                           )

### the filename prefix 
process.dqmSaver.producer = 'DQM'
#process.dqmSaver.dirName = '/tmp/'
process.dqmSaver.convention = 'Online'
process.dqmSaver.saveByRun = True


#-----------------------------
# Scheduling
#-----------------------------
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound', 
        'TooManyProducts', 
        'TooFewProducts')
)

# castorDigis   -> CastorRawToDigi_cfi
# castorreco    -> CastorSimpleReconstructor_cfi
# castorMonitor -> CastorMonitorModule_cfi

process.p = cms.Path(process.castorDigis*process.castorreco*process.castorMonitor*process.dqmEnv*process.dqmSaver)
#process.p = cms.Path(process.castorDigis*process.castorMonitor*process.dqmEnv*process.dqmSaver)
#process.p = cms.Path(process.castorMonitor*process.dqmEnv*process.dqmSaver)
