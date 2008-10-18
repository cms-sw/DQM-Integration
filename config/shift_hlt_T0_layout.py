def hltlayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)
  
hltlayout(dqmitems,"00-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflinehltResults/HLTJet30_NOn", 'description': "Trigger Rate per path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])

hltlayout(dqmitems,"01-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflinehltResults/HLT_L1Mu_NOn", 'description': "Trigger Rate rejection per filter (Y) and path (X). For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."}])
