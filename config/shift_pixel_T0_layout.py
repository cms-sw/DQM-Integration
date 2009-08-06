def shiftpixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
shiftpixellayout(dqmitems, "00 - Mean number of FED errors per Pixel FED Crate",
  [{ 'path': "Pixel/AdditionalPixelErrors/SUMOFF_NErrors_FEDErrors", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "01 - Mean number of FED errors per Pixel Barrel Ladder",
  [{ 'path': "Pixel/Barrel/SUMOFF_NErrors_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "02 - Mean number of FED errors per Pixel Endcap Blade",
  [{ 'path': "Pixel/Endcap/SUMOFF_NErrors_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "03 - Mean digi charge per Barrel Ladder",
  [{ 'path': "Pixel/Barrel/SUMOFF_adc_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "04 - Mean digi occupancy per Barrel Ladder",
  [{ 'path': "Pixel/Barrel/SUMOFF_ndigis_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "05 - Mean digi charge per Endcap Blade",
  [{ 'path': "Pixel/Endcap/SUMOFF_adc_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "06 - Mean digi occupancy per Endcap Blade",
  [{ 'path': "Pixel/Barrel/SUMOFF_ndigis_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "07 - Charge distribution for all Barrel clusters on tracks",
  [{ 'path': "Pixel/Clusters/OnTrack/charge_siPixelClusters_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "08 - Charge distribution for all Endcap clusters on tracks",
  [{ 'path': "Pixel/Clusters/OnTrack/charge_siPixelClusters_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "09 - Charge distribution for all Barrel clusters off tracks",
  [{ 'path': "Pixel/Clusters/OffTrack/charge_siPixelClusters_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "10 - Charge distribution for all Endcap clusters off tracks",
  [{ 'path': "Pixel/Clusters/OffTrack/charge_siPixelClusters_Endcap", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
shiftpixellayout(dqmitems, "11 - Pixel track counters",
  [{ 'path': "Pixel/Tracks/ntracks_rsWithMaterialTracksP5", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
