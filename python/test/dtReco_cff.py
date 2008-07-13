import FWCore.ParameterSet.Config as cms

from Geometry.CMSCommonData.cmsIdealGeometryXML_cfi import *
from Geometry.DTGeometry.dtGeometry_cfi import *
from Geometry.CSCGeometry.cscGeometry_cfi import *
from Geometry.MuonNumbering.muonNumberingInitialization_cfi import *
from RecoLocalMuon.DTRecHit.dt1DRecHits_LinearDrift_CosmicData_cfi import *
from RecoLocalMuon.DTSegment.dt2DSegments_CombPatternReco2D_LinearDrift_CosmicData_cfi import *
from RecoLocalMuon.DTSegment.dt4DSegments_CombPatternReco4D_LinearDrift_CosmicData_cfi import *
dtunpacker = cms.EDFilter("DTUnpackingModule",
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

DTMapping = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
    ),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('DTReadOutMappingRcd'),
        tag = cms.string('map_CRUZET')
    ), 
        cms.PSet(
            record = cms.string('DTT0Rcd'),
            tag = cms.string('t0_GRUMM_hlt')
        ), 
        cms.PSet(
            record = cms.string('DTStatusFlagRcd'),
            tag = cms.string('noise_CRUZET_hlt')
        ), 
        cms.PSet(
            record = cms.string('DTTtrigRcd'),
            tag = cms.string('tTrig_CRUZET_hlt')
        )),
    connect = cms.string('frontier://(proxyurl=http://localhost:3128)(serverurl=http://frontier1.cms:8000/FrontierOnProd)(serverurl=http://frontier2.cms:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_20X_DT')
)


