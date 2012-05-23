import FWCore.ParameterSet.Config as cms

process = cms.Process("BeamSpotProblemMonitor")

#----------------------------
# Common part for PP and H.I Running
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")


#--------------------------
# HLT Filter
process.load("HLTrigger.special.HLTTriggerTypeFilter_cfi")
process.hltTriggerTypeFilter.SelectedTriggerType = 1


#----------------------------
# DQM Live Environment
#-----------------------------
process.load("DQM.Integration.test.environment_cfi")
process.dqmEnv.subSystemFolder = 'BeamSpotProblemMonitor'
process.load("DQM.BeamMonitor.BeamSpotProblemMonitor_cff")
import DQMServices.Components.DQMEnvironment_cfi
#----------------------------
# BeamSpotProblemMonitor
#-----------------------------

####  SETUP TRACKING RECONSTRUCTION ####
process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load("DQM.Integration.test.FrontierCondition_GT_cfi")
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

process.qTester = cms.EDAnalyzer("QualityTester",
                                    qtList = cms.untracked.FileInPath('DQM/BeamMonitor/test/BeamSpotAvailableTest.xml'),
                                    prescaleFactor = cms.untracked.int32(1),                               
                                    testInEventloop = cms.untracked.bool(False),
                                    verboseQT =  cms.untracked.bool(True)                 
                                   )

process.dqmcommon = cms.Sequence(process.dqmEnv
                                *process.qTester
                                *process.dqmSaver)

process.monitor = cms.Sequence(process.dqmBeamSpotProblemMonitor)



#--------------------------
# Proton-Proton Stuff
#--------------------------
if (process.runType.getRunType() == process.runType.pp_run ):

    print "Running pp"

    process.castorDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.csctfDigis.producer = cms.InputTag("rawDataCollector")
    process.dttfDigis.DTTF_FED_Source = cms.InputTag("rawDataCollector")
    process.ecalDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.ecalPreshowerDigis.sourceTag = cms.InputTag("rawDataCollector")
    process.gctDigis.inputLabel = cms.InputTag("rawDataCollector")
    process.gtDigis.DaqGtInputTag = cms.InputTag("rawDataCollector")
    process.gtEvmDigis.EvmGtInputTag = cms.InputTag("rawDataCollector")
    process.hcalDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.muonCSCDigis.InputObjects = cms.InputTag("rawDataCollector")
    process.muonDTDigis.inputLabel = cms.InputTag("rawDataCollector")
    process.muonRPCDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.scalersRawToDigi.scalersInputTag = cms.InputTag("rawDataCollector")
    process.siPixelDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.siStripDigis.ProductLabel = cms.InputTag("rawDataCollector")



    process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(
             SelectEvents = cms.vstring('HLT_L1*',
                                        'HLT_Jet*',
                                        'HLT_*Cosmic*',
                                        'HLT_HT*',
                                        'HLT_MinBias_*',
                                        'HLT_Physics*',
                                        'HLT_ZeroBias*')
                                      )

    process.load("Configuration.StandardSequences.Reconstruction_cff")
    process.load("RecoVertex.PrimaryVertexProducer.OfflinePixel3DPrimaryVertices_cfi")
    process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")


    process.dqmBeamSpotProblemMonitor.OnlineMode = True              
    process.dqmBeamSpotProblemMonitor.AlarmONThreshold =  10
    process.dqmBeamSpotProblemMonitor.AlarmOFFThreshold = 12

    #Set true only if doing test at playback or localy
    process.dqmBeamSpotProblemMonitor.doTest = True
    process.dqmBeamSpotProblemMonitor.nCosmicTrk = 10
    #pixel  track/vertices reco
    process.pixelVertices.TkFilterParameters.minPt = process.pixelTracks.RegionFactoryPSet.RegionPSet.ptMin

    process.offlinePrimaryVertices.TrackLabel = cms.InputTag("pixelTracks")

    process.tracking_FirstStep  = cms.Sequence(process.siPixelDigis* 
                                               process.offlineBeamSpot*
                                               process.siPixelClusters*
                                               process.siPixelRecHits*
                                               process.pixelTracks*
                                               process.pixelVertices
                                           )

    #--pixel tracking ends here-----

    process.p = cms.Path(process.scalersRawToDigi
                         *process.hltTriggerTypeFilter
                         *process.dqmcommon
                         *process.tracking_FirstStep
                         *process.monitor)

#-----------
# For Cosmic
#-----------

if (process.runType.getRunType() == process.runType.cosmic_run):

    print "Running Cosmic"

    process.castorDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.csctfDigis.producer = cms.InputTag("rawDataCollector")
    process.dttfDigis.DTTF_FED_Source = cms.InputTag("rawDataCollector")
    process.ecalDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.ecalPreshowerDigis.sourceTag = cms.InputTag("rawDataCollector")
    process.gctDigis.inputLabel = cms.InputTag("rawDataCollector")
    process.gtDigis.DaqGtInputTag = cms.InputTag("rawDataCollector")
    process.gtEvmDigis.EvmGtInputTag = cms.InputTag("rawDataCollector")
    process.hcalDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.muonCSCDigis.InputObjects = cms.InputTag("rawDataCollector")
    process.muonDTDigis.inputLabel = cms.InputTag("rawDataCollector")
    process.muonRPCDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.scalersRawToDigi.scalersInputTag = cms.InputTag("rawDataCollector")
    process.siPixelDigis.InputLabel = cms.InputTag("rawDataCollector")
    process.siStripDigis.ProductLabel = cms.InputTag("rawDataCollector")



    process.DQMEventStreamHttpReader.SelectEvents = cms.untracked.PSet(
             SelectEvents = cms.vstring('HLT_L1*',
                                        'HLT_Jet*',
                                        'HLT_*Cosmic*',
                                        'HLT_HT*',
                                        'HLT_MinBias_*',
                                        'HLT_Physics*',
                                        'HLT_ZeroBias*')
                                      )

    process.load("Configuration.StandardSequences.Reconstruction_cff")
    process.load("RecoVertex.PrimaryVertexProducer.OfflinePixel3DPrimaryVertices_cfi")
    process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")


    process.dqmBeamSpotProblemMonitor.OnlineMode = True              
    process.dqmBeamSpotProblemMonitor.AlarmONThreshold =  10
    process.dqmBeamSpotProblemMonitor.AlarmOFFThreshold = 8   #<----ALARM will be off always

    #Set true only if doing test at playback or localy
    process.dqmBeamSpotProblemMonitor.doTest = False
    process.dqmBeamSpotProblemMonitor.nCosmicTrk = 10
    #pixel  track/vertices reco
    process.pixelVertices.TkFilterParameters.minPt = process.pixelTracks.RegionFactoryPSet.RegionPSet.ptMin

    process.offlinePrimaryVertices.TrackLabel = cms.InputTag("pixelTracks")

    process.tracking_FirstStep  = cms.Sequence(process.siPixelDigis* 
                                               process.offlineBeamSpot*
                                               process.siPixelClusters*
                                               process.siPixelRecHits*
                                               process.pixelTracks*
                                               process.pixelVertices
                                           )

    #--pixel tracking ends here-----

    process.p = cms.Path(process.scalersRawToDigi
                         *process.hltTriggerTypeFilter
                         *process.dqmcommon
                         *process.tracking_FirstStep
                         *process.monitor)


