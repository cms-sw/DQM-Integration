def shiftHcalLayout(i, p, *rows): i["Shift/Hcal/" + p] = DQMItem(layout=rows)


shiftHcalLayout(dqmitems,"Shifter Hcal Summary",
                # DataFormatMonitor, DigiMonitor
                ["HTR Error Word by Crate",
                 "BCN from HTRs",
                 "Number of Event Fragments by FED ID",
                 "Digi Depth 1 Occupancy Map", # need to add all depths?
                 "Bad Digi Fraction",
                 ],
                # 2 hists each from RecHitMonitor, TrigPrim Monitor
                ["RecHit Eta Energy Map",
                 "RecHit Phi Energy Map",
                 "TrigPrim Geo Energy Map",
                 "TP Timing"],

                # DeadCellMonitor, HotCellMonitor
                [
                 "HCAL_CoolCell_belowPed",
                 "HCALHotCellEnergyMapThresh0",
                 "HCALnadaOccMap"])
