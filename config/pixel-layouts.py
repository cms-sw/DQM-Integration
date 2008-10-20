def pixellayout(i, p, *rows): i["Pixel/Layouts/" + p] = DQMItem(layout=rows)

pixellayout(dqmitems, "00 - Pixel_RawData_FED_Summary",
  ["Pixel/AdditionalPixelErrors/SUMRAW_NErrors_FEDErrors",
   "Pixel/AdditionalPixelErrors/SUMRAW_errorType_FEDErrors"])
pixellayout(dqmitems, "01 - Pixel_RawData_Summary",
  ["Pixel/Barrel/SUMRAW_NErrors_Barrel",
   "Pixel/Barrel/SUMRAW_errorType_Barrel"],
  ["Pixel/Endcap/SUMRAW_NErrors_Endcap",
   "Pixel/Endcap/SUMRAW_errorType_Endcap"])
pixellayout(dqmitems, "02 - Pixel_Digi_Occupancy",
  ["Pixel/Endcap/endcapOccupancyMap",
   "Pixel/Barrel/barrelOccupancyMap"])
pixellayout(dqmitems, "03 - Pixel_Digi_Summary",
  ["Pixel/Barrel/SUMDIG_adc_Barrel",
   "Pixel/Barrel/SUMDIG_ndigis_Barrel",
   "Pixel/Barrel/SUMDIG_ndigisFREQ_Barrel"],
  ["Pixel/Endcap/SUMDIG_adc_Endcap",
   "Pixel/Endcap/SUMDIG_ndigis_Endcap",
   "Pixel/Endcap/SUMDIG_ndigisFREQ_Endcap"])
pixellayout(dqmitems, "04 - Pixel_Cluster_Summary",
  ["Pixel/Barrel/SUMCLU_charge_Barrel",
   "Pixel/Barrel/SUMCLU_nclusters_Barrel",
   "Pixel/Barrel/SUMCLU_size_Barrel"],
  ["Pixel/Endcap/SUMCLU_charge_Endcap",
   "Pixel/Endcap/SUMCLU_nclusters_Endcap",
   "Pixel/Endcap/SUMCLU_size_Endcap"])
