import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
#----------------------------
# Event Source
#-----------------------------
process.load("DQM.Integration.test.inputsource_cfi")
process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("*")
)
    
#----------------------------
# DQM Environment
#-----------------------------
process.load("DQMServices.Core.DQM_cfg")

#replace DQMStore.referenceFileName = "L1T_reference.root"
process.load("DQMServices.Components.DQMEnvironment_cfi")

#----------------------------
# DQM Live Environment
#-----------------------------
process.load("DQM.Integration.test.environment_cfi")

#-----------------------------
#
#  DQM SOURCES
#
process.load("CondCore.DBCommon.CondDBSetup_cfi")

process.load("Configuration.StandardSequences.Geometry_cff")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("DQM.L1TMonitor.L1TMonitor_cff")

process.load("DQM.L1TMonitorClient.L1TMonitorClient_cff")
process.l1GtParameters.BstLengthBytes = 52

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.connect = "frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"   
process.GlobalTag.globaltag = 'CRZT210_V1H::All' # or any other appropriate
process.prefer("GlobalTag")


process.EventStreamHttpReader.consumerName = 'L1T DQM Consumer'
process.dqmEnv.subSystemFolder = 'L1T'

