def pixellayout(i, p, *rows): i["Pixel/Layouts/" + p] = DQMItem(layout=rows)

pixellayout(dqmitems, "Pixel_RawData_FED_Summary",
  ["Pixel/AdditionalPixelErrors/SUMRAW_NErrors_FEDErrors",
   "Pixel/AdditionalPixelErrors/SUMRAW_errorType_FEDErrors"])
pixellayout(dqmitems, "Pixel_RawData_Toplevel_Summary",
  ["Pixel/Endcap/SUMRAW_NErrors_Endcap",
   "Pixel/Endcap/SUMRAW_errorType_Endcap"],
  ["Pixel/Endcap/HalfCylinder_mI/SUMRAW_NErrors_HalfCylinder_mI",
   "Pixel/Endcap/HalfCylinder_mI/SUMRAW_errorType_HalfCylinder_mI"],
  ["Pixel/Endcap/HalfCylinder_mO/SUMRAW_NErrors_HalfCylinder_mO",
   "Pixel/Endcap/HalfCylinder_mO/SUMRAW_errorType_HalfCylinder_mO"],
  ["Pixel/Endcap/HalfCylinder_pI/SUMRAW_NErrors_HalfCylinder_pI",
   "Pixel/Endcap/HalfCylinder_pI/SUMRAW_errorType_HalfCylinder_pI"],
  ["Pixel/Endcap/HalfCylinder_pO/SUMRAW_NErrors_HalfCylinder_pO",
   "Pixel/Endcap/HalfCylinder_pO/SUMRAW_errorType_HalfCylinder_pO"])
pixellayout(dqmitems, "Pixel_Digi_Toplevel_Summary",
  ["Pixel/Endcap/SUMDIG_adc_Endcap",
   "Pixel/Endcap/SUMDIG_ndigis_Endcap"],
  ["Pixel/Endcap/HalfCylinder_mI/SUMDIG_adc_HalfCylinder_mI",
   "Pixel/Endcap/HalfCylinder_mI/SUMDIG_ndigis_HalfCylinder_mI"],
  ["Pixel/Endcap/HalfCylinder_mO/SUMDIG_adc_HalfCylinder_mO",
   "Pixel/Endcap/HalfCylinder_mO/SUMDIG_ndigis_HalfCylinder_mO"],
  ["Pixel/Endcap/HalfCylinder_pI/SUMDIG_adc_HalfCylinder_pI",
   "Pixel/Endcap/HalfCylinder_pI/SUMDIG_ndigis_HalfCylinder_pI"],
  ["Pixel/Endcap/HalfCylinder_pO/SUMDIG_adc_HalfCylinder_pO",
   "Pixel/Endcap/HalfCylinder_pO/SUMDIG_ndigis_HalfCylinder_pO"])
pixellayout(dqmitems, "Pixel_Digi_Occupancy_Summary",
  ["Pixel/Endcap/endcapOccupancyMap",
   "Pixel/Barrel/barrelOccupancyMap"])
