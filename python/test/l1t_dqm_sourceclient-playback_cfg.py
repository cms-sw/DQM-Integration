import FWCore.ParameterSet.Config as cms

process = cms.Process("DQM")
process.load("DQM.Integration.test.inputsource_playback_cfi")

process.load("DQMServices.Core.DQM_cfg")

process.load("DQMServices.Components.DQMEnvironment_cfi")

process.load("DQM.Integration.test.environment_playback_cfi")

process.load("CondCore.DBCommon.CondDBSetup_cfi")

process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")

process.load("Geometry.RPCGeometry.rpcGeometry_cfi")

process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.load("DQM.L1TMonitor.L1TMonitor_cff")

process.load("DQM.L1TMonitorClient.L1TMonitorClient_cff")

process.EventStreamHttpReader.consumerName = 'L1T DQM Consumer'
process.dqmEnv.subSystemFolder = 'L1T'

