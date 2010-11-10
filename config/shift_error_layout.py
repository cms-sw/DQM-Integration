def errorlayout(i, p, *rows): i["00 Shift/Errors/" + p] = DQMItem(layout=rows)

errorlayout(dqmitems, "00 - HCal Warning Plots",
 [{ 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HCAL_vs_LS",
    'description': "This plots represents the number of HCAL dead Cells as a function of the LumiSection. The shift leader must be immediately informed if this number is greater than 50.", 'draw': { 'withref': "no" }}])


