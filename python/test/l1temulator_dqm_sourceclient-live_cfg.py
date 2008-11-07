import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TEmuDQMlive")

process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("DQM.Integration.test.inputsource_cfi")
process.load("DQM.Integration.test.environment_cfi")

process.load("DQM.L1TMonitor.L1TEmulatorMonitor_cff")    
process.load("DQM.L1TMonitorClient.L1TEMUMonitorClient_cff")    

#extra config:
process.EcalTrigPrimESProducer.DatabaseFile = 'TPG_startup.txt.gz'

#specify subsystems with qt's to be temporarily masked in summary map
#sequence: dtf,dtp,ctf,ctp,rpc,gmt, etp,htp,rct,gct,gt
process.l1temuEventInfoClient.maskedSystems = [0,1,1,0,0,0, 0,1,0,0,1]

#Updated GLOBAL TAG to be specified by central OPERATIONS here!
process.GlobalTag.globaltag = 'CRAFT_V2H::All'
process.GlobalTag.connect = 'frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG'

#replace DQMStore.referenceFileName = "L1TEMU_reference.root"
process.EventStreamHttpReader.SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring("*")
)
process.EventStreamHttpReader.consumerName = 'L1TEMU DQM Consumer'
process.dqmEnv.subSystemFolder = 'L1TEMU'
