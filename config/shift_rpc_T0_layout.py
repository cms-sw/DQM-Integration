def shiftrpclayout(i, p, *rows): i["00 Shift/RPC/" + p] = DQMItem(layout=rows)


fed = "FED Fatal Errors. Entries MUST be ZERO at all times. If not, report the problem and ask to stop the run."
rpcevents = "Number of processed events."
eff = "RPC Efficiency distribution. Make sure average values is greater than 80.";
rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>";
quality = "Overview of system quality. Expressed in percentage of chambers."
occupancy = "Occupancy per sector"

shiftrpclayout(dqmitems, "00-FED_Fatal_Errors",
               [{ 'path': "RPC/FEDIntegrity/FEDFatal", 'description': fed + rpclink }])
          

shiftrpclayout(dqmitems, "01-RPC_Events",
               [{ 'path': "RPC/RecHits/SummaryHistograms/RPCEvents", 'description': rpcevents + rpclink }])


shiftrpclayout(dqmitems, "02-Quality_State_Overview",
               [{ 'path': "RPC/RecHits/SummaryHistograms/RPC_System_Quality_Overview", 'description': quality + rpclink }])


shiftrpclayout(dqmitems, "03-RPC_Occupancy",
               [{ 'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink  }],
               [{ 'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_EndcapNegative", 'description': occupancy + rpclink  },
                { 'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_EndcapPositive", 'description':  occupancy + rpclink }])


shiftrpclayout(dqmitems, "04-Statistics",
               [{ 'path': "RPC/RPCEfficiency/EffBarrelRoll", 'description': eff + rpclink }])


shiftrpclayout(dqmitems, "05-Efficiency_Distribution",
               [{ 'path': "RPC/RPCEfficiency/EffBarrelRoll", 'description': eff + rpclink  }],
               [{ 'path': "RPC/RPCEfficiency/EffEndcapPlusRoll", 'description': eff + rpclink  },
                { 'path': "RPC/RPCEfficiency/EffEndcapMinusRoll", 'description':  eff + rpclink }])

