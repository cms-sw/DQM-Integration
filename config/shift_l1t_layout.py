def l1tlayout(i, p, *rows): i["00 Shift/L1T/" + p] = DQMItem(layout=rows)
  
l1tlayout(dqmitems,"00 Global Trigger",
  	[{'path': "L1T/L1TGT/algo_bits", 'description': "Global Trigger bits. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}],
	[{'path': "L1T/L1TGT/event_lumi", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TGT/evnum_trignum_lumi", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1tlayout(dqmitems,"01 Global Muon Trigger",
  	[{'path': "L1T/L1TGMT/Regional_trigger", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TGMT/GMT_candlumi", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}],
	[{'path': "L1T/L1TGMT/GMT_phi", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TGMT/GMT_etaphi", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1tlayout(dqmitems,"02 Global Calorimeter Trigger",
  	[{'path': "L1T/L1TGCT/IsoEmOccEtaPhi", 'description': "(Eta,Phi) map of Isolated Electrons rank (~Et). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}],
	[{'path': "L1T/L1TGCT/NonIsoEmOccEtaPhi", 'description': "(Eta,Phi) map of Non Isolated Electrons rank (~Et). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1tlayout(dqmitems,"03 Regional Calorimeter Trigger",
  	[{'path': "L1T/L1TRCT/RctIsoEmOccEtaPhi", 'description': "Isolated Electron Candidates occupancy plot. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TRCT/RctNonIsoEmOccEtaPhi", 'description': "Non Isolated Electron Candidates occupancy plot. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}],
	[{'path': "L1T/L1TRCT/RctRegionsLocalOccEtaPhi", 'description': "Regional Candidates local occupancy plot. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TRCT/RctRegionsOccEtaPhi", 'description': "Regional Candidates occupancy plot. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1tlayout(dqmitems,"04 CSC Track Finder",
  	[{'path': "L1T/L1TCSCTF/CSCTF_occupancies", 'description': "CSCTF occupancy. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1tlayout(dqmitems,"05 DT Track Finder",
  	[{'path': "L1T/L1TDTTF/DTTF_TRACKS/INTEG/dttf_p_phi_eta", 'description': "DTTF phi input map. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1tlayout(dqmitems,"06 RPC",
  	[{'path': "L1T/L1TRPCTF/RPCTF_muons_tower_phipacked", 'description': "Occupancy. Tower is proportional to eta (standard trigger scale). Phi uses trigger phi scale (0...143). HotChannels and DeadChannels quality test are performed on this histo. Should be ~flat in each tower. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TRPCTF/RPCTF_ntrack", 'description': "Number of muon candidates found per event. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}],
	[{'path': "L1T/L1TRPCTF/RPCTF_pt_value", 'description': "pt value of muon candidates. During CRUZET it should be equal to 140 (due to patterns used). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TRPCTF/RPCDigi_bx", 'description': "Tells if delays are properly set on our FEDs (bin 0 of the histogram should be way above other bins). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])
