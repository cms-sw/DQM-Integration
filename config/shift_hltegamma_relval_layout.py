def hltlayoutZ(i, p, *rows): i["00 Shift/HLT/Egamma/Zee Preselection/" + p] = DQMItem(layout=rows)
  
hltlayoutZ(dqmitems,"doubleEle5SWL1R",
[{'path': "HLT/HLTEgammaValidation/doubleEle5SWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleEle5SWL1R"}])

hltlayoutZ(dqmitems,"doubleElectron",
[{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleElectron"}])

hltlayoutZ(dqmitems,"doubleElectronRelaxed",
[{'path': "HLT/HLTEgammaValidation/doubleElectronDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for doubleElectron"}])

hltlayoutZ(dqmitems,"singleElectron",
[{'path': "HLT/HLTEgammaValidation/singleElectronDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singelElectron"}])

hltlayoutZ(dqmitems,"singleElectronRelaxed",
[{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singelElectronRelaxed"}])

hltlayoutZ(dqmitems,"ele15SWL1R",
[{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for ele15SWL1R"}])

hltlayoutZ(dqmitems,"looseIsoEle15LWL1R",
[{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMZee/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"}])



def hltlayoutW(i, p, *rows): i["00 Shift/HLT/Egamma/Wenu Preselection/" + p] = DQMItem(layout=rows)

hltlayoutW(dqmitems,"singleElectron",
[{'path': "HLT/HLTEgammaValidation/singleElectronDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singelElectron"}])

hltlayoutW(dqmitems,"singleElectronRelaxed",
[{'path': "HLT/HLTEgammaValidation/singleElectronRelaxedDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for singelElectronRelaxed"}])

hltlayoutW(dqmitems,"ele15SWL1R",
[{'path': "HLT/HLTEgammaValidation/ele15SWL1RDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for ele15SWL1R"}])

hltlayoutW(dqmitems,"looseIsoEle15LWL1R",
[{'path': "HLT/HLTEgammaValidation/looseIsoEle15LWL1RDQMWenu/efficiency by step MC matched", 'description':"per-event efficiency (MC matched) for looseIsoEle15LWL1R"}])

