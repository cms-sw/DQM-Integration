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

def l1t_rct_single(i, dir, name):
  i["L1T/Layouts/03-RCT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_csctf_single(i, dir, name):
  i["L1T/Layouts/04-CSCTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_dttf_single(i, dir, name):
  i["L1T/Layouts/05-DTTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_rpctf_single(i, dir, name):
  i["L1T/Layouts/06-RPCTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 



# list of summary GT histograms (dqmitems, dirPath , histoName)
l1t_gt_single(dqmitems, "L1TGT", "algo_bits")
l1t_gt_single(dqmitems, "L1TGT", "algo_bits_corr")
l1t_gt_single(dqmitems, "L1TGT", "algo_bits_lumi")
l1t_gt_single(dqmitems, "L1TGT", "event_lumi")
l1t_gt_single(dqmitems, "L1TGT", "orbit_lumi")
l1t_gt_single(dqmitems, "L1TGT", "evnum_trignum_lumi")
l1t_gt_single(dqmitems, "L1TGT", "dbx_module")
l1t_gt_single(dqmitems, "L1TGT", "event_type")

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
l1t_gct_single(dqmitems, "L1TGCT", "CenJetsEtEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "ForJetsEtEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "TauJetsEtEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "IsoEmRankEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "NonIsoEmRankEtaPhi")
l1t_gct_single(dqmitems, "L1TGCT", "CenJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "ForJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "TauJetsRank")
l1t_gct_single(dqmitems, "L1TGCT", "IsoEmRank")
l1t_gct_single(dqmitems, "L1TGCT", "NonIsoEmRank")
l1t_gct_single(dqmitems, "L1TGCT", "EtMiss")
l1t_gct_single(dqmitems, "L1TGCT", "EtTotal")
l1t_gct_single(dqmitems, "L1TGCT", "EtHad")
l1t_gct_single(dqmitems, "L1TGCT", "HFRing0Corr")
l1t_gct_single(dqmitems, "L1TGCT", "HFRing1Corr")
l1t_gct_single(dqmitems, "L1TGCT", "HFTowerCountCorr")

# list of summary RCT histograms (dqmitems, dirPath , histoName)
l1t_rct_single(dqmitems, "L1TRCT", "RctIsoEmOccEtaPhi")
l1t_rct_single(dqmitems, "L1TRCT", "RctNonIsoEmOccEtaPhi")
l1t_rct_single(dqmitems, "L1TRCT", "RctIsoEmRank")
l1t_rct_single(dqmitems, "L1TRCT", "RctNonIsoEmRank")

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

# list of summary DTTF histograms (dqmitems, dirPath , histoName)
#l1t_dttf_single(dqmitems, "EventInfo/errorSummarySegments", "DT_TPG_phi_map")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Occupancy Summary")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Occupancy Phi vs Eta")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Phi")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Eta")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Pt")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Charge")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated Packed Quality")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Integrated BX")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Num Tracks Per Event")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "BX Summary")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "2nd Track Summary")
l1t_dttf_single(dqmitems, "L1TDTTF/DTTF_TRACKS/INTEG", "Fractional High Quality Summary")

#l1tlayout(dqmitems, "GT-Summary",
#  ["L1T/L1TGT/algo_bits"])

#l1tlayout(dqmitems, "GMT-Summary",
#  ["L1T/L1TGMT/GMT_eta",
#  "L1T/L1TGMT/GMT_phi",
#  "L1T/L1TGMT/Regional_trigger"])

#l1tlayout(dqmitems, "GCT-Summary",
#          ["L1T/EventInfo/errorSummarySegments/IsoEmRankEtaPhiSumm",
#	  "L1T/EventInfo/errorSummarySegments/NonIsoEmRankEtaPhiSumm"])

#l1tlayout(dqmitems, "CSCTF-Summary",
#  ["L1T/L1TCSCTF/CSCTF_errors",
#   "L1T/L1TCSCTF/CSCTF_occupancies"])

#l1tlayout(dqmitems, "DTTF-Summary",
#  ["L1T/EventInfo/errorSummarySegments/DT_TPG_phi_map"])

