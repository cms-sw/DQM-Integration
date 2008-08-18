def pixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "Pixel_FEDError_Summary",   
  ["Pixel/Endcap/SUMRAW_NErrors_Endcap",
   "Pixel/Endcap/SUMRAW_errorType_Endcap"],
  ["Pixel/AdditionalPixelErrors/SUMRAW_NErrors_FEDErrors",
   "Pixel/AdditionalPixelErrors/SUMRAW_errorType_FEDErrors"])
pixellayout(dqmitems, "Pixel_DIGI_Summary",
  ["Pixel/Endcap/SUMDIG_adc_Endcap",
   "Pixel/Endcap/SUMDIG_ndigis_Endcap"])
