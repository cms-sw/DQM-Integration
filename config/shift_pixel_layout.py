def shiftpixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
shiftpixellayout(dqmitems, "00 - Mean number of FED errors per FED",
  [{ 'path': "Pixel/AdditionalPixelErrors/SUMRAW_NErrors_FEDErrors", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "01 - Mean number of FED errors Barrel",
  [{ 'path': "Pixel/Barrel/SUMRAW_NErrors_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "02 - Mean number of FED errors Endcap",
  [{ 'path': "Pixel/Endcap/SUMRAW_NErrors_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "03 - Mean digi charge Barrel",
  [{ 'path': "Pixel/Barrel/SUMDIG_adc_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "04 - Mean digi occupancy Barrel",
  [{ 'path': "Pixel/Barrel/SUMDIG_ndigis_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "05 - Mean digi charge Endcap",
  [{ 'path': "Pixel/Endcap/SUMDIG_adc_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "06 - Mean digi occupancy Endcap",
  [{ 'path': "Pixel/Endcap/SUMDIG_ndigis_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "07 - Mean cluster charge Barrel",
  [{ 'path': "Pixel/Barrel/SUMCLU_charge_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "08 - Mean cluster charge Endcap",
  [{ 'path': "Pixel/Endcap/SUMCLU_charge_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}]
)
