def shiftHcalLayout(i, p, *rows): i["Shift/Hcal/" + p] = DQMItem(layout=rows)


shiftHcalLayout(dqmitems,"Shifter Hcal Summary",
                # DataFormatMonitor, DigiMonitor
                [{ 'path': "Hcal/DataFormatMonitor/HTR Error Word by Crate",
                   'description': 'Ignore only OpDat Err, Clock Err, Link Err, CapID Err, and FE Format Err' },
                 "Hcal/DigiMonitor/Bad Digi Fraction",
                 "Hcal/DataFormatMonitor/Ev Frag Size 2d"],
                 ["Hcal/DigiMonitor/Digi Depth 1 Occupancy Map",
                  "Hcal/DigiMonitor/Digi Depth 2 Occupancy Map",
                  "Hcal/DigiMonitor/Digi Depth 3 Occupancy Map",
                  "Hcal/DigiMonitor/Digi Depth 4 Occupancy Map"],

                # 2 hists each from RecHitMonitor, TrigPrim Monitor
                ["Hcal/RecHitMonitor/RecHit Eta Energy Map",
                 "Hcal/RecHitMonitor/RecHit Phi Energy Map",
                 "Hcal/TrigPrimMonitor/TrigPrim Geo Energy Map",
                 "Hcal/TrigPrimMonitor/TP Timing"],

                # DeadCellMonitor, HotCellMonitor
                ["Hcal/DeadCellMonitor/HCAL/HCAL_CoolCell_belowPed",
                 "Hcal/HotCellMonitor/HCAL/HCALHotCellEnergyMapThresh0",
                 "Hcal/HotCellMonitor/HCAL/HCALnadaOccMap"])
