def hltlayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)
  
hltlayout(dqmitems,"00 Counts per muon HLT path",
  	[{'path': "HLT/HLTMonMuon/Summary/PassingBits_Summary_Muon", 'description': "event count per muon path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"01 HLT Rate w.r.t. L1 Muon trigger path",
  	[{'path': "HLT/HLTMonMuon/Summary/HLTRate_Muon", 'description': "Muon path efficiency with respect to base muon trigger (see histogram). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"02 HLT Muon Occupancy",
  	[{'path': "HLT/HLTMonMuon/L1PassThrough/Level1/HLTMuonL1_etaphi", 'description': "Occupancy distribution for muon candidates passing any L1Muon path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"03 HLT Muon Eta",
  	[{'path': "HLT/HLTMonMuon/L1PassThrough/Level1/HLTMuonL1_eta", 'description': "Eta distribution for muon candidates passing any L1Muon path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"04 HLT Muon Phi",
  	[{'path': "HLT/HLTMonMuon/L1PassThrough/Level1/HLTMuonL1_phi", 'description': "Phi distribution for muon candidates passing any L1Muon path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"05 HLT Scalers",
  	[{'path': "HLT/HLTScalers_SM/hltScalers", 'description': "HLT scaler for all hlt trigger paths. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"06 Counts per JetMET HLT path",
  	[{'path': "HLT/JetMET/All/JetMET_rate_All", 'description': "Event triggered JetMET trigger paths . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"07 HLT Rate w.r.t. L1 EG trigger path",
  	[{'path': "HLT/HLTMonElectron/Summary/HLTRate_Electron", 'description': "EG path efficiency with respect to base EG trigger (see histogram). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"08 Counts per Tau HLT path",
  	[{'path': "HLT/TauOnline/Inclusive/SingleTau/TriggerBits", 'description': "Event triggered Tau trigger paths . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])
