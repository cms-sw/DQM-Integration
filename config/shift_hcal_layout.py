def shiftHcalLayout(i, p, *rows): i["Shift/Hcal/" + p] = DQMItem(layout=rows)


shiftHcalLayout(dqmitems,"Shifter Hcal Summary",
                # DataFormatMonitor, DigiMonitor
                ["HTR Error Word by Crate",
                 "BCN from HTRs",
                 "Ev Frag Size 2d",
                 "Bad Digi Fraction"],
                 ["Digi Depth 1 Occupancy Map",
                  "Digi Depth 2 Occupancy Map",
                  "Digi Depth 3 Occupancy Map",
                  "Digi Depth 4 Occupancy Map"],

                # 2 hists each from RecHitMonitor, TrigPrim Monitor
                ["RecHit Eta Energy Map",
                 "RecHit Phi Energy Map",
                 "TrigPrim Geo Energy Map",
                 "TP Timing"],

                # DeadCellMonitor, HotCellMonitor
                ["HCAL_CoolCell_belowPed",
                 "HCALHotCellEnergyMapThresh0",
                 "HCALnadaOccMap"])
