###
# """
# file: DQM/Integration/config/hlt_relval-layouts.py
# 
# Layout file for trigger release validation
#  facilitating organization/regrouping of subsystem histograms
# -use subsystem top-folder as specified in previous stages eg
#  def trigval<subsys>(i, p, *rows): i["HLT/<subsys>/Preselection" + p] = DQMItem(layout=rows)
# """
###


###---- EGAMMA selection goes here: ----

def trigvalegammaZ(i, p, *rows): i["HLT/HLTEgammaValidation/Zee Preselection/" + p] = DQMItem(layout=rows)

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/total",
           [{'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_by_step_MC_matched", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_by_step", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/gen_et", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/gen_eta", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoDoubleElectronEt5L1MatchFilterRegional_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5L1MatchFilterRegional in doubleEle5SWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoDoubleElectronEt5L1MatchFilterRegional_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5L1MatchFilterRegional in doubleEle5SWL1R_vs_et"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoDoubleElectronEt5EtFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5EtFilter in doubleEle5SWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoDoubleElectronEt5EtFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5EtFilter in doubleEle5SWL1R_vs_et"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoDoubleElectronEt5HcalIsolFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonHLTnonIsoIsoDoubleElectronEt5HcalIsolFilter in doubleEle5SWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoDoubleElectronEt5HcalIsolFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonHLTnonIsoIsoDoubleElectronEt5HcalIsolFilter in doubleEle5SWL1R_vs_et"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoDoubleElectronEt5PixelMatchFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5PixelMatchFilter in doubleEle5SWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_DoubleEle5_SW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoDoubleElectronEt5PixelMatchFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5PixelMatchFilter in doubleEle5SWL1R_vs_et"}])



trigvalegammaZ(dqmitems,"Ele10LWL1R/total",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_by_step_MC_matched", 'description':"per-event efficiency (MC matched) for Ele10LWL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_by_step", 'description':"per-event efficiency (MC matched) for Ele10LWL1R"}])

trigvalegammaZ(dqmitems,"Ele10LWL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/gen_et", 'description':"per-event efficiency (MC matched) for Ele10LWL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/gen_eta", 'description':"per-event efficiency (MC matched) for Ele10LWL1R"}])

trigvalegammaZ(dqmitems,"Ele10LWL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10L1MatchFilterRegional_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10L1MatchFilterRegional in Ele10LWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10L1MatchFilterRegional_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10L1MatchFilterRegional in Ele10LWL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EtFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EtFilter in Ele10LWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EtFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EtFilter in Ele10LWL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10HcalIsolFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10HcalIsolFilter in Ele10LWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10HcalIsolFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10HcalIsolFilter in Ele10LWL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter in Ele10LWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter in Ele10LWL1R_vs_et"}])



trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/total",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_by_step_MC_matched", 'description':"per-event efficiency (MC matched) for Ele10LWEleIdL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_by_step", 'description':"per-event efficiency (MC matched) for Ele10LWEleIdL1R"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/gen_et", 'description':"per-event efficiency (MC matched) for Ele10LWEleIdL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/gen_eta", 'description':"per-event efficiency (MC matched) for Ele10LWEleIdL1R"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdL1MatchFilterRegional_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdL1MatchFilterRegional in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdL1MatchFilterRegional_vs_et_MC_matched" , 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdL1MatchFilterRegional in Ele10LWEleIdL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdEtFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdEtFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdEtFilter_vs_et_MC_matched",  'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdEtFilter in Ele10LWEleIdL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/cluster shape cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdClusterShapeFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdClusterShapeFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdClusterShapeFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdClusterShapeFilter in Ele10LWEleIdL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdHcalIsolFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdHcalIsolFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdHcalIsolFilter_vs_et_MC_matched",  'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdHcalIsolFilter in Ele10LWEleIdL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdPixelMatchFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdPixelMatchFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdPixelMatchFilter_vs_et_MC_matched",  'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdPixelMatchFilter in Ele10LWEleIdL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/ 1oE - 1op cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdOneOEMinusOneOPFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdOneOEMinusOneOPFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdOneOEMinusOneOPFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdOneOEMinusOneOPFilter in Ele10LWEleIdL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/ delta-eta cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDetaFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDetaFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDetaFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDetaFilter in Ele10LWEleIdL1R_vs_et"}])

trigvalegammaZ(dqmitems,"Ele10LWEleIdL1R/ delta-phi cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDphiFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDphiFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMZee/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDphiFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDphiFilter in Ele10LWEleIdL1R_vs_et"}])



                            

def hltlayoutW(i, p, *rows): i["HLT/HLTEgammaValidation/Wenu Preselection/" + p] = DQMItem(layout=rows)

hltlayoutW(dqmitems,"Ele10LWL1R/total",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_by_step_MC_matched", 'description':"per-event efficiency (MC matched) for Ele10LWL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_by_step", 'description':"per-event efficiency (MC matched) for Ele10LWL1R"}])

hltlayoutW(dqmitems,"Ele10LWL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/gen_et", 'description':"per-event efficiency (MC matched) for Ele10LWL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/gen_eta", 'description':"per-event efficiency (MC matched) for Ele10LWL1R"}])

hltlayoutW(dqmitems,"Ele10LWL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10L1MatchFilterRegional_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10L1MatchFilterRegional in Ele10LWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10L1MatchFilterRegional_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10L1MatchFilterRegional in Ele10LWL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EtFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EtFilter in Ele10LWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EtFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EtFilter in Ele10LWL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10HcalIsolFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10HcalIsolFilter in Ele10LWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10HcalIsolFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10HcalIsolFilter in Ele10LWL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter in Ele10LWL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter in Ele10LWL1R_vs_et"}])



hltlayoutW(dqmitems,"Ele10LWEleIdL1R/total",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_by_step_MC_matched", 'description':"per-event efficiency (MC matched) for Ele10LWEleIdL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_by_step", 'description':"per-event efficiency (MC matched) for Ele10LWEleIdL1R"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/gen_et", 'description':"per-event efficiency (MC matched) for Ele10LWEleIdL1R"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/gen_eta", 'description':"per-event efficiency (MC matched) for Ele10LWEleIdL1R"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdL1MatchFilterRegional_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdL1MatchFilterRegional in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdL1MatchFilterRegional_vs_et_MC_matched" , 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdL1MatchFilterRegional in Ele10LWEleIdL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdEtFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdEtFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdEtFilter_vs_et_MC_matched",  'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdEtFilter in Ele10LWEleIdL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/cluster shape cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdClusterShapeFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdClusterShapeFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdClusterShapeFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdClusterShapeFilter in Ele10LWEleIdL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdHcalIsolFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdHcalIsolFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdHcalIsolFilter_vs_et_MC_matched",  'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdHcalIsolFilter in Ele10LWEleIdL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdPixelMatchFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdPixelMatchFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdPixelMatchFilter_vs_et_MC_matched",  'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdPixelMatchFilter in Ele10LWEleIdL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/ 1oE - 1op cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdOneOEMinusOneOPFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdOneOEMinusOneOPFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdOneOEMinusOneOPFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdOneOEMinusOneOPFilter in Ele10LWEleIdL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/ delta-eta cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDetaFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDetaFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDetaFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDetaFilter in Ele10LWEleIdL1R_vs_et"}])

hltlayoutW(dqmitems,"Ele10LWEleIdL1R/ delta-phi cut",
           [{'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDphiFilter_vs_eta_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDphiFilter in Ele10LWEleIdL1R_vs_eta"},
            {'path': "HLT/HLTEgammaValidation/HLT_Ele10_LW_EleId_L1RDQMWenu/efficiency_hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDphiFilter_vs_et_MC_matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronLWEt10EleIdDphiFilter in Ele10LWEleIdL1R_vs_et"}])


def hltLayoutGammaJet(i, p, *rows): i["HLT/HLTEgammaValidation/Photon Summary" + p] = DQMItem(layout=rows)
hltLayoutGammaJet(dqmitems,"/HLT_Photon10_L1R Efficiency vs Et",
                  [{'path':"HLT/HLTEgammaValidation/HLT_Photon10_L1R_DQMGammaJet/final_eff_vs_et", 'description':"Efficiency of HLT_Photon10_L1R vs Et of generated photon"}])
hltLayoutGammaJet(dqmitems,"/HLT_Photon10_L1R Efficiency vs eta",
                  [{'path':"HLT/HLTEgammaValidation/HLT_Photon10_L1R_DQMGammaJet/final_eff_vs_eta", 'description':"Efficiency of HLT_Photon10_L1R vs eta of generated photon"}])
hltLayoutGammaJet(dqmitems,"/L1 EgammaEt5 Efficiency vs et",
                  [{'path':"HLT/HLTEgammaValidation/HLT_Photon10_L1R_DQMGammaJet/efficiency_hltL1sRelaxedSingleEgammaEt5_vs_et_MC_matched", 'description':"Efficiency of L1 EgammaEt5 vs et of generated photon"}])
hltLayoutGammaJet(dqmitems,"/L1 EgammaEt5 Efficiency vs eta",
                  [{'path':"HLT/HLTEgammaValidation/HLT_Photon10_L1R_DQMGammaJet/efficiency_hltL1sRelaxedSingleEgammaEt5_vs_eta_MC_matched", 'description':"Efficiency of L1 EgammaEt5 vs eta of generated photon"}])
hltLayoutGammaJet(dqmitems,"/HLT_Photon15_LooseEcalIso_L1R Efficiency vs Et",
                  [{'path':"HLT/HLTEgammaValidation/HLT_Photon15_LooseEcalIso_L1R_DQMGammaJet/final_eff_vs_et",'description':"Efficiency of HLT_Photon15_LooseEcalIso_L1R vs Et of generated photon"}])
hltLayoutGammaJet(dqmitems,"/HLT_Photon15_LooseEcalIso_L1R Efficiency vs eta",
                  [{'path':"HLT/HLTEgammaValidation/HLT_Photon15_LooseEcalIso_L1R_DQMGammaJet/final_eff_vs_eta",'description':"Efficiency of HLT_Photon15_LooseEcalIso_L1R vs eta of generated photon"}])
hltLayoutGammaJet(dqmitems,"/HLT_Photon15_TrackIso_L1R Efficiency vs Et",
                  [{'path':"HLT/HLTEgammaValidation/HLT_Photon15_TrackIso_L1R_DQMGammaJet/final_eff_vs_et",'description':"Efficiency of HLT_Photon15_TrackIso_L1R vs Et of generated photon"}])
hltLayoutGammaJet(dqmitems,"/HLT_Photon15_TrackIso_L1R Efficiency vs eta",
                  [{'path':"HLT/HLTEgammaValidation/HLT_Photon15_TrackIso_L1R_DQMGammaJet/final_eff_vs_eta",'description':"Efficiency of HLT_Photon15_TrackIso_L1R vs eta of generated photon"}])


###---- MUON selection goes here: ----

def trigvalmuon(i, p, *rows): i["HLT/Muon/Efficiency Summary for " + p] = DQMItem(layout=rows)

menus = ["8E29"      , "1E31"      ]
paths = ["HLT_IsoMu3", "HLT_IsoMu9"]

for menuNum in range(len(menus)):

    thisMenu          = menus[menuNum]
    thisDir           = "HLT/Muon/Distributions/" + paths[menuNum]
    thisDocumentation = " (" + paths[menuNum] + " path) (<a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLTOfflinePerformance\">documentation</a>)"

    trigvalmuon(dqmitems, thisMenu + "/pT Turn-On for L1",
        [{'path': thisDir + "/genTurnOn_L1", 'description':"Efficiency to find an L1 muon associated to a generated muon vs. pT" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/pT Turn-On for L2",
        [{'path': thisDir + "/genTurnOn_L2", 'description':"Efficiency to find a gen-matched L2 muon associated to a gen-matched L1 muon vs. pT" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/pT Turn-On for L2 Isolation",
        [{'path': thisDir + "/genTurnOn_L2Iso", 'description':"Efficiency to find an isolated gen-matched L2 muon associated to a gen-matched L1 muon vs. pT" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/pT Turn-On for L3",
        [{'path': thisDir + "/genTurnOn_L3", 'description':"Efficiency to find a gen-matched L3 muon associated to a gen-matched L1 muon vs. pT" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/pT Turn-On for L3 Isolation",
        [{'path': thisDir + "/genTurnOn_L3Iso", 'description':"Efficiency to find an isolated gen-matched L3 muon associated to a gen-matched L1 muon vs. pT" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/Efficiency of L1",
        [{'path': thisDir + "/genEffEta_L1", 'description':"Efficiency to find an L1 muon associated to a generated muon vs. eta" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/Efficiency of L2",
        [{'path': thisDir + "/genEffEta_L2", 'description':"Efficiency to find a gen-matched L2 muon associated to a gen-matched L1 muon vs. eta" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/Efficiency of L2 Isolation",
        [{'path': thisDir + "/genEffEta_L2Iso", 'description':"Efficiency to find an isolated gen-matched L2 muon associated to a gen-matched L1 muon vs. eta" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/Efficiency of L3",
        [{'path': thisDir + "/genEffEta_L3", 'description':"Efficiency to find a gen-matched L3 muon associated to a gen-matched L1 muon vs. eta" + thisDocumentation}])

    trigvalmuon(dqmitems, thisMenu + "/Efficiency of L3 Isolation",
        [{'path': thisDir + "/genEffEta_L3Iso", 'description':"Efficiency to find an isolated gen-matched L3 muon associated to a gen-matched L1 muon vs. eta" + thisDocumentation}])

##     trigvalmuon(dqmitems, thisMenu + "/Number of Objects Per Step",
##         [{'path': thisDir + "/numObjects", 'description':"Number of objects found in generated and reconstructed muon collections, and at each step of the " + paths[menuNum] + " trigger path"}])

##     trigvalmuon(dqmitems, thisMenu + "/Number of Orphans per Step",
##         [{'path': thisDir + "/genNumOrphans", 'description':"Number of objects in each step of the " + paths[menuNum] + " trigger path which were not matched to a generated muon"}])


###---- TAU selection goes here: ----
def trigvaltau(i, p, *rows): i["HLT/TauRelVal/Summary For " + p] = DQMItem(layout=rows)

for lumi in ["Default", "8E29","1E31"]:
    trigvaltau(dqmitems,"MC_"+lumi+" Menu/Double Tau Path Performance",
               [{'path': "HLT/TauRelVal/MC_"+lumi+ "/DoubleTau/EfficiencyRefInput",
                 'description':"Efficiency of the Double Tau Path with ref to MC for "+lumi},
                {'path': "HLT/TauRelVal/MC_"+lumi+ "/DoubleTau/EfficiencyRefPrevious",
                 'description':"Efficiency of the Double Tau Path with ref to previous step( "+lumi+")"}

               ])
    trigvaltau(dqmitems,"MC_"+lumi+" Menu/Single Tau Path Performance",
               [
                {'path': "HLT/TauRelVal/MC_"+lumi+ "/SingleTau/EfficiencyRefInput",
                 'description':"Efficiency of the Single Tau Path with ref to MC for "+lumi},
                {'path': "HLT/TauRelVal/MC_"+lumi+ "/SingleTau/EfficiencyRefPrevious",
                 'description':"Efficiency of the Single Tau Path with ref to previous step( "+lumi+")"}
               ])
    trigvaltau(dqmitems,"MC_"+lumi+" Menu/L1 Efficency",
               [
                  {'path': "HLT/TauRelVal/MC_"+lumi+ "/L1/L1TauEtEff", 'description':"L1 Tau Efficiency vs pt with  ref to MC for "+lumi},
                  {'path': "HLT/TauRelVal/MC_"+lumi+ "/L1/L1TauEtaEff", 'description':"L1 Tau Efficiency vs pt with  ref to MC for "+lumi},
               ])

               
    trigvaltau(dqmitems,"MC_"+lumi+" Menu/L2 Efficency",
               [
                  {'path': "HLT/TauRelVal/MC_"+lumi+ "/L2/L2TauEtEff", 'description':"L2 Tau Efficiency vs pt with  ref to MC for "+lumi},
                  {'path': "HLT/TauRelVal/MC_"+lumi+ "/L2/L2TauEtaEff", 'description':"L2 Tau Efficiency vs pt with  ref to MC for "+lumi},
               ])

    trigvaltau(dqmitems,"MC_"+lumi+" Menu/L1 Resolution",
               [
                  {'path': "HLT/TauRelVal/MC_"+lumi+ "/L1/L1TauEtResol", 'description':"L1 Tau ET resolution with ref to MC  for "+lumi}
               ])

    trigvaltau(dqmitems,"MC_"+lumi+" Menu/L2 Resolution",
               [
                  {'path': "HLT/TauRelVal/MC_"+lumi+ "/L2/L2TauEtResol", 'description':"L2 Tau ET resolution with ref to MC  for "+lumi}
               ])
###---- JETMET selection goes here: ----
#def trigvaljetmet(i, p, *rows): i["HLT//Preselection" + p] = DQMItem(layout=rows)

###---- BJET selection goes here: ----
#def trigvalbjet(i, p, *rows): i["HLT//Preselection" + p] = DQMItem(layout=rows)

###---- ALCA selection goes here: ----
def trigvalalca(i, p, *rows): i["HLT/AlCaEcalPi0/Preselection" + p] = DQMItem(layout=rows)

###---- TOP selection goes here: ----
def trigvaltopmuon(i, p, *rows): i["HLT/Top/TopValidationReport/Semileptonic_muon/" + p] = DQMItem(layout=rows)

trigvaltopmuon(dqmitems,"HLTMu9 eff vs eta",
        [{'path': "HLT/Top/Semileptonic_muon/EffVsEta_HLT_Mu9", 'description': "Trigger efficiency for HLTMu9 versus eta of the highest pt reconstructed muon with pt>20, eta<2.1 "}])
trigvaltopmuon(dqmitems,"HLTMu9 eff vs pt",
        [{'path': "HLT/Top/Semileptonic_muon/EffVsPt_HLT_Mu9", 'description': "Trigger efficiency for HLTMu9 versus pt of the highest pt reconstructed muon with pt>20, eta<2.1"}])

trigvaltopmuon(dqmitems,"HLTMu15 eff vs eta",
        [{'path': "HLT/Top/Semileptonic_muon/EffVsEta_HLT_Mu15", 'description': "Trigger efficiency for HLTMu15 versus eta of the highest pt reconstructed muon with pt>20, eta<2.1"}])
trigvaltopmuon(dqmitems,"HLTMu15 eff vs pt",
        [{'path': "HLT/Top/Semileptonic_muon/EffVsPt_HLT_Mu15", 'description': "Trigger efficiency for HLTMu15 versus pt of the highest pt reconstructed muon with pt>20, eta<2.1"}])

trigvaltopmuon(dqmitems,"Muon trigger efficiencies wrt gen",
        [{'path': "HLT/Top/Semileptonic_muon/Efficiencies_MuonTriggers_gen", 'description': "Muon trigger efficiencies wrt mc acceptance (1 muon from W decay, pt>10, eta<2.4)"}])

trigvaltopmuon(dqmitems,"Muon trigger efficiencies wrt gen+reco",
        [{'path': "HLT/Top/Semileptonic_muon/Efficiencies_MuonTriggers", 'description': "Muon trigger efficiencies wrt mc acceptance+offline  (acc: 1 muon from W, pt>10, eta<2.4; off: at least 1 rec muon, pt>20, eta<2.1 and 2 jets Et_raw>13, eta<2.4)"}])


def trigvaltopelectron(i, p, *rows): i["HLT/Top/TopValidationReport/Semileptonic_electron/" + p] = DQMItem(layout=rows)

trigvaltopelectron(dqmitems,"HLTEle15SWL1R eff vs eta",
        [{'path': "HLT/Top/Semileptonic_electron/EffVsEta_HLT_Ele15_SW_L1R", 'description': "Trigger efficiency for HLT_Ele15_SW_L1R versus eta of the highest pt reconstructed electron with pt>20, eta<2.4"}])

trigvaltopelectron(dqmitems,"HLTEle15SWL1R eff vs pt",
        [{'path': "HLT/Top/Semileptonic_electron/EffVsPt_HLT_Ele15_SW_L1R", 'description': "Trigger efficiency for HLT_Ele15_SW_L1R versus pt of the highest pt reconstructed electron with pt>20, eta<2.4"}])


trigvaltopelectron(dqmitems,"HLTEle15SWLooseTrackIsoL1R eff vs eta",
        [{'path': "HLT/Top/Semileptonic_electron/EffVsEta_HLT_Ele15_SW_LooseTrackIso_L1R", 'description': "Trigger efficiency for HLT_Ele15_SW_LooseTrackIso_L1R versus eta of the highest pt reconstructed electron with pt>20, eta<2.4"}])

trigvaltopelectron(dqmitems,"HLTEle15SWLooseTrackIsoL1R eff vs pt",
        [{'path': "HLT/Top/Semileptonic_electron/EffVsPt_HLT_Ele15_SW_LooseTrackIso_L1R", 'description': "Trigger efficiency for HLTEle15_SW_LooseTrackIso_L1R versus pt of the highest pt reconstructed electron with pt>20, eta<2.4"}])

trigvaltopelectron(dqmitems,"Electron trigger efficiencies wrt gen",
        [{'path': "HLT/Top/Semileptonic_electron/Efficiencies_ElectronTriggers_gen", 'description': "Electron trigger efficiencies wrt mc acceptance  (1 electron from W decay, pt>10, eta<2.4)"}])

trigvaltopelectron(dqmitems,"Electron trigger efficiencies wrt gen+reco",
        [{'path': "HLT/Top/Semileptonic_electron/Efficiencies_ElectronTriggers", 'description': "Electron trigger efficiencies wrt mc acceptance+offline  (acc: 1 electron from W, pt>10, eta<2.4; off: at least 1 rec electron, pt>20, eta<2.4 and 2 jets Et_raw>13, eta<2.4)"}])




###---- HEAVYFLAVOR selection goes here: ----

bphysPlotNumber=1
def trigvalbphys(items, title, histogram, description):
  global bphysPlotNumber
  items["HLT/HeavyFlavor/HLTValidationReport/" + '%02d) '%bphysPlotNumber + title] = DQMItem(layout=[[{'path':"HLT/HeavyFlavor/HLT/"+histogram, 'description':description}]])
#  items["HLT/HeavyFlavor/HLT2ValidationReport/" + '%02d) '%bphysPlotNumber + title] = DQMItem(layout=[[{'path':"HLT/HeavyFlavor/HLT2/"+histogram, 'description':description}]])
  bphysPlotNumber+=1

# SUMMARY PLOT

trigvalbphys(dqmitems,
  "Trigger Efficiencies in Di-global Events",
  "effPathGlob_recoPt",
  "Trigger path efficiencies in di-global muon events where the muons are associated to the generated muons as a function of di-muon pT"
)

# SINGLE MUON

trigvalbphys(dqmitems,
  "Glob\Gen Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effGlobGen_genEtaPhi", 
  "Efficiency to find a global muon associated to a generated muon as a function of generated muon Eta and Phi"
)
trigvalbphys(dqmitems,
  "Glob\Gen Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effGlobGen_genEtaPt", 
  "Efficiency to find a global muon associated to a generated muon as a function of generated muon Eta and pT"
)
trigvalbphys(dqmitems,
  "Glob\Gen Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effGlobGen_genEtaPtX", 
  "Efficiency to find a global muon associated to a generated muon as a function of generated muon Eta"
)
trigvalbphys(dqmitems,
  "Glob\Gen Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effGlobGen_genEtaPtY", 
  "Efficiency to find a global muon associated to a generated muon as a function of generated muon pT"
)
trigvalbphys(dqmitems,
  "Glob\Gen Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effGlobGen_genEtaPhiY", 
  "Efficiency to find a global muon associated to a generated muon as a function of generated muon Phi"
)

trigvalbphys(dqmitems,
  "L1\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt1Glob_recoEtaPhi", 
  "Efficiency to find a L1 muon associated to a global+gen muon as a function of global muon Eta and Phi"
)
trigvalbphys(dqmitems,
  "L1\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt1Glob_recoEtaPt", 
  "Efficiency to find a L1 muon associated to a global+gen muon as a function of global muon Eta and pT"
)
trigvalbphys(dqmitems,
  "L1\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt1Glob_recoEtaPtX", 
  "Efficiency to find a L1 muon associated to a global+gen muon as a function of global muon Eta"
)
trigvalbphys(dqmitems,
  "L1\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt1Glob_recoEtaPtY", 
  "Efficiency to find a L1 muon associated to a global+gen muon as a function of global muon pT"
)
trigvalbphys(dqmitems,
  "L1\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt1Glob_recoEtaPhiY", 
  "Efficiency to find a L1 muon associated to a global+gen muon as a function of global muon Phi"
)

trigvalbphys(dqmitems,
  "L2\L1 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt2Filt1_recoEtaPhi", 
  "Efficiency to find a L2 muon associated to a L1+global+gen muon as a function of global muon Eta and Phi"
)
trigvalbphys(dqmitems,
  "L2\L1 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt2Filt1_recoEtaPt", 
  "Efficiency to find a L2 muon associated to a L1+global+gen muon as a function of global muon Eta and pT"
)
trigvalbphys(dqmitems,
  "L2\L1 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt2Filt1_recoEtaPtX", 
  "Efficiency to find a L2 muon associated to a L1+global+gen muon as a function of global muon Eta"
)
trigvalbphys(dqmitems,
  "L2\L1 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt2Filt1_recoEtaPtY", 
  "Efficiency to find a L2 muon associated to a L1+global+gen muon as a function of global muon pT"
)
trigvalbphys(dqmitems,
  "L2\L1 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt2Filt1_recoEtaPhiY", 
  "Efficiency to find a L2 muon associated to a L1+global+gen muon as a function of global muon Phi"
)

trigvalbphys(dqmitems,
  "L3\L2 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Filt2_recoEtaPhi", 
  "Efficiency to find a L3 muon associated to a L2+L1+global+gen muon as a function of global muon Eta and Phi"
)
trigvalbphys(dqmitems,
  "L3\L2 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Filt2_recoEtaPt", 
  "Efficiency to find a L3 muon associated to a L2+L1+global+gen muon as a function of global muon Eta and pT"
)
trigvalbphys(dqmitems,
  "L3\L2 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Filt2_recoEtaPtX", 
  "Efficiency to find a L3 muon associated to a L2+L1+global+gen muon as a function of global muon Eta"
)
trigvalbphys(dqmitems,
  "L3\L2 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Filt2_recoEtaPtY", 
  "Efficiency to find a L3 muon associated to a L2+L1+global+gen muon as a function of global muon pT"
)
trigvalbphys(dqmitems,
  "L3\L2 Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Filt2_recoEtaPhiY", 
  "Efficiency to find a L3 muon associated to a L2+L1+global+gen muon as a function of global muon Phi"
)

trigvalbphys(dqmitems,
  "L3\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Glob_recoEtaPhi", 
  "Efficiency to find a L3 muon associated to a global+gen muon as a function of global muon Eta and Phi"
)
trigvalbphys(dqmitems,
  "L3\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Glob_recoEtaPt", 
  "Efficiency to find a L3 muon associated to a global+gen muon as a function of global muon Eta and pT"
)
trigvalbphys(dqmitems,
  "L3\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Glob_recoEtaPtX", 
  "Efficiency to find a L3 muon associated to a global+gen muon as a function of global muon Eta"
)
trigvalbphys(dqmitems,
  "L3\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Glob_recoEtaPtY", 
  "Efficiency to find a L3 muon associated to a global+gen muon as a function of global muon pT"
)
trigvalbphys(dqmitems,
  "L3\Glob Single Muon Efficiency (HLT_Mu3)",
  "HLT_Mu3/effFilt3Glob_recoEtaPhiY", 
  "Efficiency to find a L3 muon associated to a global+gen muon as a function of global muon Phi"
)

# DOUBLE MUON

trigvalbphys(dqmitems,
  "Glob\Gen Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effGlobDigenAND_genRapPt", 
  "Efficiency to find two global muons associated to two generated muons as a function of generated dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "Glob\Gen Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effGlobDigenAND_genRapPtX", 
  "Efficiency to find two global muons associated to two generated muons as a function of generated dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "Glob\Gen Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effGlobDigenAND_genRapPtY", 
  "Efficiency to find two global muons associated to two generated muons as a function of generated dimuon pT"
)
trigvalbphys(dqmitems,
  "Glob\Gen Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effGlobDigenAND_genPtDR", 
  "Efficiency to find two global muons associated to two generated muons (with pT>7) as a function of generated dimuon pT and DeltaR at Interaction Point"
)
trigvalbphys(dqmitems,
  "Glob\Gen Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effGlobDigenAND_genPtDRY", 
  "Efficiency to find two global muons associated to two generated muons (with pT>7) as a function of generated dimuon DeltaR at Interaction Point"
)

trigvalbphys(dqmitems,
  "L1\Glob Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt1DiglobAND_recoRapPt", 
  "Efficiency to find two L1 muons associated to two global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "L1\Glob Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt1DiglobAND_recoRapPtX", 
  "Efficiency to find two L1 dimuon associated to two global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "L1\Glob Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt1DiglobAND_recoRapPtY", 
  "Efficiency to find two L1 muons associated to two global+gen muons as a function of global dimuon pT"
)
trigvalbphys(dqmitems,
  "L1\Glob Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt1DiglobAND_recoPtDRpos", 
  "Efficiency to find two L1 muons associated to two global+gen muons (with pT>7) as a function of global dimuon pT and DeltaR in the Muon System"
)
trigvalbphys(dqmitems,
  "L1\Glob Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt1DiglobAND_recoPtDRposY", 
  "Efficiency to find two L1 muons associated to two global+gen muons (with pT>7) as a function of global dimuon deltaR in the Muon System"
)

trigvalbphys(dqmitems,
  "L2\L1 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt2Difilt1AND_recoRapPt", 
  "Efficiency to find two L2 muons associated to two L1+global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "L2\L1 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt2Difilt1AND_recoRapPtX", 
  "Efficiency to find two L2 muons associated to two L1+global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "L2\L1 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt2Difilt1AND_recoRapPtY", 
  "Efficiency to find two L2 muons associated to two L1+global+gen muons as a function of global dimuon pT"
)
trigvalbphys(dqmitems,
  "L2\L1 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt2Difilt1AND_recoPtDRpos", 
  "Efficiency to find two L2 muons associated to two L1+global+gen muons (with pT>7) as a function of global dimuon pT and DeltaR in the Muon System"
)
trigvalbphys(dqmitems,
  "L2\L1 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt2Difilt1AND_recoPtDRposY", 
  "Efficiency to find two L2 muons associated to two L1+global+gen muons (with pT>7) as a function of global dimuon DeltaR in the Muon System"
)

trigvalbphys(dqmitems,
  "L3\L2 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt3Difilt2AND_recoRapPt", 
  "Efficiency to find two L3 muons associated to two L2+L1+global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "L3\L2 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt3Difilt2AND_recoRapPtX", 
  "Efficiency to find two L3 muons associated to two L2+L1+global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "L3\L2 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt3Difilt2AND_recoRapPtY", 
  "Efficiency to find two L3 muons associated to two L2+L1+global+gen muons as a function of global dimuon pT"
)
trigvalbphys(dqmitems,
  "L3\L2 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt3Difilt2AND_recoPtDR", 
  "Efficiency to find two L3 muons associated to two L2+L1+global+gen muons (with pT>7) as a function of global dimuon pT and DeltaR at Interaction Point"
)
trigvalbphys(dqmitems,
  "L3\L2 Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt3Difilt2AND_recoPtDRY", 
  "Efficiency to find two L3 muons associated to two L2+L1+global+gen muons (with pT>7) as a function of global dimuon DeltaR at Interaction Point"
)

trigvalbphys(dqmitems,
  "L3\Glob Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt3DiglobAND_recoRapPt", 
  "Efficiency to find two L3 muons associated to two global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "L3\Glob Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt3DiglobAND_recoRapPtX", 
  "Efficiency to find two L3 muons associated to two global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "L3\Glob Dimuon Efficiency (HLT_DoubleMu0)",
  "HLT_DoubleMu0/effFilt3DiglobAND_recoRapPtY", 
  "Efficiency to find two L3 muons associated to two global+gen muons as a function of global dimuon pT"
)

# TRIGGER PATH

trigvalbphys(dqmitems,
  "HLT_Mu3 Efficiency in Di-Global Events",
  "HLT_Mu3/effPathDiglobOR_recoRapPt",
  "Efficiency to find an HLT_Mu3 muon associated to one of the global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "HLT_Mu3 Efficiency in Di-Global Events",
  "HLT_Mu3/effPathDiglobOR_recoRapPtX",
  "Efficiency to find an HLT_Mu3 muon associated to one of the global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "HLT_Mu3 Efficiency in Di-Global Events",
  "HLT_Mu3/effPathDiglobOR_recoRapPtY",
  "Efficiency to find an HLT_Mu3 muon associated to one of the global+gen muons as a function of global dimuon pT"
)

trigvalbphys(dqmitems,
  "HLT_Mu5 Efficiency in Di-Global Events",
  "HLT_Mu5/effPathDiglobOR_recoRapPt",
  "Efficiency to find an HLT_Mu5 muon associated to one of the global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "HLT_Mu5 Efficiency in Di-Global Events",
  "HLT_Mu5/effPathDiglobOR_recoRapPtX",
  "Efficiency to find an HLT_Mu5 muon associated to one of the global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "HLT_Mu5 Efficiency in Di-Global Events",
  "HLT_Mu5/effPathDiglobOR_recoRapPtY",
  "Efficiency to find an HLT_Mu5 muon associated to one of the global+gen muons as a function of global dimuon pT"
)

trigvalbphys(dqmitems,
  "HLT_Mu9 Efficiency in Di-Global Events",
  "HLT_Mu9/effPathDiglobOR_recoRapPt",
  "Efficiency to find an HLT_Mu9 muon associated to one of the global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "HLT_Mu9 Efficiency in Di-Global Events",
  "HLT_Mu9/effPathDiglobOR_recoRapPtX",
  "Efficiency to find an HLT_Mu9 muon associated to one of the global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "HLT_Mu9 Efficiency in Di-Global Events",
  "HLT_Mu9/effPathDiglobOR_recoRapPtY",
  "Efficiency to find an HLT_Mu9 muon associated to one of the global+gen muons as a function of global dimuon pT"
)

trigvalbphys(dqmitems,
  "HLT_DoubleMu0 Efficiency in Di-Global Events",
  "HLT_DoubleMu0/effPathDiglobAND_recoRapPt", 
  "Efficiency to find two HLT_DoubleMu0 muons associated to two global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "HLT_DoubleMu0 Efficiency in Di-Global Events",
  "HLT_DoubleMu0/effPathDiglobAND_recoRapPtX", 
  "Efficiency to find two HLT_DoubleMu0 muons associated to two global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "HLT_DoubleMu0 Efficiency in Di-Global Events",
  "HLT_DoubleMu0/effPathDiglobAND_recoRapPtY", 
  "Efficiency to find two HLT_DoubleMu0 muons associated to two global+gen muons as a function of global dimuon pT"
)

trigvalbphys(dqmitems,
  "HLT_DoubleMu3 Efficiency in Di-Global Events",
  "HLT_DoubleMu3/effPathDiglobAND_recoRapPt", 
  "Efficiency to find two HLT_DoubleMu3 muons associated to two global+gen muons as a function of global dimuon Rapidity and pT"
)
trigvalbphys(dqmitems,
  "HLT_DoubleMu3 Efficiency in Di-Global Events",
  "HLT_DoubleMu3/effPathDiglobAND_recoRapPtX", 
  "Efficiency to find two HLT_DoubleMu3 muons associated to two global+gen muons as a function of global dimuon Rapidity"
)
trigvalbphys(dqmitems,
  "HLT_DoubleMu3 Efficiency in Di-Global Events",
  "HLT_DoubleMu3/effPathDiglobAND_recoRapPtY", 
  "Efficiency to find two HLT_DoubleMu3 muons associated to two global+gen muons as a function of global dimuon pT"
)

###---- SUSYEXO selection goes here: ----
def trigvalsusybsm(i, p, *rows): i["HLT/SusyExo/Preselection" + p] = DQMItem(layout=rows)

###---- HIGGS selection goes here: ----

def trigvalhiggsHWW(i, p, *rows): i["HLT/Higgs/HiggsValidationReport/HWW/" + p] = DQMItem(layout=rows)

trigvalhiggsHWW(dqmitems,"mumu selection: HLTMu9 eff vs eta ",
        [{'path': "HLT/Higgs/HWW/EffVsEta_HLT_Mu9", 'description': "Trigger efficiency for HLTMu9 in the dimuon channel vs eta of the highest pt reconstructed muon ( Event selection: at least 2 globalMuons pt>10,20, eta<2.4, opp charge)"}])

trigvalhiggsHWW(dqmitems,"mumu selection : HLTMu9 eff vs pt",
        [{'path': "HLT/Higgs/HWW/EffVsPt_HLT_Mu9", 'description': "Trigger efficiency for HLTMu9 in the dimuon channel vs Pt of the highest pt reconstructed muon (Event selection: at least 2 globalMuons pt>10,20, eta<2.4, opp charge)"}])

trigvalhiggsHWW(dqmitems,"ee selection :HLTEle10LWL1R eff vs eta ",
        [{'path': "HLT/Higgs/HWW/EffVsEta_HLT_Ele10_LW_L1R", 'description':" Trigger efficiency for  HLTEle10LWL1R in the ee channel vs eta of the highest pt reco electron (Event selection: at least 2 electrons pt>10,20,eta<2.4,opp charge,H/E<0.05,0.6< E/p<2.5)"}])

trigvalhiggsHWW(dqmitems,"ee selection: EffVsPt HLT_Ele10LWL1R ",
        [{'path': "HLT/Higgs/HWW/EffVsPt_HLT_Ele10_LW_L1R", 'description': "Trigger efficiency for HLTEle10_LW_L1R in the ee channel vs Pt of the highest pt reco electron (Event selection: at least 2 electrons pt>10,20, eta<2.4,opp charge, H/E<0.05,0.6< E/p<2.5) "}])

trigvalhiggsHWW(dqmitems,"emu selection: EffVsEta HLTMu9 ",
        [{'path': "HLT/Higgs/HWW/EffVsEta_HLT_Mu9_EM", 'description': "Trigger efficiency for HLTMu9 in the emu channel vs muon eta ( Event selection applied: at least 2 leptons pt>10,20,eta<2.4, opp. charge, muons:globalMuons, electrons:H/E<0.05,0.6< E/p<2.5)"}])

trigvalhiggsHWW(dqmitems,"emu selection: EffVsPt HLTEle10LWL1R ",
        [{'path': "HLT/Higgs/HWW/EffVsPt_HLT_Ele10_LW_L1R_EM", 'description': "Trigger efficiency for HLTEle10_LW_L1R in the emu channel vs electron eta ( Event selection applied: at least 2 leptons pt>10,20,eta<2.4, opp. charge, muons:globalMuons, electrons:H/E<0.05,0.6< E/p<2.5)"}])

trigvalhiggsHWW(dqmitems,"mumu selection : global Efficiencies ",
        [{'path': "HLT/Higgs/HWW/Efficiencies_MuonTriggers", 'description': "Muon Trigger efficiencies in the dimuon channel wrt the events passing the selection (at least 2 globalMuons pt>10,20, eta<2.4, opp charge)"}])

trigvalhiggsHWW(dqmitems,"ee selection: global Efficiencies ",
        [{'path': "HLT/Higgs/HWW/Efficiencies_ElectronTriggers", 'description': "Electron Trigger efficiencies in the dielectron channel wrt the events passing the selection ( at least 2 electrons pt>10,20,eta<2.4, opp. charge, H/E<0.05,0.6< E/p<2.5)"}])

trigvalhiggsHWW(dqmitems,"emu selection: global Efficiencies ",
        [{'path': "HLT/Higgs/HWW/TriggerEfficiencies_EmuChannel", 'description': "Trigger efficiencies in the emu channel wrt the events passing the selection ( at least 2 leptons pt>10,20,eta<2.4, opp. charge, muons:globalMuons, electrons:H/E<0.05, 0.6< E/p<2.5)"}])


def trigvalhiggsHgg(i, p, *rows): i["HLT/Higgs/HiggsValidationReport/Hgg/" + p] = DQMItem(layout=rows)
trigvalhiggsHgg(dqmitems,"HLTDoublePhoton10L1R eff vs eta",
        [{'path': "HLT/Higgs/Hgg/EffVsEta_HLT_DoublePhoton10_L1R", 'description': "Trigger efficiency for HLTDoublePhoton10 versus eta of the highest pt reconstructed photon in the event passing the selection (at least 2 reconstructed photons pt>20, eta<2.4)"}])
trigvalhiggsHgg(dqmitems,"HLTDoublePhoton10L1R vs pt",
        [{'path': "HLT/Higgs/Hgg/EffVsPt_HLT_DoublePhoton10_L1R", 'description': "Trigger efficiency for HLTDoublePhoton10 versus pt of the highest pt reconstructed photon in the event passing the selection (at least 2 reconstructed photons pt>20, eta<2.4)"}])

trigvalhiggsHgg(dqmitems,"Photon global Efficiencies ",
        [{'path': "HLT/Higgs/Hgg/Efficiencies_PhotonTriggers", 'description': "Photon Trigger efficiencies  wrt the events passing the selection (at least 2 reco photons pt>20, eta<2.4)"}])




def trigvalhiggsH2tau(i, p, *rows): i["HLT/Higgs/HiggsValidationReport/H2tau/" + p] = DQMItem(layout=rows)
trigvalhiggsH2tau(dqmitems,"semimu channel: HLTMu3 eff vs eta",
        [{'path': "HLT/Higgs/H2tau/EffVsEta_HLT_Mu3", 'description': "Trigger efficiency for HLTMu3 versus eta of the generated muon from tau decay passing the selection (1 muon from tau pt>15, eta<2.4)"}])

trigvalhiggsH2tau(dqmitems,"semimu channel: HLTMu3 eff vs pt",
        [{'path': "HLT/Higgs/H2tau/EffVsPt_HLT_Mu3", 'description': "Trigger efficiency for HLTMu3 versus pt of the generated muon from tau decay passing the selection (1 muon from tau pt>15, eta<2.4)"}])

trigvalhiggsH2tau(dqmitems,"semielec channel: HLTEle10LW eff vs eta",
        [{'path': "HLT/Higgs/H2tau/EffVsEta_HLT_Ele10_LW_L1R", 'description': "Trigger efficiency for HLTEle10LWL1R versus eta of the generated electron from tau decay passing the selection (1 electron from tau pt>15, eta<2.4)"}])

trigvalhiggsH2tau(dqmitems,"semielec channel: HLTEle10LW eff vs pt",
        [{'path': "HLT/Higgs/H2tau/EffVsPt_HLT_Ele10_LW_L1R", 'description': "Trigger efficiency for HLTEle10LWL1R versus Pt of the generated electron from tau decay passing the selection (1 electron from tau pt>15, eta<2.4)"}])

trigvalhiggsH2tau(dqmitems,"semimuonic channel : global Efficiencies ",
        [{'path': "HLT/Higgs/H2tau/Efficiencies_MuonTriggers", 'description': "Muon Trigger efficiencies  wrt the events passing the muon selection (1 muon from tau decay pt>15, eta<2.4"}])

trigvalhiggsH2tau(dqmitems,"semielectronic channel: global Efficiencies ",
        [{'path': "HLT/Higgs/H2tau/Efficiencies_ElectronTriggers", 'description': "Electron Trigger efficiencies  wrt the events passing the electron selection ( 1 electron from tau pt>15,eta<2.4)"}])



def trigvalhiggsHZZ(i, p, *rows): i["HLT/Higgs/HiggsValidationReport/HZZ/" + p] = DQMItem(layout=rows)

trigvalhiggsHZZ(dqmitems,"4mu selection: HLTMu9 eff vs eta ",
        [{'path': "HLT/Higgs/HZZ/EffVsEta_HLT_Mu9", 'description': "Trigger efficiency for HLTMu9 vs eta of the highest pt reconstructed muon in the event passing the selection (at least 4 globalMuons pt>10, eta<2.4, opp charge"}])

trigvalhiggsHZZ(dqmitems,"4mu selection :HLTMu9 eff vs pt ",
        [{'path': "HLT/Higgs/HZZ/EffVsPt_HLT_Mu9", 'description': "Trigger efficiency for HLTMu9  vs Pt of the highest pt reconstructed muon in the event passing the selection (at least 4 globalMuons pt>10, eta<2.4, opp charge"}])

trigvalhiggsHZZ(dqmitems,"4e selection :HLTEle10LWL1R eff vs eta ",
        [{'path': "HLT/Higgs/HZZ/EffVsEta_HLT_Ele10_LW_L1R", 'description': "Trigger efficiency for HLTEle10_LW_L1R  vs eta of the highest pt reconstructed electron in the event passing the selection (at least 4 gsfElectrons pt>10, eta<2.4,opp charge, H/E<0.05, 0.6< E/p<2.5) "}])

trigvalhiggsHZZ(dqmitems,"4e selection: HLT_Ele10LWL1R  eff vs pt",
        [{'path': "HLT/Higgs/HZZ/EffVsPt_HLT_Ele10_LW_L1R", 'description': "Trigger efficiency for HLTEle10_LW_L1R  vs Pt of the highest pt reconstructed electron in the event passing the selection (at least 4 gsfElectrons pt>10, eta<2.4,opp charge, H/E<0.05, 0.6< E/p<2.5) "}])

trigvalhiggsHZZ(dqmitems,"2e2mu selection: HLTMu9 eff vs eta ",
        [{'path': "HLT/Higgs/HZZ/EffVsEta_HLT_Mu9_EM", 'description': "Trigger efficiency for HLTMu9  vs eta of the highest pt reconstructed muon in the event passing the selection ( at least 2 muons and 2 electrons  pt>10,eta<2.4, opp. charge, muons:globalMuons, electrons:H/E<0.05, 0.6< E/p<2.5)"}])

trigvalhiggsHZZ(dqmitems,"2e2mu selection: HLTEle10LWL1R eff vs pt ",
        [{'path': "HLT/Higgs/HZZ/EffVsPt_HLT_Ele10_LW_L1R_EM", 'description': "Trigger efficiency for HLTEle10_LW_L1R  vs pt of the highest pt reconstructed electron in the event passing the selection ( at least 2 muons and 2 electrons pt>10,eta<2.4, opp. charge, muons:globalMuons, electrons:H/E<0.05,0.6< E/p<2.5)"}])

trigvalhiggsHZZ(dqmitems,"4mu selection : global Efficiencies ",
        [{'path': "HLT/Higgs/HZZ/Efficiencies_MuonTriggers", 'description': "Muon Trigger efficiencies  wrt the events passing the selection (at least 4 globalMuons pt>10, eta<2.4, opp charge"}])

trigvalhiggsHZZ(dqmitems,"4e selection: global Efficiencies ",
        [{'path': "HLT/Higgs/HZZ/Efficiencies_ElectronTriggers", 'description': "Electron Trigger efficiencies wrt the events passing the selection ( at least 4 electrons pt>10,eta<2.4, opp. charge, H/E<0.05, 0.6< E/p<2.5)"}])

trigvalhiggsHZZ(dqmitems,"2e2mu selection: global Efficiencies ",
        [{'path': "HLT/Higgs/HZZ/TriggerEfficiencies_EmuChannel", 'description': "Trigger efficiencies  wrt the events passing the selection ( at least 2 muons and 2 electrons pt>10,20,eta<2.4, opp. charge, muons:globalMuons, electrons:H/E<0.05, 0.6< E/p<2.5)"}])


def trigvalhiggsHtaunu(i, p, *rows): i["HLT/Higgs/HiggsValidationReport/Htaunu/" + p] = DQMItem(layout=rows)

trigvalhiggsHtaunu(dqmitems,"Tau global Efficiencies ",
        [{'path': "HLT/Higgs/Htaunu/globalEfficiencies", 'description': "Tau trigger efficiencies  wrt the events passing the selection ( at least 1 gen tau pt>100,eta<2.4)"}])








###---- QCD selection goes here: ----
#def trigvalqcd(i, p, *rows): i["HLT//Preselection" + p] = DQMItem(layout=rows)
