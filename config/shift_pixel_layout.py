def pixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "Pixel_DIGI_Summary",
  ["Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMDIG_adc_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMDIG_ndigis_Panel_2"])
pixellayout(dqmitems, "Pixel_FEDError_Summary",   
  ["Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_NErrors_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_errorType_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_TBMType_Panel_2"],
  ["Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_EvtNbr_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_ROCNmbr_Panel_2"],
  ["Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_ROCId_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_DCOLId_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_PXId_Panel_2"])
