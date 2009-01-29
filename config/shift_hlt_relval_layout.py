def hltvallayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)

hltvallayout(dqmitems,"00-HLT EGamma Histograms",
  	[{'path': "HLT/HLTEgammaValidation/singleElectronDQMWnu/total_eff", 'description': "Trigger efficiency. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideEgammaHLTOfflinePerformance\">here</a>."}])

hltvallayout(dqmitems,"00-HLT Muon Histograms",
  	[{'path': "HLT/Muon/Distributions/HLT_IsoMu9/GenEffEta_L1Filtered", 'description': "L1 trigger efficiency for IsoMu9 versus eta. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLTOfflinePerformance\">here</a>."}])

hltvallayout(dqmitems,"00-HLT Tau Histograms",
  	[{'path': "HLT/HLTTAU/SingleTau/Triggers", 'description': "Accepted events per single tau path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TauTriggerValidation\">here</a>."}])

hltvallayout(dqmitems,"00-HLT AlCa Histograms",
             [{'path': "HLT/AlCaEcalPi0/Pi0InvmassEB", 'description': "Pi0 Invariant mass EB . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideSpecialHLTOfflinePerformance\">here</a>."},
         {'path': "HLT/EcalPhiSym/eventEnergyEB", 'description': "Event energy EB . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideSpecialHLTOfflinePerformance\">here</a>."}])

hltvallayout(dqmitems,"00-HLT Top Histograms",
  	[{'path': "HLT/Top/EffEta_IsoEle18", 'description': "Trigger efficiency for IsoEle18 versus eta. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideTopHLTOfflinePerformance\">here</a>."}])


#hltvallayout(dqmitems,"00-HLT Histograms",
#  	[{'path': "HLT/", 'description': "Trigger efficiency . For more information please click <a href=\"https:\">here</a>."}])






