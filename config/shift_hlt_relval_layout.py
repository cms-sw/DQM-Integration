###
# """
# file: DQM/Integration/config/shift_hlt_relval_layout.py
# 
# This layout file contains hlt me selection for release validation
# -each subsystem specifies below O(10) most important validation histograms 
# -histogram folder is specified as 
#  def hltval<subsys>(i, p, *rows): i["00 Shift/TRIGGER Validation/HLT <subsys>" + p] = DQMItem(layout=rows)
# -selected histograms are specified as
#  hltval<subsys>(dqmitems,"doubleEle5SWL1R",
#  [{'path': "path to histogram as HLT/<subsys>/<my folder>/<my histo>",
#   'description':"summary histogram description"}])
# """
###




###---- EGAMMA selection goes here: ----

def trigvalegammaZ(i, p, *rows): i["00 Shift/HLT/Egamma/Zee Preselection/" + p] = DQMItem(layout=rows)
  
trigvalegammaZ(dqmitems,"doubleEle5SWL1R",
[{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"}])

trigvalegammaZ(dqmitems,"doubleElectron",
[{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleElectron"}])

trigvalegammaZ(dqmitems,"doubleElectronRelaxed",
[{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleElectron"}])

trigvalegammaZ(dqmitems,"singleElectron",
[{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singelElectron"}])

trigvalegammaZ(dqmitems,"singleElectronRelaxed",
[{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singelElectronRelaxed"}])

trigvalegammaZ(dqmitems,"ele15SWL1R",
[{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for ele15SWL1R"}])

trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R",
[{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"}])

def trigvalegammaW(i, p, *rows): i["00 Shift/HLT/Egamma/Wenu Preselection/" + p] = DQMItem(layout=rows)

trigvalegammaW(dqmitems,"singleElectron",
[{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singelElectron"}])

trigvalegammaW(dqmitems,"singleElectronRelaxed",
[{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singelElectronRelaxed"}])

trigvalegammaW(dqmitems,"ele15SWL1R",
[{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for ele15SWL1R"}])

trigvalegammaW(dqmitems,"looseIsoEle15LWL1R",
[{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"}])



###---- MUON selection goes here: ----

def trigvalmuon(i, p, *rows): i["00 Shift/HLT/Muon/" + p] = DQMItem(layout=rows)
trigvalmuon(dqmitems,"Efficiency L1 vs Gen",
  	[{'path': "HLT/Muon/Distributions/HLT_IsoMu9/genEffEta_L1Filtered", 'description': "L1 trigger efficiency for IsoMu9 versus eta. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLTOfflinePerformance\">here</a>."}])



###---- TAU selection goes here: ----

def trigvaltau(i, p, *rows): i["00 Shift/HLT/Tau/" + p] = DQMItem(layout=rows)
trigvaltau(dqmitems,"Single Tau",
  	[{'path': "HLT/HLTTAU/SingleTau/Triggers", 'description': "Accepted events per single tau path. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TauTriggerValidation\">here</a>."}])



###---- JETMET selection goes here: ----
def trigvaljetmet(i, p, *rows): i["00 Shift/HLT/JetMET/" + p] = DQMItem(layout=rows)

###---- BJET selection goes here: ----
def trigvalbjet(i, p, *rows): i["00 Shift/HLT/BJet/" + p] = DQMItem(layout=rows)

###---- ALCA selection goes here: ----

def trigvalalca(i, p, *rows): i["00 Shift/HLT/AlCa/" + p] = DQMItem(layout=rows)
trigvalalca(dqmitems,"Pi0 inv mass",
           [{'path': "HLT/AlCaEcalPi0/Pi0InvmassEB", 'description': "Pi0 Invariant mass EB . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideSpecialHLTOfflinePerformance\">here</a>."}])
trigvalalca(dqmitems,"event energy eb",
            [{'path': "HLT/EcalPhiSym/eventEnergyEB", 'description': "Event energy EB . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideSpecialHLTOfflinePerformance\">here</a>."}])



###---- HEAVYFLAVOR selection goes here: ----
def trigvalbphys(i, p, *rows): i["00 Shift/HLT/HeavyFlavor/" + p] = DQMItem(layout=rows)
trigvalbphys(dqmitems,"Quakonium efficiency",
             [{'path': "HLT/HeavyFlavor/QuarkoniumEfficiencies/genQuakonium_genPt", 'description': ". For more information please click <a href=\"\">here</a>."}])



###---- TOP selection goes here: ----
def trigvaltop(i, p, *rows): i["00 Shift/HLT/Top/" + p] = DQMItem(layout=rows)
trigvaltop(dqmitems,"Efficiency IsoEle18 vs Eta",
  	[{'path': "HLT/Top/EffEta_IsoEle18", 'description': "Trigger efficiency for IsoEle18 versus eta. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideTopHLTOfflinePerformance\">here</a>."}])



###---- SUSYEXO selection goes here: ----
def trigvalsusybsm(i, p, *rows): i["00 Shift/HLT/SusyExo/" + p] = DQMItem(layout=rows)
trigvalsusybsm(dqmitems,"HltBits",
               [{'path': "HLT/SusyExo/TriggerBits/HltBits", 'description': "HLT trigger bits. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideSUSYBSMHLTOfflinePerformance\">here</a>."}])



###---- HIGGS selection goes here: ----
def trigvalhiggs(i, p, *rows): i["00 Shift/HLT/Higgs/" + p] = DQMItem(layout=rows)
#trigvalhiggs(dqmitems,"", [{'path': "HLT/", 'description': ". For more information please click <a href=\"\">here</a>."}])


###---- QCD selection goes here: ----
def trigvalqcd(i, p, *rows): i["00 Shift/HLT/QCD/" + p] = DQMItem(layout=rows)
#trigvalqcd(dqmitems,"", [{'path': "HLT/", 'description': ". For more information please click <a href=\"\">here</a>."}])




#trigvallayout(dqmitems,"HLT Histograms",
#  	[{'path': "HLT/", 'description': "Trigger efficiency . For more information please click <a href=\"https:\">here</a>."}])






