def shiftjetmetlayout(i, p, *rows): i["00 Shift/JetMET/" + p] = DQMItem(layout=rows)

shiftjetmetlayout(dqmitems, "00 Jet Pt", [{ 'path': "JetMET/Jet/AntiKtJets/Pt2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "01 Jet Eta", [{ 'path': "JetMET/Jet/AntiKtJets/Eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "02 Jet Phi", [{ 'path': "JetMET/Jet/AntiKtJets/Phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "03 Jet Constituents", [{ 'path': "JetMET/Jet/AntiKtJets/Constituents", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "04 MET", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMET", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "05 MET Phi", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMETPhi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "06 MET Significance  ", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMETSig", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "07 MET x", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMEx", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "08 MET y", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMEy", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])
