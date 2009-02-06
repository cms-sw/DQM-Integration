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
           [{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"},
            {'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency by step", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/gen et", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"},
            {'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/gen eta", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoDoubleElectronEt5L1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5L1MatchFilterRegional in doubleEle5SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoDoubleElectronEt5L1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5L1MatchFilterRegional in doubleEle5SWL1R vs et"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoDoubleElectronEt5EtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5EtFilter in doubleEle5SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoDoubleElectronEt5EtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5EtFilter in doubleEle5SWL1R vs et"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonHLTnonIsoIsoDoubleElectronEt5HcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonHLTnonIsoIsoDoubleElectronEt5HcalIsolFilter in doubleEle5SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonHLTnonIsoIsoDoubleElectronEt5HcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonHLTnonIsoIsoDoubleElectronEt5HcalIsolFilter in doubleEle5SWL1R vs et"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoDoubleElectronEt5PixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5PixelMatchFilter in doubleEle5SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoDoubleElectronEt5PixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5PixelMatchFilter in doubleEle5SWL1R vs et"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/track match",
           [{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTnonIsoDoubleElectronEt5HOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTnonIsoDoubleElectronEt5HOneOEMinusOneOPFilter in doubleEle5SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTnonIsoDoubleElectronEt5HOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTnonIsoDoubleElectronEt5HOneOEMinusOneOPFilter in doubleEle5SWL1R vs et"}])

trigvalegammaZ(dqmitems,"doubleEle5SWL1R/track isolation",
           [{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoDoubleElectronEt5TrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5TrackIsolFilter in doubleEle5SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoDoubleElectronEt5TrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoDoubleElectronEt5TrackIsolFilter in doubleEle5SWL1R vs et"}])


trigvalegammaZ(dqmitems,"doubleElectron/total",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleElectron"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency by step", 'description':"per-event efficiency (MC matched) for doubleElectron"}])

trigvalegammaZ(dqmitems,"doubleElectron/kinematics",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/gen et", 'description':"per-event efficiency (MC matched) for doubleElectron"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/gen eta", 'description':"per-event efficiency (MC matched) for doubleElectron"}])

trigvalegammaZ(dqmitems,"doubleElectron/L1 match",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronL1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronL1MatchFilterRegional in doubleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronL1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronL1MatchFilterRegional in doubleElectron vs et"}])

trigvalegammaZ(dqmitems,"doubleElectron/Et cut",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronEtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronEtFilter in doubleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronEtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronEtFilter in doubleElectron vs et"}])

trigvalegammaZ(dqmitems,"doubleElectron/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronHcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronHcalIsolFilter in doubleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronHcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronHcalIsolFilter in doubleElectron vs et"}])

trigvalegammaZ(dqmitems,"doubleElectron/pixel match",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronPixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronPixelMatchFilter in doubleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronPixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronPixelMatchFilter in doubleElectron vs et"}])

trigvalegammaZ(dqmitems,"doubleElectron/track match",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronEoverpFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronEoverpFilter in doubleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronEoverpFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronEoverpFilter in doubleElectron vs et"}])

trigvalegammaZ(dqmitems,"doubleElectron/track isolation",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronTrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronTrackIsolFilter in doubleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency hltL1IsoDoubleElectronTrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoDoubleElectronTrackIsolFilter in doubleElectron vs et"}])



trigvalegammaZ(dqmitems,"doubleElectronRelaxed/total",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleElectronRelaxed"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency by step", 'description':"per-event efficiency (MC matched) for doubleElectronRelaxed"}])

trigvalegammaZ(dqmitems,"doubleElectronRelaxed/kinematics",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/gen et", 'description':"per-event efficiency (MC matched) for doubleElectronRelaxed"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/gen eta", 'description':"per-event efficiency (MC matched) for doubleElectronRelaxed"}])

trigvalegammaZ(dqmitems,"doubleElectronRelaxed/L1 match",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronL1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronL1MatchFilterRegional in doubleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronL1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronL1MatchFilterRegional in doubleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"doubleElectronRelaxed/Et cut",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronEtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronEtFilter in doubleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronEtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronEtFilter in doubleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"doubleElectronRelaxed/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronHcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronHcalIsolFilter in doubleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronHcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronHcalIsolFilter in doubleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"doubleElectronRelaxed/pixel match",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronPixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronPixelMatchFilter in doubleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronPixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronPixelMatchFilter in doubleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"doubleElectronRelaxed/track match",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronEoverpFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronEoverpFilter in doubleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronEoverpFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronEoverpFilter in doubleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"doubleElectronRelaxed/track isolation",
           [{'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronTrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronTrackIsolFilter in doubleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/doubleElectronRelaxedDQMZee/efficiency hltL1NonIsoDoubleElectronTrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoDoubleElectronTrackIsolFilter in doubleEle5SWL1R vs et"}])



trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R/total",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency by step", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"}])

trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/gen et", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/gen eta", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"}])

trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15L1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15L1MatchFilterRegional in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15L1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15L1MatchFilterRegional in looseIsoEle15LWL1R vs et"}])

trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15EtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15EtFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15EtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15EtFilter in looseIsoEle15LWL1R vs et"}])

trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HcalIsolFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HcalIsolFilter in looseIsoEle15LWL1R vs et"}])

trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15PixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15PixelMatchFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15PixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15PixelMatchFilter in looseIsoEle15LWL1R vs et"}])

trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R/track match",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HOneOEMinusOneOPFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HOneOEMinusOneOPFilter in looseIsoEle15LWL1R vs et"}])

trigvalegammaZ(dqmitems,"looseIsoEle15LWL1R/track isolation",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15TrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15TrackIsolFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15TrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15TrackIsolFilter in looseIsoEle15LWL1R vs et"}])

        
        
trigvalegammaZ(dqmitems,"ele15SWL1R/total",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for ele15SWL1R"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency by step", 'description':"per-event efficiency (MC matched) for ele15SWL1R"}])

trigvalegammaZ(dqmitems,"ele15SWL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/gen et", 'description':"per-event efficiency (MC matched) for ele15SWL1R"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/gen eta", 'description':"per-event efficiency (MC matched) for ele15SWL1R"}])

trigvalegammaZ(dqmitems,"ele15SWL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15L1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15L1MatchFilterRegional in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15L1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15L1MatchFilterRegional in ele15SWL1R vs et"}])

trigvalegammaZ(dqmitems,"ele15SWL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15EtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15EtFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15EtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15EtFilter in ele15SWL1R vs et"}])

trigvalegammaZ(dqmitems,"ele15SWL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15HcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15HcalIsolFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15HcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15HcalIsolFilter in ele15SWL1R vs et"}])

trigvalegammaZ(dqmitems,"ele15SWL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter in ele15SWL1R vs et"}])

trigvalegammaZ(dqmitems,"ele15SWL1R/track match",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15HOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15HOneOEMinusOneOPFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15HOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15HOneOEMinusOneOPFilter in ele15SWL1R vs et"}])

trigvalegammaZ(dqmitems,"ele15SWL1R/track isolation",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15TrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15TrackIsolFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15TrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15TrackIsolFilter in ele15SWL1R vs et"}])


trigvalegammaZ(dqmitems,"singleElectron/total",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singleElectron"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency by step", 'description':"per-event efficiency (MC matched) for singleElectron"}])

trigvalegammaZ(dqmitems,"singleElectron/kinematics",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/gen et", 'description':"per-event efficiency (MC matched) for singleElectron"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/gen eta", 'description':"per-event efficiency (MC matched) for singleElectron"}])

trigvalegammaZ(dqmitems,"singleElectron/L1 match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleL1MatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleL1MatchFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleL1MatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleL1MatchFilter in singleElectron vs et"}])

trigvalegammaZ(dqmitems,"singleElectron/Et cut",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronEtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronEtFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronEtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronEtFilter in singleElectron vs et"}])

trigvalegammaZ(dqmitems,"singleElectron/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronHcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronHcalIsolFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronHcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronHcalIsolFilter in singleElectron vs et"}])

trigvalegammaZ(dqmitems,"singleElectron/pixel match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronPixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronPixelMatchFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronPixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronPixelMatchFilter in singleElectron vs et"}])

trigvalegammaZ(dqmitems,"singleElectron/track match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronHOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronHOneOEMinusOneOPFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronHOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronHOneOEMinusOneOPFilter in singleElectron vs et"}])

trigvalegammaZ(dqmitems,"singleElectron/track isolation",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronTrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronTrackIsolFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency hltL1IsoSingleElectronTrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronTrackIsolFilter in singleElectron vs et"}])




        
trigvalegammaZ(dqmitems,"singleElectronRelaxed/total",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singleElectronRelaxed"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency by step", 'description':"per-event efficiency (MC matched) for singleElectronRelaxed"}])

trigvalegammaZ(dqmitems,"singleElectronRelaxed/kinematics",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/gen et", 'description':"per-event efficiency (MC matched) for singleElectronRelaxed"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/gen eta", 'description':"per-event efficiency (MC matched) for singleElectronRelaxed"}])

trigvalegammaZ(dqmitems,"singleElectronRelaxed/L1 match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronL1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronL1MatchFilterRegional in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronL1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronL1MatchFilterRegional in singleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"singleElectronRelaxed/Et cut",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronEtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronEtFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronEtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronEtFilter in singleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"singleElectronRelaxed/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronHcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronHcalIsolFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronHcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronHcalIsolFilter in singleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"singleElectronRelaxed/pixel match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronPixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronPixelMatchFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronPixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronPixelMatchFilter in singleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"singleElectronRelaxed/track match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronHOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronHOneOEMinusOneOPFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronHOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronHOneOEMinusOneOPFilter in singleElectronRelaxed vs et"}])

trigvalegammaZ(dqmitems,"singleElectronRelaxed/track isolation",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronTrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronTrackIsolFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronTrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronTrackIsolFilter in singleElectronRelaxed vs et"}])




                            

def hltlayoutW(i, p, *rows): i["HLT/HLTEgammaValidation/Wenu Preselection/" + p] = DQMItem(layout=rows)

hltlayoutW(dqmitems,"looseIsoEle15LWL1R/total",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency by step", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"}])

hltlayoutW(dqmitems,"looseIsoEle15LWL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/gen et", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/gen eta", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"}])

hltlayoutW(dqmitems,"looseIsoEle15LWL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15L1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15L1MatchFilterRegional in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15L1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15L1MatchFilterRegional in looseIsoEle15LWL1R vs et"}])

hltlayoutW(dqmitems,"looseIsoEle15LWL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15EtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15EtFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15EtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15EtFilter in looseIsoEle15LWL1R vs et"}])

hltlayoutW(dqmitems,"looseIsoEle15LWL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HcalIsolFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HcalIsolFilter in looseIsoEle15LWL1R vs et"}])

hltlayoutW(dqmitems,"looseIsoEle15LWL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15PixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15PixelMatchFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15PixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15PixelMatchFilter in looseIsoEle15LWL1R vs et"}])

hltlayoutW(dqmitems,"looseIsoEle15LWL1R/track match",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HOneOEMinusOneOPFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15HOneOEMinusOneOPFilter in looseIsoEle15LWL1R vs et"}])

hltlayoutW(dqmitems,"looseIsoEle15LWL1R/track isolation",
           [{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15TrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15TrackIsolFilter in looseIsoEle15LWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency hltL1NonIsoHLTLooseIsoSingleElectronLWEt15TrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTLooseIsoSingleElectronLWEt15TrackIsolFilter in looseIsoEle15LWL1R vs et"}])


        
hltlayoutW(dqmitems,"ele15SWL1R/total",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for ele15SWL1R"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency by step", 'description':"per-event efficiency (MC matched) for ele15SWL1R"}])

hltlayoutW(dqmitems,"ele15SWL1R/kinematics",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/gen et", 'description':"per-event efficiency (MC matched) for ele15SWL1R"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/gen eta", 'description':"per-event efficiency (MC matched) for ele15SWL1R"}])

hltlayoutW(dqmitems,"ele15SWL1R/L1 match",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15L1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15L1MatchFilterRegional in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15L1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15L1MatchFilterRegional in ele15SWL1R vs et"}])

hltlayoutW(dqmitems,"ele15SWL1R/Et cut",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15EtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15EtFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15EtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15EtFilter in ele15SWL1R vs et"}])

hltlayoutW(dqmitems,"ele15SWL1R/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15HcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15HcalIsolFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15HcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15HcalIsolFilter in ele15SWL1R vs et"}])

hltlayoutW(dqmitems,"ele15SWL1R/pixel match",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15PixelMatchFilter in ele15SWL1R vs et"}])

hltlayoutW(dqmitems,"ele15SWL1R/track match",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15HOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15HOneOEMinusOneOPFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15HOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15HOneOEMinusOneOPFilter in ele15SWL1R vs et"}])

hltlayoutW(dqmitems,"ele15SWL1R/track isolation",
           [{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15TrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15TrackIsolFilter in ele15SWL1R vs eta"},
            {'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency hltL1NonIsoHLTNonIsoSingleElectronEt15TrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoHLTNonIsoSingleElectronEt15TrackIsolFilter in ele15SWL1R vs et"}])




hltlayoutW(dqmitems,"singleElectron/total",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singleElectron"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency by step", 'description':"per-event efficiency (MC matched) for singleElectron"}])

hltlayoutW(dqmitems,"singleElectron/kinematics",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/gen et", 'description':"per-event efficiency (MC matched) for singleElectron"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/gen eta", 'description':"per-event efficiency (MC matched) for singleElectron"}])

hltlayoutW(dqmitems,"singleElectron/L1 match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleL1MatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleL1MatchFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleL1MatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleL1MatchFilter in singleElectron vs et"}])

hltlayoutW(dqmitems,"singleElectron/Et cut",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronEtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronEtFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronEtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronEtFilter in singleElectron vs et"}])

hltlayoutW(dqmitems,"singleElectron/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronHcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronHcalIsolFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronHcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronHcalIsolFilter in singleElectron vs et"}])

hltlayoutW(dqmitems,"singleElectron/pixel match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronPixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronPixelMatchFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronPixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronPixelMatchFilter in singleElectron vs et"}])

hltlayoutW(dqmitems,"singleElectron/track match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronHOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronHOneOEMinusOneOPFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronHOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronHOneOEMinusOneOPFilter in singleElectron vs et"}])

hltlayoutW(dqmitems,"singleElectron/track isolation",
           [{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronTrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronTrackIsolFilter in singleElectron vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency hltL1IsoSingleElectronTrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1IsoSingleElectronTrackIsolFilter in singleElectron vs et"}])


        
hltlayoutW(dqmitems,"singleElectronRelaxed/total",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singleElectronRelaxed"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency by step", 'description':"per-event efficiency (MC matched) for singleElectronRelaxed"}])

hltlayoutW(dqmitems,"singleElectronRelaxed/kinematics",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/gen et", 'description':"per-event efficiency (MC matched) for singleElectronRelaxed"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/gen eta", 'description':"per-event efficiency (MC matched) for singleElectronRelaxed"}])

hltlayoutW(dqmitems,"singleElectronRelaxed/L1 match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronL1MatchFilterRegional vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronL1MatchFilterRegional in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronL1MatchFilterRegional vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronL1MatchFilterRegional in singleElectronRelaxed vs et"}])

hltlayoutW(dqmitems,"singleElectronRelaxed/Et cut",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronEtFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronEtFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronEtFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronEtFilter in singleElectronRelaxed vs et"}])

hltlayoutW(dqmitems,"singleElectronRelaxed/Hcal isolation",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronHcalIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronHcalIsolFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronHcalIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronHcalIsolFilter in singleElectronRelaxed vs et"}])

hltlayoutW(dqmitems,"singleElectronRelaxed/pixel match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronPixelMatchFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronPixelMatchFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronPixelMatchFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronPixelMatchFilter in singleElectronRelaxed vs et"}])

hltlayoutW(dqmitems,"singleElectronRelaxed/track match",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronHOneOEMinusOneOPFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronHOneOEMinusOneOPFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronHOneOEMinusOneOPFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronHOneOEMinusOneOPFilter in singleElectronRelaxed vs et"}])

hltlayoutW(dqmitems,"singleElectronRelaxed/track isolation",
           [{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronTrackIsolFilter vs eta MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronTrackIsolFilter in singleElectronRelaxed vs eta"},
            {'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency hltL1NonIsoSingleElectronTrackIsolFilter vs et MC matched", 'description':"per-object (MC matched) for hltL1NonIsoSingleElectronTrackIsolFilter in singleElectronRelaxed vs et"}])



###---- MUON selection goes here: ----

def trigvalmuon(i, p, *rows): i["HLT/Muon/Preselection" + p] = DQMItem(layout=rows)
#trigvalmuon(dqmitems,"", [{'path': "", 'description':""}, {'path': "", 'description':""}])

###---- TAU selection goes here: ----
def trigvaltau(i, p, *rows): i["HLT/HLTTAU/Preselection" + p] = DQMItem(layout=rows)

###---- JETMET selection goes here: ----
#def trigvaljetmet(i, p, *rows): i["HLT//Preselection" + p] = DQMItem(layout=rows)

###---- BJET selection goes here: ----
#def trigvalbjet(i, p, *rows): i["HLT//Preselection" + p] = DQMItem(layout=rows)

###---- ALCA selection goes here: ----
def trigvalalca(i, p, *rows): i["HLT/AlCaEcalPi0/Preselection" + p] = DQMItem(layout=rows)

###---- TOP selection goes here: ----
def trigvaltop(i, p, *rows): i["HLT/Top/Preselection" + p] = DQMItem(layout=rows)

###---- HEAVYFLAVOR selection goes here: ----
def trigvalbphys(i, p, *rows): i["HLT/HeavyFlavor/Preselection" + p] = DQMItem(layout=rows)

###---- SUSYEXO selection goes here: ----
def trigvalsusybsm(i, p, *rows): i["HLT/SusyExo/Preselection" + p] = DQMItem(layout=rows)

###---- HIGGS selection goes here: ----
#def trigvalhiggs(i, p, *rows): i["HLT//Preselection" + p] = DQMItem(layout=rows)
###---- QCD selection goes here: ----
#def trigvalqcd(i, p, *rows): i["HLT//Preselection" + p] = DQMItem(layout=rows)
