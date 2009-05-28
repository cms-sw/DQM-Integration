def ecalpreshowerlayout(i, p, *rows): i["EcalPreshower/Layouts/" + p] = DQMItem(layout=rows)
def esshifterlayout(i, p, *rows): i["EcalPreshower/00 Shift/" + p] = DQMItem(layout=rows)

# Quick Collections
ecalpreshowerlayout(dqmitems, "01-IntegritySummary-EcalPreshower",
  [{ 'path': "EcalPreshower/ESIntegrityClient/ES Integrity Summary 1 Z 1 P 1", 'description': "ES+ Front Integrity Summary 1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/PreshowerWikiHome>PreshowerDQM</a>" },
   { 'path': "EcalPreshower/ESIntegrityClient/ES Integrity Summary 1 Z 1 P 2", 'description': "ES+ Rear Integrity Summary 1 - <a href==https://twiki.cern.ch/twiki/bin/view/CMS/PreshowerWikiHome>PreshowerDQM</a>" }])

esshifterlayout(dqmitems, "01-IntegritySummary",
  [{ 'path': "EcalPreshower/ESIntegrityClient/ES Integrity Summary 1 Z 1 P 1", 'description': "ES+ Front Integrity Summary 1 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/PreshowerWikiHome>PreshowerDQM</a>" },
   { 'path': "EcalPreshower/ESIntegrityClient/ES Integrity Summary 1 Z 1 P 2", 'description': "ES+ Rear Integrity Summary 1 - <a href==https://twiki.cern.ch/twiki/bin/view/CMS/PreshowerWikiHome>PreshowerDQM</a>" }])

