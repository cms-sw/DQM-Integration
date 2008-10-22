def pixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "00 - Pixel_DIGI_Summary",
  [{ 'path': "Pixel/Barrel/SUMOFF_adc_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Barrel/SUMOFF_ndigis_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Endcap/SUMOFF_adc_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMOFF_ndigis_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}])
pixellayout(dqmitems, "01 - Pixel_CLUSTER_Summary",
  [{ 'path': "Pixel/Barrel/SUMOFF_charge_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Barrel/SUMOFF_nclusters_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Barrel/SUMOFF_size_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Endcap/SUMOFF_charge_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMOFF_nclusters_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMOFF_size_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}])
pixellayout(dqmitems, "02 - Pixel_RECHIT_Summary",
  [{ 'path': "Pixel/Barrel/SUMOFF_ClustX_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Barrel/SUMOFF_ClustY_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Endcap/SUMOFF_ClustX_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Endcap/SUMOFF_ClustY_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiPixel>Description for the Central DQM Shifter</a>"}])
