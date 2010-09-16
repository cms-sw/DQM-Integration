def hltlayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)
  

hltlayout(dqmitems,"01 HLT_Egamma_Pass_Any",
  	[{'path': "HLT/FourVector/PathsSummary/HLT_Egamma_Pass_Any", 'description': "Shows total number of HLT Egamma trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"02 HLT_JetMet_Pass_Any",
  	[{'path': "HLT/FourVector/PathsSummary/HLT_JetMet_Pass_Any", 'description': "Shows total number of HLT JetMET trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"03 HLT_Muon_Pass_Any",
  	[{'path': "HLT/FourVector/PathsSummary/HLT_Muon_Pass_Any", 'description': "Shows total number of HLT Muon trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"04 HLT_Rest_Pass_Any",
  	[{'path': "HLT/FourVector/PathsSummary/HLT_Rest_Pass_Any", 'description': "Shows total number of HLT Rest trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"05 HLT_Special_Pass_Any",
  	[{'path': "HLT/FourVector/PathsSummary/HLT_Special_Pass_Any", 'description': "Shows total number of HLT Special trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

