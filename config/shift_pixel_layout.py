def shiftpixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
shiftpixellayout(dqmitems, "01 - Total number of errors per FED channel",
  [{ 'path': "Pixel/AdditionalPixelErrors/FedChNErrArray", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#01>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "02 - Digi charge Barrel",
  [{ 'path': "Pixel/Barrel/ALLMODS_adcCOMB_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#02>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "03 - Digi charge Endcap",
  [{ 'path': "Pixel/Endcap/ALLMODS_adcCOMB_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#03>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "04 - Mean digi charge Barrel",
  [{ 'path': "Pixel/Barrel/SUMDIG_adc_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#04>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "05 - Mean digi charge Endcap",
  [{ 'path': "Pixel/Endcap/SUMDIG_adc_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#05>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "06 - Digi occupancy Barrel",
  [{ 'path': "Pixel/Barrel/SUMDIG_ndigisFREQ_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#06>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "07 - Digi occupancy Endcap",
  [{ 'path': "Pixel/Endcap/SUMDIG_ndigisFREQ_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#07>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "08 - Cluster charge Barrel",
  [{ 'path': "Pixel/Barrel/ALLMODS_chargeCOMB_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#08>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "09 - Cluster charge Endcap",
  [{ 'path': "Pixel/Endcap/ALLMODS_chargeCOMB_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#09>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "10 - Mean cluster charge Barrel",
  [{ 'path': "Pixel/Barrel/SUMCLU_charge_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#10>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "11 - Mean cluster charge Endcap",
  [{ 'path': "Pixel/Endcap/SUMCLU_charge_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#11>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "12 - Events with many digis",
  [{ 'path': "Pixel/bigEventRate", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#12>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "13 - Events with many FPIX clusters",
  [{ 'path': "Pixel/bigFpixClusterEventRate", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel#13>Description for the Central DQM Shifter</a>"}]
)
