def pixellayout(i, p, *rows): i["Pixel/Layouts/" + p] = DQMItem(layout=rows)

pixellayout(dqmitems, "00 - Pixel_Error_Summary",
  [{ 'path': "Pixel/AdditionalPixelErrors/SUMOFF_NErrors_FEDErrors",
     'description': "Mean number of errors per FED crate (not associated with a specific module ID - should be empty!", 
     'draw': { 'withref': "no" }}],
  [{ 'path': "Pixel/Barrel/SUMOFF_NErrors_Barrel",
     'description': "Mean number of errors per barrel module - should be empty!",
     'draw': { 'withref': "no" }}],
  [{ 'path': "Pixel/Endcap/SUMOFF_NErrors_Endcap",
     'description': "Mean number of errors per endcap module - should be empty!",
     'draw': { 'withref': "no" }}]
  )
pixellayout(dqmitems, "01 - Pixel_Digi_Summary",
  [{ 'path': "Pixel/Barrel/SUMOFF_adc_Barrel",
     'description': "Mean digi charge in ADC counts per barrel Ladder",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Barrel/SUMOFF_ndigis_Barrel",
     'description': "Mean number of digis per event per barrel Ladder",
     'draw': { 'withref': "yes" }}],
  [{ 'path': "Pixel/Endcap/SUMOFF_adc_Endcap",
     'description': "Mean digi charge in ADC counts per endcap Blade",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Endcap/SUMOFF_ndigis_Endcap",
     'description': "Mean number of digis per event per endcap Blade",
     'draw': { 'withref': "yes" }}]
  )
pixellayout(dqmitems, "02 - Pixel_Cluster_Summary",
  [{ 'path': "Pixel/Barrel/SUMOFF_charge_Barrel",
     'description': "Mean cluster charge in kilo electrons per barrel Ladder",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Barrel/SUMOFF_nclusters_Barrel",
     'description': "Mean number of clusters per event per barrel Ladder",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Barrel/SUMOFF_size_Barrel",
     'description': "Mean cluster size in number of pixels per barrel Ladder",
     'draw': { 'withref': "yes" }}],
  [{ 'path': "Pixel/Endcap/SUMOFF_charge_Endcap",
     'description': "Mean cluster charge in kilo electrons per endcap Blade",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Endcap/SUMOFF_nclusters_Endcap",
     'description': "Mean number of clusters per event per endcap Blade",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Endcap/SUMOFF_size_Endcap",
     'description': "Mean cluster size in number of pixels per barrel Blade",
     'draw': { 'withref': "yes" }}])
pixellayout(dqmitems, "03 - Pixel_Track_Summary",
  [{ 'path': "Pixel/Clusters/OnTrack/charge_siPixelClusters", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Clusters/OnTrack/size_siPixelClusters", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Clusters/OffTrack/charge_siPixelClusters", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"},
   { 'path': "Pixel/Clusters/OffTrack/size_siPixelClusters", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}],
  [{ 'path': "Pixel/Tracks/ntracks_generalTracks", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiPixel>Description for the Central DQM Shifter</a>"}]
)
pixellayout(dqmitems, "04 - Barrel_Digi_Summary_per_Shell",
  [{ 'path': "Pixel/Barrel/Shell_mI/SUMOFF_adc_Shell_mI", 'description': "Mean digi charge in ADC counts per Barrel Shell_mI module"},
   { 'path': "Pixel/Barrel/Shell_mO/SUMOFF_ndigis_Shell_mO", 'description': "Mean number of digis per event per Barrel Shell_mO module"}],
  [{ 'path': "Pixel/Barrel/Shell_pI/SUMOFF_adc_Shell_pI", 'description': "Mean digi charge in ADC counts per Barrel Shell_pI module"},
   { 'path': "Pixel/Barrel/Shell_pO/SUMOFF_ndigis_Shell_pO", 'description': "Mean number of digis per event per Barrel Shell_pO module"}]
)     
pixellayout(dqmitems, "05 - Endcap_Digi_Summary_per_HalfCylinder",
  [{ 'path': "Pixel/Endcap/HalfCylinder_mI/SUMOFF_adc_HalfCylinder_mI", 'description': "Mean digi charge in ADC counts per Endcap HalfCylinder_mI module"},
   { 'path': "Pixel/Endcap/HalfCylinder_mO/SUMOFF_ndigis_HalfCylinder_mO", 'description': "Mean number of digis per event per Endcap HalfCylinder_mO module"}],
  [{ 'path': "Pixel/Endcap/HalfCylinder_pI/SUMOFF_adc_HalfCylinder_pI", 'description': "Mean digi charge in ADC counts per Endcap HalfCylinder_pI module"},
   { 'path': "Pixel/Endcap/HalfCylinder_pO/SUMOFF_ndigis_HalfCylinder_pO", 'description': "Mean number of digis per event per Endcap HalfCylinder_pO module"}]
)
pixellayout(dqmitems, "06 - Barrel OnTrack cluster positions",
  [{ 'path': "Pixel/Clusters/OnTrack/position_siPixelClusters_Layer_1", 'description': "Global position of OnTrack clusters in Barrel/Layer_1"}],
  [{ 'path': "Pixel/Clusters/OnTrack/position_siPixelClusters_Layer_2", 'description': "Global position of OnTrack clusters in Barrel/Layer_2"}],
  [{ 'path': "Pixel/Clusters/OnTrack/position_siPixelClusters_Layer_3", 'description': "Global position of OnTrack clusters in Barrel/Layer_3"}]
)
pixellayout(dqmitems, "07 - Endcap OnTrack cluster positions",
  [{ 'path': "Pixel/Clusters/OnTrack/position_siPixelClusters_mz_Disk_1", 'description': "Global position of OnTrack clusters in Endcap -z Disk_1"},
   { 'path': "Pixel/Clusters/OnTrack/position_siPixelClusters_mz_Disk_2", 'description': "Global position of OnTrack clusters in Endcap -z Disk_2"}],
  [{ 'path': "Pixel/Clusters/OnTrack/position_siPixelClusters_pz_Disk_1", 'description': "Global position of OnTrack clusters in Endcap +z Disk_1"},
   { 'path': "Pixel/Clusters/OnTrack/position_siPixelClusters_pz_Disk_2", 'description': "Global position of OnTrack clusters in Endcap +z Disk_2"}]
)
