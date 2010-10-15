def hltlayout(i, p, *rows): i["00 Shift/HLT/Cosmics" + p] = DQMItem(layout=rows)
  

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



def hltlayout(i, p, *rows): i["00 Shift/HLT/Collisions" + p] = DQMItem(layout=rows)
  

hltlayout(dqmitems,"01 HLT_BTau_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_BTau_Pass_Any", 'description': "Shows total number of HLT Egamma trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"02 HLT_Commissioning_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_Commissioning_Pass_Any", 'description': "Shows total number of HLT Commissioning trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"03 HLT_Cosmics_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_Cosmics_Pass_Any", 'description': "Shows total number of HLT Cosmics trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"04 HLT_EGMonitor_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_EGMonitor_Pass_Any", 'description': "Shows total number of HLT EGMonitor trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"05 HLT_Electron_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_Electron_Pass_Any", 'description': "Shows total number of HLT Electron trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"06 HLT_HcalHPDNoise_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_HcalHPDNoise_Pass_Any", 'description': "Shows total number of HLT HcalHPDNoise trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"07 HLT_HcalHZS_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_HcalHZS_Pass_Any", 'description': "Shows total number of HLT HcalHZS trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"08 HLT_Jet_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_Jet_Pass_Any", 'description': "Shows total number of HLT Jet trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"09 HLT_JetMETTauMonitor_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_JetMETTauMonitor_Pass_Any", 'description': "Shows total number of HLT JetMETTauMonitor trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"10 HLT_METFwd_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_METFwd_Pass_Any", 'description': "Shows total number of HLT METFwd trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"11 HLT_MinimumBias_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_MinimumBias_Pass_Any", 'description': "Shows total number of HLT MinimumBias trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"12 HLT_Mu_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_Mu_Pass_Any", 'description': "Shows total number of HLT Mu trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"13 HLT_MuMonitor_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_MuMonitor_Pass_Any", 'description': "Shows total number of HLT MuMonitor trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"14 HLT_MuOnia_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_MuOnia_Pass_Any", 'description': "Shows total number of HLT MuOnia trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"15 HLT_MultiJet_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_MultiJet_Pass_Any", 'description': "Shows total number of HLT MultiJet trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"16 HLT_Photon_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_Photon_Pass_Any", 'description': "Shows total number of HLT Photon trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])


hltlayout(dqmitems,"01 HLT_Cosmics_Pass_Any", [{'path': "HLT/FourVector/PathsSummary/HLT_Cosmics_Pass_Any", 'description': "Shows total number of HLT Cosmics trigger accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])
