def l1toverviewlayout(i, p, *rows): i["Collisions/L1TFeedBack/" + p] = DQMItem(layout=rows)

l1toverviewlayout(dqmitems,"00 Rate BSCL.BSCR",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/TechnicalRates/Rate_TechBit_040", 'description': "Rate BSCL.BSCR. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

l1toverviewlayout(dqmitems,"01 Rate BSC splash right",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/TechnicalRates/Rate_TechBit_042", 'description': "Rate BSC splash right. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

l1toverviewlayout(dqmitems,"02 Rate BSC splash left",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/TechnicalRates/Rate_TechBit_043", 'description': "Rate BSC splash left. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

l1toverviewlayout(dqmitems,"03 Integ BSCL*BSCR Triggers vs LS",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/TechnicalRates/Integral_TechBit_040", 'description': "Integrated BSCL*BSCR Triggers vs LS. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

l1toverviewlayout(dqmitems,"04 Integ BSCL or BSCR Triggers vs LS",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/TechnicalRates/Integral_TechBit_042_OR_043", 'description': "Integrated BSCL or BSCR Triggers vs LS. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

l1toverviewlayout(dqmitems,"05 Integ HF Triggers vs LS",
  	[{'path': "L1T/L1TScalersSCAL/Level1TriggerRates/TechnicalRates/Integral_TechBit_009", 'description': "Integrated HF Triggers vs LS. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

