def shiftjetmetlayout(i, p, *rows): i["00 Shift/JetMET/" + p] = DQMItem(layout=rows)

shiftjetmetlayout(dqmitems, "00 Jet Pt (for collisions)", [{ 'path': "JetMET/Jet/CleanedAntiKtJets/Pt2", 'description': "Distribution of Jet Pt for all cleaned jets (event primary vertex requirement, technical trigger requirements (bit 0 && (40||41) && !(36||37||38||39) ), and HLT physics declared, the distribution should be fast falling with no spikes) (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "00 Jet Pt (for cosmics)", [{ 'path': "JetMET/Jet/AntiKtJets/Pt2", 'description': "Distribution of Jet Pt with no cleaning requirements for cosmic runs, the distribution should be fast falling with no spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>more</a>)" }])

shiftjetmetlayout(dqmitems, "01 Jet Eta (for collisions)", [{ 'path': "JetMET/Jet/CleanedAntiKtJets/Eta", 'description': "Eta distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "01 Jet Eta (for cosmics)", [{ 'path': "JetMET/Jet/AntiKtJets/Eta", 'description': "Eta distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET>more</a>)" }])

shiftjetmetlayout(dqmitems, "02 Jet Phi (for collisions)", [{ 'path': "JetMET/Jet/CleanedAntiKtJets/Phi", 'description': "Phi distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "02 Jet Phi (for cosmics)", [{ 'path': "JetMET/Jet/AntiKtJets/Phi", 'description': "Phi distribution for all jets.  Should be smooth and without spikes (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "03 Jet Constituents (for collisions)", [{ 'path': "JetMET/Jet/CleanedAntiKtJets/Constituents", 'description': "Number of constituents towers in the jet.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "03 Jet Constituents (for cosmics)", [{ 'path': "JetMET/Jet/AntiKtJets/Constituents", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#jet_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "04 MET (for collisions)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/METTask_CaloMET", 'description': "The Calorimeter Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "04 MET (for cosmics)", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMET", 'description': "The Calorimeter Missing ET distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "05 MET Phi (for collisions)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/METTask_CaloMETPhi", 'description': "The Calorimeter Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "05 MET Phi (for cosmics)", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMETPhi", 'description': "The Calorimeter Missing ET phi distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "06 MET x (for collisions)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/METTask_CaloMEx", 'description': "The Calorimeter Missing Ex distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "06 MET x (for cosmics)", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMEx", 'description': "The Calorimeter Missing Ex distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "07 MET y (for collisions)", [{ 'path': "JetMET/MET/CaloMET/BasicCleanup/METTask_CaloMEy", 'description': "The Calorimeter Missing Ey distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "07 MET y (for cosmics)", [{ 'path': "JetMET/MET/CaloMET/All/METTask_CaloMEy", 'description': "The Calorimeter Missing Ey distribution.  There should not be any spikes in the distribution (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#met_summary_plots>more</a>)" }])

shiftjetmetlayout(dqmitems, "08 CaloTower occupancy", [{ 'path': "JetMET/CaloTowers/SchemeB/METTask_CT_Occ_ieta_iphi", 'description': "The occupancy of the Calo Towers, there should not be any large holes in the plot (<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineJetMET#calotower_plots>more</a>)" }])
