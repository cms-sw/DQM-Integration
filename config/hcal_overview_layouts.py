# Dummy check of python syntax within file when run stand-alone
if __name__=="__main__":
    class DQMItem:
        def __init__(self,layout):
            print layout

    dqmitems={}

def hcaloverviewlayout(i, p, *rows): i["Collisions/HcalFeedBack/"+p] = DQMItem(layout=rows)

#  HF+/HF- coincidence triggers, requiring minbias
hcaloverviewlayout(dqmitems, "01 - HF+,HF- distributions for MinBias",
           [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HFweightedtimeDifference",
             'description':"Difference in weighted times between HF+ and HF- for all cells > threshold, where times are weighted by rechit energies, in events passing BPTX trigger"},
            {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HFenergyDifference",
             'description':"Sum(E_HFplus - E_HFminus)/Sum(E_HFplus+E_HFminus) for all cells > threshold in events passing a BPTX trigger"},
            ])

# HF+/HF- coincidence triggers, also requiring !BPTX
hcaloverviewlayout(dqmitems, "02 - HF+,HF- distributions for Hcal HLT",
           [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedHcalHLTriggers/HF_HcalHLT_weightedtimeDifference",
             'description':"Difference in weighted times between HF+ and HF- for all cells > threshold, where times are weighted by rechit energies, n events failing BPTX but passing an HF coincidence trigger"},
            {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedHcalHLTriggers/HF_HcalHLT_energyDifference",
             'description':"Sum(E_HFplus - E_HFminus)/Sum(E_HFplus+E_HFminus) for all cells > threshold in events passing an HF coincidence trigger ( but BPTX *doesn't* fire)"},
            ])

# HE+/HE- distributions, requiring BPTX
hcaloverviewlayout(dqmitems, "03 - HE+,HE- distributions for MinBias",
                   [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HEweightedtimeDifference",
                     'description':"Difference in weighted times between HE+ and HE- for all cells > threshold, where times are weighted by rechit energies, in events passing BPTX trigger"},
                    {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HEenergyDifference",
                     'description':"Sum(E_HEplus - E_HEminus)/Sum(E_HEplus+E_HEminus) for all cells > threshold in events passing a BPTX trigger"},
                                ])


# Digi Shape plots for digis with ADC sum > threshold N
hcaloverviewlayout(dqmitems, "04 - Digi Shapes for Total Digi Signals > N counts",
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
hcaloverviewlayout(dqmitems,"05 - Lumi Bunch Crossing Checks",
                   [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/BX_allevents",
                     'description':"Bunch Crossing # for all processed events"}],
                   [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/BX_MinBias_Events_notimecut",
                     'description':"BC # for all events with HT_HF+ > 1 GeV, HT_HF- > 1 GeV, passing MinBias HLT trigger"}],
                   [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedHcalHLTriggers/BX_HcalHLT_Events_notimecut",
                     'description':"BC # for all events with HT_HF+ > 1 GeV, HT_HF- > 1 GeV, Hcal HLT trigger passed"}]
                   )


hcaloverviewlayout(dqmitems,"06 - Events Per Lumi Section",
                   [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/AllEventsPerLS",
                     'description':"LS # for all processed events"}],
                   [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/MinBiasEventsPerLS_notimecut",
                     'description':"LS# for all events with HT_HF+ > 1 GeV, HT_HF- > 1 GeV, passed BPTX, |HF+ - HF- | < threshold"}],
                   [{'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedHcalHLTriggers/HcalHLTEventsPerLS_notimecut",
                     'description':"LS# for all events with HT_HF+ > 1 GeV, HT_HF- > 1 GeV, Hcal HLT trigger passed"}]
                   )


hcaloverviewlayout(dqmitems,"07 - Lumi Distributions",
                   [
    {'path':"Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/MinTime_vs_MinSumET",
     'description':"Min (HF+,HF-) time vs energy"},
    {'path':"Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/HFM_Time_vs_SumET",
     'description':"average HF- time vs energy"},
     {'path':"Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/HFP_Time_vs_SumET",
     'description':"average HF+ time vs energy"},
                   ],
                   [
    {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/timeHFplus_vs_timeHFminus",
     'description':"HF+ vs HF- energy-weighted average time for BPTX events"},
    {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/SumHT_plus_minus",
     'description':"HF+ sum HT vs HF- sum HT"},
    {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/SumEnergy_plus_minus",
     'description':"HF+ vs HF- total energy"}
                   ],
                   )


hcaloverviewlayout(dqmitems,"08 - RecHit Average Occupancy",
                   [
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HB HE HF Depth 1 Above Threshold RecHit Occupancy",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HB HE HF Depth 2 Above Threshold RecHit Occupancy",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   ],
                   [
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HE Depth 3 Above Threshold RecHit Occupancy",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HO Depth 4 Above Threshold RecHit Occupancy",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   ],
                   )

hcaloverviewlayout(dqmitems,"09 - RecHit Average Energy",
                   [
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HB HE HF Depth 1 Above Threshold RecHit Average Energy GeV",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HB HE HF Depth 2 Above Threshold RecHit Average Energy GeV",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   ],
                   [
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HE Depth 3 Above Threshold RecHit Average Energy GeV",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HO Depth 4 Above Threshold RecHit Average Energy GeV",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   ],
                   )

hcaloverviewlayout(dqmitems,"10 - RecHit Average Time",
                   [
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HB HE HF Depth 1 Above Threshold RecHit Average Time nS",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HB HE HF Depth 2 Above Threshold RecHit Average Time nS",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   ],
                   [
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HE Depth 3 Above Threshold RecHit Average Time nS",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   {'path':"Hcal/RecHitMonitor_Hcal/Distributions_PassedMinBias/HO Depth 4 Above Threshold RecHit Average Time nS",
                   'description':"occupancy for rechits > threshold in BPTX events"},
                   ],
                   )
