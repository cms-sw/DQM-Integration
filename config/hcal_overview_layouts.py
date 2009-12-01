def hcaloverviewlayout(i, p, *rows): i["Collisions/Hcal/"+p] = DQMItem(layout=rows)

hcaloverviewlayout(dqmitems, "01 - Hcal Parameters",
           // HF plots
           [{'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HFweightedtimeDifference",
             'description':"Difference in weighted times between HF+ and HF-, where times are weighted by rechit energies"},
            {'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HFtimeDifference",
             'description':"Difference in average times between HF+ and HF-"},
            {'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HFenergyDifference",
             'description':"Sum(E_HFplus - E_HFminus)/Sum(E_HFplus+E_HFminus)"},
            {'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HFaverageenergyDifference",
             'description':"Difference in average energies between HF+ and HF-"}
            ],
           // HE plots
           [{'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HEweightedtimeDifference",
             'description':"Difference in weighted times between HE+ and HE-, where times are weighted by rechit energies"},
            {'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HEtimeDifference",
             'description':"Difference in average times between HE+ and HE-"},
            {'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HEenergyDifference",
             'description':"Sum(E_HEplus - E_HEminus)/Sum(E_HEplus+E_HEminus)"},
            {'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HEaverageenergyDifference",
             'description':"Difference in average energies between HE+ and HE-"}
            ]
                   )

hcaloverviewlayout( dqmitems, "TEST",
                    [{ 'path':"Hcal/EventInfo/reportSummaryMap",
                       'description':"This shows the fraction of bad cells in each subdetector.  All subdetectors should appear green.  Values should all be above 98%."}]
                    )
