def hltlayout(i, p, *rows): i["HLT/Layouts/" + p] = DQMItem(layout=rows)

def hlt_evInfo_single(i, dir, name):
  i["HLT/Layouts/00-FourVector-Summary/%s" % name] = \
    DQMItem(layout=[["HLT/%s/%s" % (dir, name)]]) 



# list of summary GT histograms (dqmitems, dirPath , histoName)
hlt_evInfo_single(dqmitems, "FourVectorHLT", "HLT1Electron_etaphi")

########################################
########## TPG Summary #################
#######################################

def tpgSummary_l1t(i, p, *rows): 
   i["L1T/Layouts/TPG-Summary-L1T/" + p] = DQMItem(layout=rows)


tpgSummary_l1t(dqmitems, "01 - L1 Predeadtime Rate - Physics",
           [{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/Physics Trigger Rate", 'description':"Physics Predeadtime"}])
           

tpgSummary_l1t(dqmitems, "02 - L1 Predeadtime Rate - Technical",
           [{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/TechnicalRates/Rate_TechBit_005", 'description':"Technical Predeadtime"}])
           

tpgSummary_l1t(dqmitems, "03.01 - Muon Timing DT vs CSC",
           [{'path': "L1T/L1TGMT/bx_DT_vs_CSC", 'description':"Muon Timing"}])

tpgSummary_l1t(dqmitems, "03.02 - Muon Timing DT vs RPC",
           [{'path': "L1T/L1TGMT/bx_DT_vs_RPC", 'description':"Muon Timing"}])

tpgSummary_l1t(dqmitems, "03.03 - Muon Timing DT vs RPC",
           [{'path': "L1T/L1TGMT/bx_CSC_vs_RPC", 'description':"Muon Timing"}])


######################## TPG HLT ################################3

def tpgSummary_hlt(i, p, *rows): 
   i["HLT/Layouts/TPG-Summary-HLT/" + p] = DQMItem(layout=rows)


tpgSummary_hlt(dqmitems, "01 - HLT Postdeadtime Rate",
           [{'path': "HLT/HLTScalers_SM/hltRate", 'description':"HLT Rate Postdeadtime"}])

tpgSummary_hlt(dqmitems, "02 - HLT MinBiasBSC Counts",
           [{'path': "HLT/FourVector/PathsSummary/HLT LS/Paths/HLT_MinBiasBSC_count_per_LS", 'description':"HLT MinBias BSC Counts per lumi sec"}])

tpgSummary_hlt(dqmitems, "03 - HLT MinBiasBSC Counts",
           [{'path': "HLT/FourVector/PathsSummary/HLT LS/Paths/HLT_MinBiasPixel_SingleTrack_count_per_LS", 'description':"HLT MinBias Pixel Counts per lumi sec"}])
