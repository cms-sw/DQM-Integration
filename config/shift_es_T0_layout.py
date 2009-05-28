def shifteslayout(i, p, *rows): i["00 Shift/EcalPreshower/" + p] = DQMItem(layout=rows)

shifteslayout(dqmitems, "01-IntegritySummary",
  [{ 'path': "EcalPreshower/ESIntegrityClient/ES Integrity Summary 1 Z 1 P 1", 'description': "ES+ Front Integrity Summary 1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/PreshowerWikiHome>PreshowerDQM</a>" },
   { 'path': "EcalPreshower/ESIntegrityClient/ES Integrity Summary 1 Z 1 P 2", 'description': "ES+ Rear Integrity Summary 1 - <a href==https://twiki.cern.ch/twiki/bin/view/CMS/PreshowerWikiHome>PreshowerDQM</a>" }])

