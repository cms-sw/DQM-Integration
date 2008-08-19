def pixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "Pixel_FEDError_Summary",   
  [{ 'path': "Pixel/Endcap/SUMRAW_NErrors_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMRAW_errorType_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/AdditionalPixelErrors/SUMRAW_NErrors_FEDErrors", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/AdditionalPixelErrors/SUMRAW_errorType_FEDErrors", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}])
pixellayout(dqmitems, "Pixel_DIGI_Summary",
  [{ 'path': "Pixel/Endcap/SUMDIG_adc_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMDIG_ndigis_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}])
