import FWCore.ParameterSet.Config as cms

process = cms.Process("EvFDQM")

#----------------------------
#### Event Source
#----------------------------
process.load("DQM.Integration.test.inputsource_playback_cfi")
process.EventStreamHttpReader.consumerName = 'FED DQM Consumer'


#----------------------------
#### DQM Environment
#----------------------------
process.load("DQMServices.Core.DQM_cfg")
#process.DQMStore.referenceFileName = "DT_reference.root"


#----------------------------
#### DQM Environment
#----------------------------
process.load("DQM.Integration.test.environment_playback_cfi")
process.dqmEnv.subSystemFolder = 'FED'
#-----------------------------


# message logger
process.MessageLogger = cms.Service("MessageLogger",
                                    destinations = cms.untracked.vstring('cout'),
                                    cout = cms.untracked.PSet(threshold = cms.untracked.string('WARNING'))
                                    )

# Global tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')
process.GlobalTag.connect ="frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"
process.GlobalTag.globaltag = "CRAFT_V1H::All"


#-----------------------------
#### Sub-system configuration follows

# CSC DQM sequence
process.load("DQM.CSCMonitorModule.test.csc_hlt_dqm_sourceclient_cfi")

# DT DQM sequence
process.load("DQM.DTMonitorModule.dtDataIntegrityTask_EvF_cff")

# ECAL DQM sequences
process.load("EventFilter.EcalRawToDigiDev.EcalUnpackerMapping_cfi")
process.load("EventFilter.EcalRawToDigiDev.EcalUnpackerData_cfi")
process.load("Geometry.EcalMapping.EcalMapping_cfi")
process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")
import DQM.EcalBarrelMonitorTasks.EBHltTask_cfi
process.ebDQMEvF = DQM.EcalBarrelMonitorTasks.EBHltTask_cfi.ecalBarrelHltTask.clone()
import DQM.EcalEndcapMonitorTasks.EEHltTask_cfi
process.eeDQMEvF = DQM.EcalEndcapMonitorTasks.EEHltTask_cfi.ecalEndcapHltTask.clone()

# L1T DQM sequences 
process.load("DQM.L1TMonitor.L1TFED_cfi")

# Pixel DQM sequences
process.load("Geometry.TrackerSimData.trackerSimGeometryXML_cfi")
process.load("Geometry.TrackerGeometryBuilder.trackerGeometry_cfi")
process.load("Geometry.TrackerNumberingBuilder.trackerNumberingGeometry_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
# Pixel RawToDigi conversion
process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
process.siPixelDigis.InputLabel = "source"
process.siPixelDigis.Timing = False
process.siPixelDigis.IncludeErrors = True
process.load("DQM.SiPixelMonitorRawData.SiPixelMonitorHLT_cfi")
process.SiPixelHLTSource.saveFile = True
process.SiPixelHLTSource.slowDown = False

# DQM Modules
process.dqmmodules = cms.Sequence(process.dqmEnv + process.dqmSaver)

#-----------------------------
### Define the path
process.evfDQMPath = cms.Path(process.dqmmodules + 
                              process.cscDQMEvF + 
			      process.dtDQMEvF + 
			      process.ecalEBunpacker  + process.ebDQMEvF + process.eeDQMEvF +
			      process.l1tfed +
			      process.siPixelDigis + process.SiPixelHLTSource )


