def shiftdtlayout(i, p, *rows): i["Shift/DT/" + p] = DQMItem(layout=rows)

shiftdtlayout(dqmitems, "01-DataIntegrity",
  ["DT/DataIntegrity/FED770/FED770_ROSSummary",
   "DT/DataIntegrity/FED771/FED771_ROSSummary",
   "DT/DataIntegrity/FED772/FED772_ROSSummary"],
  ["DT/DataIntegrity/FED773/FED773_ROSSummary",
   "DT/DataIntegrity/FED774/FED774_ROSSummary"])

shiftdtlayout(dqmitems, "02-CorrelatedTriggers",
  ["DT/Tests/DTLocalTrigger/Wheel-2/LocalTriggerPhi/CorrFraction_Phi_W-2",
   "DT/Tests/DTLocalTrigger/Wheel-1/LocalTriggerPhi/CorrFraction_Phi_W-1",
   "DT/Tests/DTLocalTrigger/Wheel0/LocalTriggerPhi/CorrFraction_Phi_W0"],
  ["DT/Tests/DTLocalTrigger/Wheel1/LocalTriggerPhi/CorrFraction_Phi_W1",
   "DT/Tests/DTLocalTrigger/Wheel2/LocalTriggerPhi/CorrFraction_Phi_W2"])
