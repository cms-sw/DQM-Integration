import FWCore.ParameterSet.Config as cms



# filter on trigger type
calibrationEventsFilter = cms.EDFilter("TriggerTypeFilter",
                                       InputLabel = cms.string('source'),
                                       TriggerFedId = cms.int32(812),
                                       # 1=Physics, 2=Calibration, 3=Random, 4=Technical
                                       SelectedTriggerType = cms.int32(1) 
                                       )

# DT digitization and reconstruction
from EventFilter.DTTFRawToDigi.dttfunpacker_cfi import *

dtunpacker = cms.EDProducer("DTUnpackingModule",
    dataType = cms.string('DDU'),
    useStandardFEDid = cms.untracked.bool(True),
    fedbyType = cms.untracked.bool(True),
    readOutParameters = cms.PSet(
        debug = cms.untracked.bool(False),
        rosParameters = cms.PSet(
            writeSC = cms.untracked.bool(True),
            readingDDU = cms.untracked.bool(True),
            performDataIntegrityMonitor = cms.untracked.bool(True),
            readDDUIDfromDDU = cms.untracked.bool(True),
            debug = cms.untracked.bool(False),
            localDAQ = cms.untracked.bool(False)
        ),
        localDAQ = cms.untracked.bool(False),
        performDataIntegrityMonitor = cms.untracked.bool(True)
    )
)

from Configuration.StandardSequences.Geometry_cff import *
from RecoLocalMuon.Configuration.RecoLocalMuonCosmics_cff import *
dt1DRecHits.dtDigiLabel = 'dtunpacker'
DTLinearDriftAlgo_CosmicData.recAlgoConfig.tTrigModeConfig.kFactor = -0.7


from Configuration.StandardSequences.FrontierConditions_GlobalTag_cff import *
#GlobalTag.globaltag = "CRZT210_V1::All" # or "IDEAL_V2::All" or... 
es_prefer_GlobalTag = cms.ESPrefer('PoolDBESSource','GlobalTag')

GlobalTag.connect ="frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_21X_GLOBALTAG"
GlobalTag.globaltag = "CRZT210_V1H::All"


# Data integrity
from DQM.DTMonitorModule.dtDataIntegrityTask_cfi import *
from DQM.DTMonitorClient.dtDataIntegrityTest_cfi import *

# Digi task
from DQM.DTMonitorModule.dtDigiTask_cfi import *
from DQM.DTMonitorClient.dtOccupancyTest_cfi import *
dtDigiMonitor.readDB = False 

# Local Trigger task
from DQM.DTMonitorModule.dtTriggerTask_cfi import *
from DQM.DTMonitorClient.dtLocalTriggerTest_cfi import *
dtTriggerMonitor.process_dcc = True
dtTriggerMonitor.dcc_label="dttfunpacker" 
    
# segment reco task
from DQM.DTMonitorModule.dtSegmentTask_cfi import *
from DQM.DTMonitorClient.dtSegmentAnalysisTest_cfi import *

# resolution task
from DQM.DTMonitorModule.dtResolutionTask_cfi import *

# noise task
from DQM.DTMonitorModule.dtNoiseTask_cfi import *
from DQM.DTMonitorClient.dtNoiseAnalysis_cfi import *

# report summary
from DQM.DTMonitorClient.dtSummaryClients_cfi import *

dtqTester = cms.EDFilter("QualityTester",
                         reportThreshold = cms.untracked.string('red'),
                         prescaleFactor = cms.untracked.int32(1),
                         qtList = cms.untracked.FileInPath('DQM/DTMonitorClient/test/QualityTests.xml'),
                         getQualityTestsFromFile = cms.untracked.bool(True)
                         )


reco = cms.Sequence(dtunpacker + dttfunpacker + dt1DRecHits + dt4DSegments)

dtDQMTask = cms.Sequence(dtDigiMonitor + dtSegmentAnalysisMonitor + dtTriggerMonitor + dtNoiseMonitor + dtResolutionAnalysisMonitor)

dtDQMTest = cms.Sequence( dataIntegrityTest + triggerTest + dtOccupancyTest + segmentTest + dtNoiseAnalysisMonitor + dtSummaryClients + dtqTester)

