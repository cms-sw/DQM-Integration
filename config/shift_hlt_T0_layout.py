

###---- GENERIC - FourVector selection goes here: ####
######################################################

###---- GENERIC - FourVector Muon
def trigvalFVMuon(i, p, *rows): i["00 Shift/HLT/FourVector/Muon/" + p] = DQMItem(layout=rows)
  

trigvalFVMuon(dqmitems,"Muon Eff HLT to L1",
[{'path': "HLT/FourVector/client/HLT_Mu9/custom-eff/HLT_Mu9_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Mu9"}])

trigvalFVMuon(dqmitems,"Muon Eff HLT to RECO",
[{'path': "HLT/FourVector/client/HLT_Mu9/custom-eff/HLT_Mu9_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Mu9"}])

trigvalFVMuon(dqmitems,"HLT_Mu9: Et of L1 Muon Objects",
[{'path': "HLT/FourVector/source/HLT_Mu9/HLT_Mu9_wrt__l1EtL1", 'description':"Et of L1 Muon object for path HLT_Mu9"}])

trigvalFVMuon(dqmitems,"HLT_Mu9: Et of HLT Muon Objects",
[{'path': "HLT/FourVector/source/HLT_Mu9/HLT_Mu9_wrt__onEtOn", 'description':"Et of HLT Muon object for path HLT_Mu9"}])

trigvalFVMuon(dqmitems,"HLT_Mu9: Et of RECO Muon Objects",
[{'path': "HLT/FourVector/source/HLT_Mu9/HLT_Mu9_wrt__offEtOff", 'description':"Et of RECO Muon object for path HLT_Mu9"}])



###---- GENERIC - FourVector Electron
def trigvalFVEle(i, p, *rows): i["00 Shift/HLT/FourVector/Electron/" + p] = DQMItem(layout=rows)
  

trigvalFVEle(dqmitems,"Electron Eff HLT to L1",
[{'path': "HLT/FourVector/client/HLT_Ele10_LW_L1R/custom-eff/HLT_Ele10_LW_L1R_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Ele10_LW_L1R"}])

trigvalFVEle(dqmitems,"Electron Eff HLT to RECO",
[{'path': "HLT/FourVector/client/HLT_Ele10_LW_L1R/custom-eff/HLT_Ele10_LW_L1R_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Ele10_LW_L1R"}])

trigvalFVEle(dqmitems,"HLT_Ele10_LW_L1R: Et of L1 Electron Objects",
     [{'path': "HLT/FourVector/source/HLT_Ele10_LW_L1R/HLT_Ele10_LW_L1R_wrt__l1EtL1", 'description':"Et of L1 Electron object for path HLT_Ele10_LW_L1R"}])

trigvalFVEle(dqmitems,"HLT_Ele10_LW_L1R: Et of HLT Electron Objects",
[{'path': "HLT/FourVector/source/HLT_Ele10_LW_L1R/HLT_Ele10_LW_L1R_wrt__onEtOn", 'description':"Et of HLT Electron object for path HLT_Ele10_LW_L1R"}])

trigvalFVEle(dqmitems,"HLT_Ele10_LW_L1R: Et of RECO Electron Objects",
[{'path': "HLT/FourVector/source/HLT_Ele10_LW_L1R/HLT_Ele10_LW_L1R_wrt__offEtOff", 'description':"Et of RECO Electron object for path HLT_Ele10_LW_L1R"}])

             

###---- GENERIC - FourVector Jet
def trigvalFVJet(i, p, *rows): i["00 Shift/HLT/FourVector/Jet/" + p] = DQMItem(layout=rows)
  

trigvalFVJet(dqmitems,"Jet Eff HLT to L1",
[{'path': "HLT/FourVector/client/HLT_Jet30U/custom-eff/HLT_Jet30U_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Jet30U"}])

trigvalFVJet(dqmitems,"Jet Eff HLT to RECO",
[{'path': "HLT/FourVector/client/HLT_Jet30U/custom-eff/HLT_Jet30U_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Jet30U"}])

trigvalFVJet(dqmitems,"HLT_Jet30U: Et of L1 Jet Objects",
[{'path': "HLT/FourVector/source/HLT_Jet30U/HLT_Jet30U_wrt__l1EtL1", 'description':"Et of L1 Jet object for path HLT_Jet30U"}])
             
trigvalFVJet(dqmitems,"HLT_Jet30U: Et of HLT Jet Objects",
[{'path': "HLT/FourVector/source/HLT_Jet30U/HLT_Jet30U_wrt__onEtOn", 'description':"Et of HLT Jet object for path HLT_Jet30U"}])

trigvalFVJet(dqmitems,"HLT_Jet30U: Et of RECO Jet Objects",
[{'path': "HLT/FourVector/source/HLT_Jet30U/HLT_Jet30U_wrt__offEtOff", 'description':"Et of RECO Jet object for path HLT_Jet30U"}])

###---- GENERIC - FourVector Photon
def trigvalFVPho(i, p, *rows): i["00 Shift/HLT/FourVector/Photon/" + p] = DQMItem(layout=rows)
  

trigvalFVPho(dqmitems,"Photon Eff HLT to L1",
[{'path': "HLT/FourVector/client/HLT_Photon15_L1R/custom-eff/HLT_Photon15_L1R_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Photon15_L1R"}])

trigvalFVPho(dqmitems,"Photon Eff HLT to RECO",
[{'path': "HLT/FourVector/client/HLT_Photon15_L1R/custom-eff/HLT_Photon15_L1R_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Photon15_L1R"}])

trigvalFVPho(dqmitems,"HLT_Photon15_L1R: Et of L1 Photon Objects",
[{'path': "HLT/FourVector/source/HLT_Photon15_L1R/HLT_Photon15_L1R_wrt__l1EtL1", 'description':"Et of L1 Photon object for path HLT_Photon15_L1R"}])

trigvalFVPho(dqmitems,"HLT_Photon15_L1R: Et of HLT Photon Objects",
[{'path': "HLT/FourVector/source/HLT_Photon15_L1R/HLT_Photon15_L1R_wrt__onEtOn", 'description':"Et of HLT Photon object for path HLT_Photon15_L1R"}])

trigvalFVPho(dqmitems,"HLT_Photon15_L1R: Et of RECO Photon objects",
[{'path': "HLT/FourVector/source/HLT_Photon15_L1R/HLT_Photon15_L1R_wrt__offEtOff", 'description':"Et of RECO Photon object for path HLT_Photon15_L1R"}])


def hltlayout(i, p, *rows): i["00 Shift/HLT/Cosmics/" + p] = DQMItem(layout=rows)
  
hltlayout(dqmitems,"N of HLT_L1MuOpen_NoBPTX muons" ,
  	[{'path': "HLT/FourVector/source/HLT_L1MuOpen_NoBPTX/HLT_L1MuOpen_NoBPTX_wrt__NOn", 'description': "Multiplicity of HLT muons passing HLT_L1Mu path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"RECO muons Et",
  	[{'path': "HLT/FourVector/source/HLT_L1MuOpen_NoBPTX/HLT_L1MuOpen_NoBPTX_wrt__offEtOnOff", 'description': "Et of the RECO muons matched (eta-phi) with the triggering HLT_L1MuOpen_NoBPTX muons.   For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"RECO muons eta-phi",
  	[{'path': "HLT/FourVector/source/HLT_L1MuOpen_NoBPTX/HLT_L1MuOpen_NoBPTX_wrt__offEtaoffPhiOff", 'description': "X=eta and Y=phi for RECO muons that are matched (eta-phi) with HLT muons triggering this path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"HLT_L1MuOpen_NoBPTX & L1 muons eta-phi",
  	[{'path': "HLT/FourVector/source/HLT_L1MuOpen_NoBPTX/HLT_L1MuOpen_NoBPTX_wrt__l1Etal1PhiL1On", 'description': "X=eta and Y=phi for L1 muons that are matched (eta-phi) with HLT muons triggering this path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"Eff HLT_L1MuOpen_NoBPTX to its L1 vs Pt",
  	[{'path': "HLT/FourVector/client/HLT_L1MuOpen_NoBPTX/custom-eff/HLT_L1MuOpen_NoBPTX_wrt__l1Et_Eff_OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of Et.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"Eff HLT_L1MuOpen_NoBPTX to its L1 vs eta-phi",
  	[{'path': "HLT/FourVector/client/HLT_L1MuOpen_NoBPTX/custom-eff/HLT_L1MuOpen_NoBPTX_wrt__l1Etal1Phi_Eff_OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of eta-phi.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"Eff HLT_L2Mu9 to its L1 vs Pt",
  	[{'path': "HLT/FourVector/client/HLT_L2Mu9/custom-eff/HLT_L2Mu9_wrt__l1Et_Eff_OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of Et.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])
  
hltlayout(dqmitems,"Eff HLT_L2Mu9 to its L1 vs eta-phi",
  	[{'path': "HLT/FourVector/client/HLT_L2Mu9/custom-eff/HLT_L2Mu9_wrt__l1Etal1Phi_Eff_OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of eta-phi.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"Jet Eff HLT to L1",
[{'path': "HLT/FourVector/client/HLT_Jet30U/custom-eff/HLT_Jet30U_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Jet30U"}])

hltlayout(dqmitems,"Jet Eff HLT to RECO",
[{'path': "HLT/FourVector/client/HLT_Jet30U/custom-eff/HLT_Jet30U_wrt__l1Etal1Phi_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Jet30U"}])

