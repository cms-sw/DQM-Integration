def l1tlayout(i, p, *rows): i["L1T/Layouts/" + p] = DQMItem(layout=rows)

def l1t_gt_single(i, dir, name):
  i["L1T/Layouts/00-GT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_gmt_single(i, dir, name):
  i["L1T/Layouts/01-GMT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_gct_single(i, dir, name):
  i["L1T/Layouts/02-GCT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

#def l1t_rct_single(i, dir, name):
#  i["L1T/Layouts/03-RCT-Summary/%s" % name] = \
#    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_csctf_single(i, dir, name):
  i["L1T/Layouts/04-CSCTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

#def l1t_dttf_single(i, dir, name):
#  i["L1T/Layouts/05-DTTF-Summary/%s" % name] = DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 
def l1t_dttf_single(i, p, *rows): i["L1T/Layouts/05-DTTF-Summary/" + p] = DQMItem(layout=rows)

def l1t_rpctf_single(i, dir, name):
  i["L1T/Layouts/06-RPCTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_scal_single(i, p, *rows): i["L1T/Layouts/07-SCAL4Cosmics-Summary/" + p] = DQMItem(layout=rows)

def l1t_rct_expert(i, p, *rows): i["L1T/Layouts/03-RCT-Summary/" + p] = DQMItem(layout=rows)
l1t_rct_expert(dqmitems, "RctEmIsoEmEtEtaPhi",
  [{ 'path': "L1T/L1TRCT/RctEmIsoEmEtEtaPhi", 'description': "For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "RctEmNonIsoEmEtEtaPhi",
  [{ 'path': "L1T/L1TRCT/RctEmNonIsoEmEtEtaPhi", 'description': "For description see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a>  CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "RctRegionsEtEtaPhi",
  [{ 'path': "L1T/L1TRCT/RctRegionsEtEtaPhi", 'description': "For description see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])


def l1t_summary(i, p, *rows): i["L1T/Layouts/08-L1T-Summary/" + p] = DQMItem(layout=rows)

l1t_summary(dqmitems,"00 Physics Trigger Rate",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/Physics Trigger Rate", 'description': "Physics Trigger Rate. x-axis: Time(lumisection); y-axis: Rate (Hz).  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1t_summary(dqmitems,"01 Random Trigger Rate",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/Random Trigger Rate", 'description': "Random Trigger Rate. x-axis: Time(lumisection); y-axis: Rate (Hz).  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])



# list of summary GT histograms (dqmitems, dirPath , histoName)
l1t_gt_single(dqmitems, "L1TGT", "algo_bits")
l1t_gt_single(dqmitems, "L1TGT", "tt_bits")
l1t_gt_single(dqmitems, "L1TGT", "gtfe_bx")
l1t_gt_single(dqmitems, "L1Scalers_SM", "l1AlgoBits_Vs_Bx")
l1t_gt_single(dqmitems, "L1Scalers_SM", "l1TechBits_Vs_Bx")
l1t_gt_single(dqmitems, "BXSynch", "BxOccyGtTrigType1")

# list of summary GMT histograms (dqmitems, dirPath , histoName)
l1t_gmt_single(dqmitems, "L1TGMT", "DTTF_phi")
l1t_gmt_single(dqmitems, "L1TGMT", "CSC_eta")
l1t_gmt_single(dqmitems, "L1TGMT", "RPCb_phi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_phi")
l1t_gmt_single(dqmitems, "L1TGMT", "DTTF_candlumi")
l1t_gmt_single(dqmitems, "L1TGMT", "CSCTF_candlumi")
l1t_gmt_single(dqmitems, "L1TGMT", "RPCb_candlumi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_candlumi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_etaphi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_qty")
l1t_gmt_single(dqmitems, "L1TGMT", "n_RPCb_vs_DTTF")
l1t_gmt_single(dqmitems, "L1TGMT", "Regional_trigger")

# list of summary GCT histograms (dqmitems, dirPath , histoName)
l1t_gct_single(dqmitems, "L1TGCT", "AllEtEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "TauJetsEtEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "IsoEmRankEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "NonIsoEmRankEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "CenJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "ForJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "TauJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "IsoEmRank")
l1t_gct_single(dqmitems, "L1TGCT", "NonIsoEmRank")
l1t_gct_single(dqmitems, "L1TGCT", "EtMiss")
l1t_gct_single(dqmitems, "L1TGCT", "HtMiss")
l1t_gct_single(dqmitems, "L1TGCT", "EtTotal")
l1t_gct_single(dqmitems, "L1TGCT", "EtHad")

# list of summary RCT histograms (dqmitems, dirPath , histoName)
#l1t_rct_single(dqmitems, "L1TRCT", "RctIsoEmOccEtaPhi")
#l1t_rct_single(dqmitems, "L1TRCT", "RctNonIsoEmOccEtaPhi")
#l1t_rct_single(dqmitems, "L1TRCT", "RctIsoEmRank")
#l1t_rct_single(dqmitems, "L1TRCT", "RctNonIsoEmRank")

# list of summary CSCTF histograms (dqmitems, dirPath , histoName)
l1t_csctf_single(dqmitems, "L1TCSCTF", "CSCTF_errors")
l1t_csctf_single(dqmitems, "L1TCSCTF", "CSCTF_occupancies")

# list of summary RPC histograms (dqmitems, dirPath , histoName)
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_muons_tower_phipacked")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_phi_valuepacked")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_ntrack")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_quality")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_charge_value")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_pt_value")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCTF_bx")
l1t_rpctf_single(dqmitems, "L1TRPCTF", "RPCDigi_bx")

#### list of summary DTTF histograms (dqmitems, dirPath , histoName)
## l1t_dttf_single(dqmitems, "EventInfo/errorSummarySegments", "DT_TPG_phi_map")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Occupancy Summary")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Occupancy Phi vs Eta")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Phi")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Eta")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Pt")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Charge")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Quality")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated BX")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Num Tracks Per Event")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "BX Summary")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "2nd Track Summary")
## l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Fractional High Quality Summary")




#l1t_dttf_single(dqmitems, "DTTF Occupancy Summary",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_03_tracks_distr_summary", 'description' :  "DTTF occupancy plot (divided by the total number of events with a DTTF track) for each sector of each logical wheel. The N0 boards get less than 10% tracks than the corresponding P0: the blue color is normal there. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
#l1t_dttf_single(dqmitems, "Occupancy Phi vs Eta",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_phi_eta_fine_summary", 'description' : "Integrated occupancy (proportionate to total number of events with a DTTF track) - phi vs eta.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
#l1t_dttf_single(dqmitems, "Integrated Packed Phi",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_phi_integ", 'description' : "Integrated Paced Phi. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
#l1t_dttf_single(dqmitems, "Integrated Packed Eta",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_eta_integ", 'description' : "Integrated Packed Eta. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
#l1t_dttf_single(dqmitems, "Integrated Packed Pt",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_pt_integ", 'description' : "Integrated Packed Pt.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
#l1t_dttf_single(dqmitems, "Integrated Packed Charge",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_q_integ", 'description' : "Integrated Packed Charge. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
#l1t_dttf_single(dqmitems, "Integrated Packed Quality",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_qual_integ", 'description' : "Integrated Packed Quality. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
#l1t_dttf_single(dqmitems, "Integrated BX",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_bx_integ", 'description' : "Integrated BX plot. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>"}])
#l1t_dttf_single(dqmitems, "Num Tracks Per Event",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_nTracksPerEvent_integ", 'description' : "Integrated number of tracks per event. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>"}])
#l1t_dttf_single(dqmitems, "BX Summary",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_bx_summary", 'description' : "Summary of BX's for each wheel (proportionate to total number of events with a DTTF track). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>"}])
#l1t_dttf_single(dqmitems, "2nd Track Summary",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_2ndtrack_occupancy_summary", 'description' : "Number of 2nd tracks (proportionate to total number of events that have a DTTF track) - Sector vs Logical Wheel.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>"}])
#l1t_dttf_single(dqmitems, "Fractional High Quality Summary",
#               [{'path':"L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_highQual_summary", 'description' : "Fractional high quality (qual>3) (proportional to total bin occupancy) summary - Sector vs Logical Wheel.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\" target=\"_blank\">here</a>"}])


l1t_dttf_single(dqmitems,  "01 - Number of Tracks per Event",
           [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_01_nTracksPerEvent_integ", 'description' : "Number of DTTF Tracks Per Event. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "02 - Fraction of tracks per wheel",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_02_nTracks", 'description' : "DTTF Tracks per Wheel distribution. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "03 - DTTF Occupancy Summary",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_03_tracks_distr_summary", 'description' : "DTTF Tracks distribution by Sector and Wheel (blue in P0 normal: it has <10%% of P0 tracks). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "04 - Tracks BX Distribution by Wheel",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_05_bx_distr", 'description' : "DTTF Tracks BX Distribution by Wheel. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
  
l1t_dttf_single(dqmitems,  "05 - Fraction of Tracks BX w.r.t. Tracks with BX=0",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_06_bx", 'description' : "Fraction of DTTF Tracks BX w.r.t. Tracks with BX=0. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "06 - Tracks Quality distribution",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_07_quality", 'description' : "DTTF Tracks Quality distribution. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "07 - Quality distribution by wheel",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_08_quality_distr", 'description' : "DTTF Tracks Quality distribution by wheel. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "08 - High Quality Tracks fraction",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_09_highQualTracks_distr", 'description' : "Fraction of DTTF Tracks with Quality>2 by Sector and Wheel. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "09 - Tracks Quality vs Eta",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_10_qual_eta_distr", 'description' : "DTTF Tracks Quality vs Eta Distribution. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "10 - Occupancy Phi vs Eta-Coarse",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_11_phi_eta_coarse_distr", 'description' : "#eta-#phi Distribution of DTTF Tracks with coarse #eta assignment (packed values). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "11 - Occupancy Phi vs Eta-Fine",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_12_phi_etaFine_distr", 'description' : "#eta-#phi Distribution of DTTF Tracks with fine #eta assignment (packed values). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "12 - Occupancy Phi vs Eta",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_13_phi_eta_distr", 'description' : "#eta-#phi Distribution of DTTF Tracks. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "13 - Fraction of tracks with Eta fine assigment",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_14_eta_fine_fraction", 'description' : "Fraction of DTTF Tracks with Fine #eta Assignment. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "14 - Integrated Packed Eta",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_15_eta", 'description' : "DTTF Tracks #eta distribution (Packed values). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "15 - Integrated Packed Phi",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_16_phi", 'description' : "DTTF Tracks Phi distribution (Packed values). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "16 - Integrated Packed pT",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_17_pt", 'description' : "DTTF Tracks p_{T} distribution (Packed values). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "17 - Integrated Packed Charge",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_18_q", 'description' : "DTTF Tracks Charge distribution. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "18 - 2nd Track Summary",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/INCLUSIVE/dttf_19_2ndTrack_distr_summary", 'description' : "DTTF 2nd Tracks Only Distribution by Sector and Wheel w.r.t. the total Number of tracks. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "19 - DTTF to GMT match ratio",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/GMT_MATCH/dttf_gmt_fract_matching", 'description' : "Fraction of DTTF tracks matching with GMT tracks. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "20 - DTTF tracks not matching with GMT",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/GMT_MATCH/dttf_tracks_without_gmt_match", 'description' : "DTTF Tracks Without a Match in GMT. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "21 - DTTF tracks matching with GMT",
                [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/GMT_MATCH/dttf_tracks_with_gmt_match", 'description' : "DTTF Tracks With a Match in GMT. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])

l1t_dttf_single(dqmitems,  "22 - GMT Tracks Without DTTF Track",
                  [{'path' : "L1T/L1TDTTF/DTTF_TRACKS/GMT_MATCH/dttf_missing_tracks_in_gmt", 'description' : "GMT Tracks Without a Corresponding Track in DTTF. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/L1DQM#DT_TF_monitor\"  target=\"_blank\">here</a>."}])
  





# list of summary SCAL histograms (dqmitems, dirPath , histoName)
l1t_scal_single(dqmitems, "Rate_AlgoBit_002",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_002", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_003",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_003", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_004",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_004", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_005",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_005", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_006",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_006", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_007",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_007", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_008",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_008", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_009",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_009", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_010",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_010", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_011",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_011", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_012",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_012", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_013",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_013", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_015",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_015", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_016",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_016", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_045",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_045", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_054",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_054", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_055",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_055", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_056",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_056", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_057",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_057", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_058",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_058", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_059",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_059", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_060",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_060", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_061",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_061", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_062",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_062", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_063",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_063", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_065",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_065", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_068",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_068", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_070",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_070", 'description' :  "none"}])
l1t_scal_single(dqmitems, "Rate_AlgoBit_088",
               [{'path':"L1T/L1TScalersSCAL/Level1TriggerRates/AlgorithmRates/Rate_AlgoBit_088", 'description' :  "none"}])

# GCT expert layouts
def gct_expert_cenjets_layout (i, p, *rows): i["L1T/Layouts/10 GCT Expert/01 Central Jets/" + p] = DQMItem(layout=rows)
def gct_expert_forjets_layout (i, p, *rows): i["L1T/Layouts/10 GCT Expert/02 Forward Jets/" + p] = DQMItem(layout=rows)
def gct_expert_taujets_layout (i, p, *rows): i["L1T/Layouts/10 GCT Expert/03 Tau Jets/" + p] = DQMItem(layout=rows)
def gct_expert_isoem_layout   (i, p, *rows): i["L1T/Layouts/10 GCT Expert/04 Iso EM/" + p] = DQMItem(layout=rows)
def gct_expert_nonisoem_layout(i, p, *rows): i["L1T/Layouts/10 GCT Expert/05 Non-Iso EM/" + p] = DQMItem(layout=rows)
def gct_expert_met_layout     (i, p, *rows): i["L1T/Layouts/10 GCT Expert/06 MET/" + p] = DQMItem(layout=rows)
def gct_expert_mht_layout     (i, p, *rows): i["L1T/Layouts/10 GCT Expert/07 MHT/" + p] = DQMItem(layout=rows)
def gct_expert_et_layout      (i, p, *rows): i["L1T/Layouts/10 GCT Expert/08 SumET/" + p] = DQMItem(layout=rows)
def gct_expert_ht_layout      (i, p, *rows): i["L1T/Layouts/10 GCT Expert/09 HT/" + p] = DQMItem(layout=rows)
def gct_expert_hfsums_layout  (i, p, *rows): i["L1T/Layouts/10 GCT Expert/10 HF Ring ET Sums/" + p] = DQMItem(layout=rows)
def gct_expert_hfcnts_layout  (i, p, *rows): i["L1T/Layouts/10 GCT Expert/11 HF Ring Tower Counts/" + p] = DQMItem(layout=rows)

gct_expert_cenjets_layout(dqmitems,"CenJetsOccEtaPhi",[{'path': "L1T/L1TGCT/CenJetsOccEtaPhi", 'description': "Eta-phi map of central-jet occupancy" }])
gct_expert_cenjets_layout(dqmitems,"CenJetsEtEtaPhi", [{'path': "L1T/L1TGCT/CenJetsEtEtaPhi",  'description': "Eta-phi map of Et-weighted central-jet occupancy" }])
gct_expert_cenjets_layout(dqmitems,"CenJetsOccEta",   [{'path': "L1T/L1TGCT/CenJetsOccEta",    'description': "Eta distribution for central jets" }])
gct_expert_cenjets_layout(dqmitems,"CenJetsOccPhi",   [{'path': "L1T/L1TGCT/CenJetsOccPhi",    'description': "Phi distribution for central jets" }])
gct_expert_cenjets_layout(dqmitems,"CenJetsRank",     [{'path': "L1T/L1TGCT/CenJetsRank",      'description': "Et distribution for central jets" }])
gct_expert_cenjets_layout(dqmitems,"AllJetsOccRankBx",[{'path': "L1T/L1TGCT/AllJetsOccRankBx", 'description': "Et distribution for all jets as a function of BX" }])

gct_expert_forjets_layout(dqmitems,"ForJetsOccEtaPhi",[{'path': "L1T/L1TGCT/ForJetsOccEtaPhi", 'description': "Eta-phi map of forward-jet occupancy" }])
gct_expert_forjets_layout(dqmitems,"ForJetsEtEtaPhi", [{'path': "L1T/L1TGCT/ForJetsEtEtaPhi",  'description': "Eta-phi map of Et-weighted forward-jet occupancy" }])
gct_expert_forjets_layout(dqmitems,"ForJetsOccEta",   [{'path': "L1T/L1TGCT/ForJetsOccEta",    'description': "Eta distribution for forward jets" }])
gct_expert_forjets_layout(dqmitems,"ForJetsOccPhi",   [{'path': "L1T/L1TGCT/ForJetsOccPhi",    'description': "Phi distribution for forward jets" }])
gct_expert_forjets_layout(dqmitems,"ForJetsRank",     [{'path': "L1T/L1TGCT/ForJetsRank",      'description': "Et distribution for forward jets" }])
gct_expert_forjets_layout(dqmitems,"AllJetsOccRankBx",[{'path': "L1T/L1TGCT/AllJetsOccRankBx", 'description': "Et distribution for all jets as a function of BX" }])

gct_expert_taujets_layout(dqmitems,"TauJetsOccEtaPhi",[{'path': "L1T/L1TGCT/TauJetsOccEtaPhi", 'description': "Eta-phi map of tau-jet occupancy" }])
gct_expert_taujets_layout(dqmitems,"TauJetsEtEtaPhi", [{'path': "L1T/L1TGCT/TauJetsEtEtaPhi",  'description': "Eta-phi map of Et-weighted tau-jet occupancy" }])
gct_expert_taujets_layout(dqmitems,"TauJetsOccEta",   [{'path': "L1T/L1TGCT/TauJetsOccEta",    'description': "Eta distribution for tau jets" }])
gct_expert_taujets_layout(dqmitems,"TauJetsOccPhi",   [{'path': "L1T/L1TGCT/TauJetsOccPhi",    'description': "Phi distribution for tau jets" }])
gct_expert_taujets_layout(dqmitems,"TauJetsRank",     [{'path': "L1T/L1TGCT/TauJetsRank",      'description': "Et distribution for tau jets" }])
gct_expert_taujets_layout(dqmitems,"AllJetsOccRankBx",[{'path': "L1T/L1TGCT/AllJetsOccRankBx", 'description': "Et distribution for all jets as a function of BX" }])

gct_expert_isoem_layout(dqmitems,"IsoEmOccEtaPhi",    [{'path': "L1T/L1TGCT/IsoEmOccEtaPhi",  'description': "Eta-phi map of isolated electron/photon occupancy" }])
gct_expert_isoem_layout(dqmitems,"IsoEmRankEtaPhi",   [{'path': "L1T/L1TGCT/IsoEmRankEtaPhi", 'description': "Eta-phi map of Et-weighted isolated electron/photon occupancy" }])
gct_expert_isoem_layout(dqmitems,"IsoEmOccEta",       [{'path': "L1T/L1TGCT/IsoEmOccEta",    'description': "Eta distribution for isolated electrons/photons" }])
gct_expert_isoem_layout(dqmitems,"IsoEmOccPhi",       [{'path': "L1T/L1TGCT/IsoEmOccPhi",    'description': "Phi distribution for isolated electrons/photons" }])
gct_expert_isoem_layout(dqmitems,"IsoEmRank",         [{'path': "L1T/L1TGCT/IsoEmRank",      'description': "Et distribution for isolated electrons/photons" }])
gct_expert_isoem_layout(dqmitems,"AllEmOccRankBx",    [{'path': "L1T/L1TGCT/AllEmOccRankBx", 'description': "Et distribution for all electrons/photons as a function of BX" }])

gct_expert_nonisoem_layout(dqmitems,"NonIsoEmOccEtaPhi", [{'path': "L1T/L1TGCT/NonIsoEmOccEtaPhi", 'description': "Eta-phi map of non-isolated electron/photon occupancy" }])
gct_expert_nonisoem_layout(dqmitems,"NonIsoEmRankEtaPhi",[{'path': "L1T/L1TGCT/NonIsoEmRankEtaPhi", 'description': "Eta-phi map of Et-weighted non-isolated electron/photon occupancy" }])
gct_expert_nonisoem_layout(dqmitems,"NonIsoEmOccEta", [{'path': "L1T/L1TGCT/NonIsoEmOccEta", 'description': "Eta distribution for non-isolated electrons/photons" }])
gct_expert_nonisoem_layout(dqmitems,"NonIsoEmOccPhi", [{'path': "L1T/L1TGCT/NonIsoEmOccPhi", 'description': "Phi distribution for non-isolated electrons/photons" }])
gct_expert_nonisoem_layout(dqmitems,"NonIsoEmRank",   [{'path': "L1T/L1TGCT/NonIsoEmRank",   'description': "Et distribution for non-isolated electrons/photons" }])
gct_expert_nonisoem_layout(dqmitems,"AllEmOccRankBx", [{'path': "L1T/L1TGCT/AllEmOccRankBx", 'description': "Et distribution for all electrons/photons as a function of BX" }])

gct_expert_met_layout(dqmitems,"EtMiss",              [{'path': "L1T/L1TGCT/EtMiss",              'description': "MET distribution" }])
gct_expert_met_layout(dqmitems,"EtMissOf",            [{'path': "L1T/L1TGCT/EtMissOf",            'description': "MET overflow bit" }])
gct_expert_met_layout(dqmitems,"EtMissPhi",           [{'path': "L1T/L1TGCT/EtMissPhi",           'description': "MET phi" }])
gct_expert_met_layout(dqmitems,"EtMissOccBx",         [{'path': "L1T/L1TGCT/EtMissOccBx",         'description': "MET distribution as a function of BX" }])
gct_expert_met_layout(dqmitems,"EtMissHtMissCorr",    [{'path': "L1T/L1TGCT/EtMissHtMissCorr",    'description': "Correlation between MET and MHT" }])
gct_expert_met_layout(dqmitems,"EtMissHtMissPhiCorr", [{'path': "L1T/L1TGCT/EtMissHtMissPhiCorr", 'description': "Correlation between MET and MHT phi" }])

gct_expert_mht_layout(dqmitems,"HtMiss",              [{'path': "L1T/L1TGCT/HtMiss",              'description': "MHT distribution" }])
gct_expert_mht_layout(dqmitems,"HtMissOf",            [{'path': "L1T/L1TGCT/HtMissOf",            'description': "MHT overflow bit" }])
gct_expert_mht_layout(dqmitems,"HtMissPhi",           [{'path': "L1T/L1TGCT/HtMissPhi",           'description': "MHT phi" }])
gct_expert_mht_layout(dqmitems,"HtMissOccBx",         [{'path': "L1T/L1TGCT/HtMissOccBx",         'description': "MHT distribution as a function of BX" }])
gct_expert_mht_layout(dqmitems,"EtMissHtMissCorr",    [{'path': "L1T/L1TGCT/EtMissHtMissCorr",    'description': "Correlation between MET and MHT" }])
gct_expert_mht_layout(dqmitems,"EtMissHtMissPhiCorr", [{'path': "L1T/L1TGCT/EtMissHtMissPhiCorr", 'description': "Correlation between MET and MHT phi" }])

gct_expert_et_layout(dqmitems,"EtTotal",              [{'path': "L1T/L1TGCT/EtTotal",              'description': "Sum ET distribution" }])
gct_expert_et_layout(dqmitems,"EtTotalOf",            [{'path': "L1T/L1TGCT/EtTotalOf",            'description': "Sum ET overflow bit" }])
gct_expert_et_layout(dqmitems,"EtTotalOccBx",         [{'path': "L1T/L1TGCT/EtTotalOccBx",         'description': "Sum ET distribution as a function of BX" }])
gct_expert_et_layout(dqmitems,"EtTotalEtHadCorr",     [{'path': "L1T/L1TGCT/EtTotalEtHadCorr",     'description': "Correlation between sum ET and HT" }])

gct_expert_ht_layout(dqmitems,"EtHad",                [{'path': "L1T/L1TGCT/EtHad",                'description': "HT distribution" }])
gct_expert_ht_layout(dqmitems,"EtHadOf",              [{'path': "L1T/L1TGCT/EtHadOf",              'description': "HT overflow bit" }])
gct_expert_ht_layout(dqmitems,"EtHadOccBx"  ,         [{'path': "L1T/L1TGCT/EtHadOccBx",           'description': "HT distribution as a function of BX" }])
gct_expert_ht_layout(dqmitems,"EtTotalEtHadCorr",     [{'path': "L1T/L1TGCT/EtTotalEtHadCorr",     'description': "Correlation between sum ET and HT" }])

gct_expert_hfsums_layout(dqmitems,"HFRing1ETSumPosEta",[{'path': "L1T/L1TGCT/HFRing1ETSumPosEta",  'description': "HF ring 1 ET sum for positive eta" }])
gct_expert_hfsums_layout(dqmitems,"HFRing1ETSumNegEta",[{'path': "L1T/L1TGCT/HFRing1ETSumNegEta",  'description': "HF ring 1 ET sum for negative eta" }])
gct_expert_hfsums_layout(dqmitems,"HFRing2ETSumPosEta",[{'path': "L1T/L1TGCT/HFRing2ETSumPosEta",  'description': "HF ring 2 ET sum for positive eta" }])
gct_expert_hfsums_layout(dqmitems,"HFRing2ETSumNegEta",[{'path': "L1T/L1TGCT/HFRing2ETSumNegEta",  'description': "HF ring 2 ET sum for negative eta" }])
gct_expert_hfsums_layout(dqmitems,"HFRing1Corr",[{'path': "L1T/L1TGCT/HFRing1Corr",  'description': "Correlation between HF ring 1 ET sums for positive and negative eta" }])
gct_expert_hfsums_layout(dqmitems,"HFRing2Corr",[{'path': "L1T/L1TGCT/HFRing2Corr",  'description': "Correlation between HF ring 2 ET sums for positive and negative eta" }])
gct_expert_hfsums_layout(dqmitems,"HFRingRatioPosEta",[{'path': "L1T/L1TGCT/HFRingRatioPosEta",  'description': "Ratio of HF ring 1 ET to ring 2 ET for positive eta" }])
gct_expert_hfsums_layout(dqmitems,"HFRingRatioNegEta",[{'path': "L1T/L1TGCT/HFRingRatioNegEta",  'description': "Ratio of HF ring 1 ET to ring 2 ET for negative eta" }])
gct_expert_hfsums_layout(dqmitems,"HFRingETSumOccBx", [{'path': "L1T/L1TGCT/HFRingETSumOccBx",  'description': "All HF ring ET sums as a function of BX" }])

gct_expert_hfcnts_layout(dqmitems,"HFRing1TowerCountPosEta",[{'path': "L1T/L1TGCT/HFRing1TowerCountPosEta",  'description': "HF ring 1 tower count for positive eta" }])
gct_expert_hfcnts_layout(dqmitems,"HFRing1TowerCountNegEta",[{'path': "L1T/L1TGCT/HFRing1TowerCountNegEta",  'description': "HF ring 1 tower count for negative eta" }])
gct_expert_hfcnts_layout(dqmitems,"HFRing2TowerCountPosEta",[{'path': "L1T/L1TGCT/HFRing2TowerCountPosEta",  'description': "HF ring 2 tower count for positive eta" }])
gct_expert_hfcnts_layout(dqmitems,"HFRing2TowerCountNegEta",[{'path': "L1T/L1TGCT/HFRing2TowerCountNegEta",  'description': "HF ring 2 tower count for negative eta" }])
gct_expert_hfcnts_layout(dqmitems,"HFRing1TowerCountCorr",[{'path': "L1T/L1TGCT/HFRing1TowerCountCorr",  'description': "Correlation between HF ring 1 tower counts for positive and negative eta" }])
gct_expert_hfcnts_layout(dqmitems,"HFRing2TowerCountCorr",[{'path': "L1T/L1TGCT/HFRing2TowerCountCorr",  'description': "Correlation between HF ring 2 tower counts for positive and negative eta" }])
gct_expert_hfcnts_layout(dqmitems,"HFRingTowerCountOccBx", [{'path': "L1T/L1TGCT/HFRingTowerCountOccBx",  'description': "All HF ring tower counts as a function of BX" }])
