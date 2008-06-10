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
  	[{'path': "L1T/L1TDTTF/DTTF_PHI/BxEncoding_PHI_OUT", 'description': "DTTF phi input map. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

l1tlayout(dqmitems,"06 RPC",
  	[{'path': "L1T/L1TRPCTF/Client/RPCTF_phi_valuepacked_bad", 'description': "Channels in phi having to small/big occupancy. Useful only for runs with muons coming mostly from IP. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TRPCTF/Client/RPCTF_phi_valuepacked_dead", 'description': "Dead channels in phi. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}],
	[{'path': "L1T/L1TRPCTF/Client/RPCTF_deadchannels", 'description': "Dead channels in (phi,tower). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."},
	{'path': "L1T/L1TRPCTF/Client/RPCTF_noisychannels", 'description': "Noisy channels in (phi,tower). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])
