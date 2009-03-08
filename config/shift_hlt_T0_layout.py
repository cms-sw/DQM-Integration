def hltlayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)
  
hltlayout(dqmitems,"00-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflinehltResults/HLT_L1Mu_NOn", 'description': "Multiplicity of HLT muons passing HLT_L1Mu path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"01-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflinehltResults/HLT_L1Mu_etOn", 'description': "Et of the HLT muons. (never mind that the histogram title reads offline.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"02-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflinehltResults/HLT_L1Mu_etOff", 'description': "Et of the RECO muons matched (eta-phi) with the triggering HLT muons.   For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"04-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflinehltResults/HLT_L1Mu_etaphiOn", 'description': "X=eta and Y=phi for HLT muons triggering this path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"05-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflinehltResults/HLT_L1Mu_etaphiOff", 'description': "X=eta and Y=phi for RECO muons that are matched (eta-phi) with HLT muons triggering this path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"06-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflinehltResults/HLT_L1Mu_etaphiL1", 'description': "X=eta and Y=phi for L1 muons that are matched (eta-phi) with HLT muons triggering this path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"07-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflineClient/paths/HLT_L1Mu/efficiencies/HLT_L1Mu_eta_Eff-OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of eta.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"08-HLT Shift Histogram",
  	[{'path': "HLTOffline/FourVectorHLTOfflineClient/paths/HLT_L1Mu/efficiencies/HLT_L1Mu_phi_Eff-OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of phi.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
