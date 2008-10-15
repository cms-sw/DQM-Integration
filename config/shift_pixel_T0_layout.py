def pixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "00 - Pixel_FEDError_Summary",   
  [{ 'path': "Pixel/Barrel/SUMRAW_NErrors_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Barrel/SUMRAW_errorType_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Endcap/SUMRAW_NErrors_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMRAW_errorType_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/AdditionalPixelErrors/SUMRAW_NErrors_FEDErrors", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/AdditionalPixelErrors/SUMRAW_errorType_FEDErrors", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}])
pixellayout(dqmitems, "01 - Pixel_Occupancy",
  [{ 'path': "Pixel/Barrel/barrelOccupancyMap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Endcap/endcapOccupancyMap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}])
pixellayout(dqmitems, "02 - Pixel_DIGI_Summary",
  [{ 'path': "Pixel/Barrel/SUMDIG_adc_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Barrel/SUMDIG_ndigis_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Barrel/SUMDIG_ndigisFREQ_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Endcap/SUMDIG_adc_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMDIG_ndigis_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMDIG_ndigisFREQ_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}])
