

###---- GENERIC - FourVector selection goes here: ####
######################################################

###---- GENERIC - FourVector Muon
def trigHltMuonOfflineSummary(i, p, *rows): 
   i["HLT/Muon/MuonHLTSummary/" + p] = DQMItem(layout=rows)


######################################################

trigHltMuonOfflineSummary(dqmitems,"01 - HLT_Mu3_v4",
   [{'path': "HLT/Muon/Distributions/HLT_Mu3_v4/allMuons/recEffPt_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_Mu3_v4/allMuons/recEffPhiVsEta_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"02 - HLT_Mu5_v4",
   [{'path': "HLT/Muon/Distributions/HLT_Mu5_v4/allMuons/recEffPt_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_Mu5_v4/allMuons/recEffPhiVsEta_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"03 - HLT_Mu12_v2",
   [{'path': "HLT/Muon/Distributions/HLT_Mu12_v2/allMuons/recEffPt_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_Mu12_v2/allMuons/recEffPhiVsEta_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"04 - HLT_Mu30_v2",
   [{'path': "HLT/Muon/Distributions/HLT_Mu30_v2/allMuons/recEffPt_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_Mu30_v2/allMuons/recEffPhiVsEta_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"05 - HLT_L2Mu10_v2",
   [{'path': "HLT/Muon/Distributions/HLT_L2Mu10_v2/allMuons/recEffPt_L2Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_L2Mu10_v2/allMuons/recEffPhiVsEta_L2Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"06 - HLT_L2Mu20_v2",
   [{'path': "HLT/Muon/Distributions/HLT_L2Mu20_v2/allMuons/recEffPt_L2Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_L2Mu20_v2/allMuons/recEffPhiVsEta_L2Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

