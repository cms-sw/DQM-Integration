def pixellayout(i, p, *rows): i["Layouts/Pixel Layouts/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "Pixel_Digi_Toplevel_Summary",
  ["Pixel/Barrel/SUMDIG_adc_Barrel",
   "Pixel/Barrel/SUMDIG_ndigis_Barrel"],
  ["Pixel/Endcap/SUMDIG_adc_Endcap",
   "Pixel/Endcap/SUMDIG_ndigis_Endcap"])
pixellayout(dqmitems, "Pixel_PIB_Summary",
  ["Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_errorType_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_NErrors_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_TBMType_Panel_2"],
  ["Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_EvtNbr_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_ROCId_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_DCOLId_Panel_2"],
  ["Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_PXId_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_ROCNmbr_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMRAW_TBMMessage_Panel_2"],
  ["Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMDIG_adc_Panel_2",
   "Pixel/Endcap/HalfCylinder_pO/Disk_1/Blade_09/Panel_2/SUMDIG_ndigis_Panel_2"])
