# Dummy check of python syntax within file when run stand-alone
if __name__=="__main__":
    class DQMItem:
        def __init__(self,layout):
            print layout

    dqmitems={}


def shifthcallayout(i, p, *rows): i["00 Shift/Hcal/" + p] = DQMItem(layout=rows)

# Report Summary Map
shifthcallayout(dqmitems, "01 Hcal Report Summary",
                [{'path':"Hcal/EventInfo/reportSummaryMap",
                  'description':  "Shows average fraction of good cells per event in each Hcal subdetector (HB/HE/HO/HF/HO0/HO12/HFLumi).  Values should be greater than 0.98 for HB, HE, and HF.  There are known dead cells in HO, so the HO/HO0/HO12 values will usually be lower than those of the other subdetectors.  The HO0 value should still be > 0.95.  The summary map is fed by the results from the other plots on this page, so when a value is less than expected, you can use the other tests to determine the type of failure."}]
                )

shifthcallayout(dqmitems, "02 HCAL Raw Data",
                [{ 'path': "Hcal/RawDataMonitor_Hcal/ ProblemRawData",
                   'description': "A Raw Data error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad channels over all 4 depths in HCAL. The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "03 HCAL Digi Problems",
                [{ 'path': "Hcal/DigiMonitor_Hcal/ ProblemDigis",
                   'description': "This plot shows the results of checks on the HCAL digis  ('digis' are digitized signals produced from the raw data.)  A digi is considered bad if the capid rotation for that digi was incorrect, if the digi's data valid/error flags are incorrect, or if there is an IDLE-BCN mismatch.  This plot is the sum of bad digis over all depths. Known bad cells appear in black, while new problems appear in yellow, orange, or red.  (Entries in green can still be considered okay, but should be tracked in case they move into the yellow or orange range.)  The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/DigiMonitor_Hcal/bad_digis/1D_digi_plots/BadDigisVsLB",
                   'description': "Total number of bad digis found in HCAL vs luminosity section.  This keeps a running tally of the number of bad digis versus luminosity section.  Sudden jumps in the number of bad digis may indicate that a new problem has appeared during a run."}],
                )

shifthcallayout(dqmitems, "04 HCAL Dead Cell Check",
                [{ 'path': "Hcal/DeadCellMonitor_Hcal/ ProblemDeadCells",
                   'description': "Potential dead cell candidates in all depths. Known problems appear in black, while new dead cells appear in yellow, orange, or red. (Occasional 'green' entries are okay, but should be watched in case they increase into the yellow or orange range.)  Binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41).  More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HCAL_vs_LS",
                   'description': "Total number of dead cells found in HCAL vs luminosity section.  Sudden jumps in the number of dead cells may indicate a channel dying in the middle of a run"}],
                )

shifthcallayout(dqmitems, "05 HCAL Hot Cell Check",
                [{ 'path': "Hcal/HotCellMonitor_Hcal/ ProblemHotCells",
                   'description': "A cell is considered potentially hot if it is above some threshold energy in some fraction of events, or if it is persistently above some (lower) threshold enery for a number of consecutive events. Seriously hot if hot for >5% of a full run. Known problems appear in black, while new problems will appear in red, orange, or yellow.  Occasional green entries are okay.  Histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/HotCellMonitor_Hcal/TotalHotCells_HCAL_vs_LS",
                   'description': "Total number of hot cells found in HCAL vs luminosity section.  Sudden jumps in the number of hot cells may indicate a problem that has occurred in the middle of a run."}],
                )

shifthcallayout(dqmitems, "06 HCAL Trigger Primitives",
                [{ 'path': "Hcal/TrigPrimMonitor_Hcal/ ProblemTriggerPrimitives",
                   'description': "See details at: <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "07 HCAL Lumi Problems",
                [{'path': "Hcal/BeamMonitor_Hcal/ Problem BeamMonitor",
                  'description':"This shows problems only in the sections of HF used for luminosity monitoring.  Channels that are hot or dead are considered as problems, where the definitions of 'hot' and 'dead' are slightly different than in the normal HCAL monitors.  More details at  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "08 HCAL RecHit Energies",
                [{'path': "Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/rechit_1D_plots/HB_energy_1D",
                  'description':"Average energy/hit for each of the 2592 channels in HB"},
                 
                 {'path': "Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/rechit_1D_plots/HE_energy_1D",
                  'description':"Average energy/hit for each of the 2592 channels in HE"}],
                [{'path': "Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/rechit_1D_plots/HF_energy_1D",
                  'description':"Average energy/hit for each of the 1728 channels in HF"},
                 {'path': "Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/rechit_1D_plots/HO_energy_1D",
                  'description':"Average energy/hit for each of the 2160 channels in HO.  (You may see fewer entries than 2160 because of ~30 known dead cells in HO.)"}]
                )
