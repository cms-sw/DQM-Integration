def hcaloverviewlayout(i, p, *rows): i["Collisions/HcalFeedBack/"+p] = DQMItem(layout=rows)


#  HF+/HF- coincidence triggers, also requiring BPTX
hcaloverviewlayout(dqmitems, "01 - HF+,HF- coincidences (with BPTX)",
           [{'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HFweightedtimeDifference",
             'description':"Difference in weighted times between HF+ and HF- for all cells > 3 GeV, where times are weighted by rechit energies"},
            {'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HFenergyDifference",
             'description':"Sum(E_HFplus - E_HFminus)/Sum(E_HFplus+E_HFminus) for all cells > 3 GeV in an HF coincidence trigger"},
            ])

# HF+/HF- coincidence triggers, also requiring !BPTX
hcaloverviewlayout(dqmitems, "02 - HF+,HF- coincidences (without BPTX)",
           [{'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HFnotBPTXweightedtimeDifference",
             'description':"Difference in weighted times between HF+ and HF- for all cells > 3 GeV, where times are weighted by rechit energies"},
            {'path':"Hcal/RecHitMonitor_Hcal/rechit_info/HFnotBPTXenergyDifference",
             'description':"Sum(E_HFplus - E_HFminus)/Sum(E_HFplus+E_HFminus) for all cells > 3 GeV in an HF coincidence trigger (BPTX doesn't fire)"},
            ])

# Digi Shape plots for digis with ADC sum > threshold N
hcaloverviewlayout(dqmitems, "03 - Digi Shapes for Total Digi Signals > N counts",
                   [{'path':"Hcal/DigiMonitor_Hcal/digi_info/HB/HB Digi Shape - over thresh",
                     'description':"Digi shape for all HB digis with sum ADC count > N counts"},
                    {'path':"Hcal/DigiMonitor_Hcal/digi_info/HE/HE Digi Shape - over thresh",
                     'description':"Digi shape for all HE digis with sum ADC count > N counts"}
                    ],
                   [{'path':"Hcal/DigiMonitor_Hcal/digi_info/HF/HF Digi Shape - over thresh",
                     'description':"Digi shape for all HF digis with sum ADC count > N counts"},
                    {'path':"Hcal/DigiMonitor_Hcal/digi_info/HO/HO Digi Shape - over thresh",
                     'description':"Digi shape for all HO digis with sum ADC count > N counts"}
                    ]
                   )

# Lumi plots
hcaloverviewlayout(dqmitems,"04 - Lumi Bunch Crossing Checks",
                   [{'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/BX_allevents",
                     'description':"Bunch Crossing # for all processed events"}],
                   [{'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/BX_goodevents",
                     'description':"BC # for all events with HT_HF+ > 1 GeV, HT_HF- > 1 GeV, avg HF+ & HF- time > 25 ns"}],
                   [{'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/BX_goodevents_notimecut",
                     'description':"BC # for all events with HT_HF+ > 1 GeV, HT_HF- > 1 GeV"}]
                   )


hcaloverviewlayout(dqmitems,"05 - Events Per Lumi Section",
                   [{'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/LS_allevents",
                     'description':"LS # for all processed events"}],
                   [{'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/EventsPerLS",
                     'description':"LS# for all events with HT_HF+ > 1 GeV, HT_HF- > 1 GeV, avg HF+ & HF- time > 25 ns"}],
                   [{'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/EventsPerLS_notimecut",
                     'description':"LS# for all events with HT_HF+ > 1 GeV, HT_HF- > 1 GeV"}]
                   )


hcaloverviewlayout(dqmitems,"06 - Lumi Distributions",
                   [
                   {'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/MinTime_vs_MinHT",
                   'description':"Min (HF+,HF-) time vs energy"},
                   {'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/timeHFplus_vs_timeHFminus",
                   'description':"HF+ vs HF- energy-weighted average time"}
                   ],
                   [
                   {'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/SumHT_plus_minus",
                   'description':"HF+ sum HT vs HF- sum HT"},
                   {'path':"Hcal/RecHitMonitor_Hcal/luminosityplots/SumEnergy_plus_minus",
                   'description':"HF+ vs HF- total energy"}
                   ],
                   )
