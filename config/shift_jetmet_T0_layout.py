def shiftjetmetlayout(i, p, *rows): i["00 Shift/JetMET/" + p] = DQMItem(layout=rows)

shiftjetmetlayout(dqmitems, "00 Jet Pt", [{ 'path': "JetMET/SISConeJets/Pt2", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "01 Jet Eta", [{ 'path': "JetMET/SISConeJets/Eta", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "02 Jet Phi", [{ 'path': "JetMET/SISConeJets/Phi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "03 Jet Constituents", [{ 'path': "JetMET/SISConeJets/Constituents", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "04 MET", [{ 'path': "JetMET/CaloMETAnalyzer/METTask_CaloMET", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "05 MET Phi", [{ 'path': "JetMET/CaloMETAnalyzer/METTask_CaloMETPhi", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "06 MET Significance  ", [{ 'path': "JetMET/CaloMETAnalyzer/METTask_CaloMETSig", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "07 MET x", [{ 'path': "JetMET/CaloMETAnalyzer/METTask_CaloMEx", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])

shiftjetmetlayout(dqmitems, "08 MET y", [{ 'path': "JetMET/CaloMETAnalyzer/METTask_CaloMEy", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>Description</a>" }])
