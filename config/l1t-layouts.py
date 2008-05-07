def l1tlayout(i, p, *rows): i["L1T/Layouts/" + p] = DQMItem(layout=rows)

def l1t_gt_single(i, dir, name):
  i["L1T/Layouts/GT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_gmt_single(i, dir, name):
  i["L1T/Layouts/GMT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_gct_single(i, dir, name):
  i["L1T/Layouts/GCT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_rct_single(i, dir, name):
  i["L1T/Layouts/RCT-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_rpctf_single(i, dir, name):
  i["L1T/Layouts/RPCTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_dttf_single(i, dir, name):
  i["L1T/Layouts/DTTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

def l1t_csctf_single(i, dir, name):
  i["L1T/Layouts/CSCTF-Summary/%s" % name] = \
    DQMItem(layout=[["L1T/%s/%s" % (dir, name)]]) 

# list of summary GT histograms (dqmitems, dirPath , histoName)
l1t_gt_single(dqmitems, "L1TGT", "algo_bits")

# list of summary GMT histograms (dqmitems, dirPath , histoName)
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_phi")
l1t_gmt_single(dqmitems, "L1TGMT", "GMT_eta")
l1t_gmt_single(dqmitems, "L1TGMT", "Regional_trigger")

# list of summary GCT histograms (dqmitems, dirPath , histoName)
l1t_gct_single(dqmitems, "EventInfo/errorSummarySegments", "IsoEmRankEtaPhiSumm")
l1t_gct_single(dqmitems, "EventInfo/errorSummarySegments", "NonIsoEmRankEtaPhiSumm")

# list of summary RCT histograms (dqmitems, dirPath , histoName)
l1t_rct_single(dqmitems, "L1TRCT", "XYZ")

# list of summary CSCTF histograms (dqmitems, dirPath , histoName)
l1t_csctf_single(dqmitems, "L1TCSCTF", "CSCTF_errors")
l1t_csctf_single(dqmitems, "L1TCSCTF", "CSCTF_occupancies")

# list of summary RPC histograms (dqmitems, dirPath , histoName)
l1t_rpctf_single(dqmitems, "L1TRPCTF", "XYZ")

# list of summary DTTF histograms (dqmitems, dirPath , histoName)
l1t_dttf_single(dqmitems, "EventInfo/errorSummarySegments", "DT_TPG_phi_map")


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

