def l1tlayout(i, p, *rows): i["L1T/Layouts/" + p] = DQMItem(layout=rows)


l1tlayout(dqmitems, "GT Information",
  ["L1T/L1TGT/algo_bits"])

l1tlayout(dqmitems, "GMT Information",
  ["L1T/L1TGMT/GMT_eta",
  "L1T/L1TGMT/GMT_phi",
  "L1T/L1TGMT/Regional_trigger"])

l1tlayout(dqmitems, "GCT Information",
          ["L1T/EventInfo/errorSummarySegments/IsoEmRankEtaPhiSumm",
	  "L1T/EventInfo/errorSummarySegments/NonIsoEmRankEtaPhiSumm"])

l1tlayout(dqmitems, "CSCTF Information",
  ["L1T/L1TGT/CSCTF_errors",
   "L1T/L1TCSCTF/CSCTF_occupancies"])

l1tlayout(dqmitems, "DTTF Information",
  ["L1T/EventInfo/errorSummarySegments/DT_TPG_phi_map"])

