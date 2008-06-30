def hltlayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)
  
hltlayout(dqmitems,"00 Filtered ET Muon",
  	[{'path': "HLT/HLTMonhltMonMu/hltZMML2Filteredet", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"01 Filtered Eta Muon",
  	[{'path': "HLT/HLTMonhltMonMu/hltZMML2Filteredeta", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"02 Total Efficiency Muon",
  	[{'path': "HLT/HLTMonhltMonMu/total eff", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"03 Occupancy Muon",
  	[{'path': "HLT/HLTMonhltMonMu/hltZMML2Filteredeta_phi", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])


hltlayout(dqmitems,"00 Filtered ET Electron",
  	[{'path': "HLT/HLTMonhltMonE/hltL1seedRelaxedSingleEt8et", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"01 Filtered Eta Electron",
  	[{'path': "HLT/HLTMonhltMonE/hltL1seedRelaxedSingleEt8eta", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"02 Total Efficiency Electron",
  	[{'path': "HLT/HLTMonhltMonE/total eff", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"03 Occupancy Electron",
  	[{'path': "HLT/HLTMonhltMonE/hltL1seedRelaxedSingleEt8eta_phi", 'description': "Information missing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])
