def hltvallayout(i, p, *rows): i["HLT/Layouts/" + p] = DQMItem(layout=rows)

def hlt_egamma(i, dir, name):
  i["HLT/Layouts/00-EGamma-Summary/%s" % name] = \
    DQMItem(layout=[["HLT/%s/%s" % (dir, name)]]) 

def hlt_muon(i, dir, name):
  i["HLT/Layouts/00-Muon-Summary/%s" % name] = \
    DQMItem(layout=[["HLT/%s/%s" % (dir, name)]]) 

def hlt_tau(i, dir, name):
  i["HLT/Layouts/00-Tau-Summary/%s" % name] = \
    DQMItem(layout=[["HLT/%s/%s" % (dir, name)]]) 

def hlt_top(i, dir, name):
  i["HLT/Layouts/00-Top-Summary/%s" % name] = \
    DQMItem(layout=[["HLT/%s/%s" % (dir, name)]]) 

def hlt_alca(i, dir, name):
  i["HLT/Layouts/00-AlCa-Summary/%s" % name] = \
    DQMItem(layout=[["HLT/%s/%s" % (dir, name)]]) 

#def hlt_bsm(i, dir, name):
#  i["HLT/Layouts/00-SusyExo-Summary/%s" % name] = \
#    DQMItem(layout=[["HLT/%s/%s" % (dir, name)]]) 


# list of summary histograms (dqmitems, dirPath , histoName)

#hlt_egamma (dqmitems,"","")
hlt_egamma (dqmitems, "HLTEgammaValidation/singleElectronDQMWnu", "total_eff")

#hlt_muon   (dqmitems,"","")
hlt_muon   (dqmitems,"Muon/Distributions/HLT_IsoMu9","GenEffEta_L1Filtered")

#hlt_tau    (dqmitems,"","")
hlt_tau    (dqmitems,"HLTTAU/SingleTau","Triggers")

#hlt_top    (dqmitems,"","")
hlt_top    (dqmitems,"Top","EffPt_Mu15")

#hlt_alca   (dqmitems,"","")
hlt_alca   (dqmitems,"AlCaEcalPi0","Pi0InvmassEB")
hlt_alca   (dqmitems,"EcalPhiSym","eventEnergyEB")

#hlt_bsm    (dqmitems,"","")
