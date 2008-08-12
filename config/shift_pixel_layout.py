def pixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "Pixel_FEDError_Summary",   
  ["Pixel/Endcap/SUMRAW_NErrors_Endcap",
   "Pixel/Endcap/SUMRAW_errorType_Endcap"])
pixellayout(dqmitems, "Pixel_DIGI_Summary",
  ["Pixel/Endcap/SUMDIG_adc_Endcap",
   "Pixel/Endcap/SUMDIG_ndigis_Endcap"])
pixellayout(dqmitems, "Pixel_CLUSTER_Summary",
  ["Pixel/Endcap/SUMCLU_charge_Endcap",
   "Pixel/Endcap/SUMCLU_nclusters_Endcap",
   "Pixel/Endcap/SUMCLU_size_Endcap"])
