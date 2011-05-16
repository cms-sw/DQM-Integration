def shiftrpclayout(i, p, *rows): i["00 Shift/RPC/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings ############# 
rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" 
fed = "FED Fatal Errors";
rpcevents = "Events processed by the RPC DQM"
quality = "Overview of system quality. Expressed in percentage of chambers."
occupancy = "Occupancy per sector"


################### Links to Histograms #################################

#FED Fatal
shiftrpclayout(dqmitems, "01-Fatal_FED_Errors",
               [{ 'path': "RPC/FEDIntegrity/FEDFatal", 'description': fed + rpclink }])

#RPC Events
shiftrpclayout(dqmitems, "02-RPC_Events",
               [{ 'path': "RPC/AllHits/SummaryHistograms/RPCEvents", 'description': rpcevents + rpclink }])


shiftrpclayout(dqmitems, "03-Quality_State_Overview",
               [{ 'path': "RPC/AllHits/SummaryHistograms/RPC_System_Quality_Overview", 'description': quality + rpclink }])


shiftrpclayout(dqmitems, "04-RPC_Occupancy",
               [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink  }],
               [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_EndcapNegative", 'description': occupancy + rpclink  },
                { 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_EndcapPositive", 'description':  occupancy + rpclink }])
