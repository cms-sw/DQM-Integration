server.workspace('DQMQuality', 0, 'Summaries', 'Summary')
server.workspace('DQMSummary', 1, 'Summaries', 'Reports')
server.workspace('DQMShift',   2, 'Summaries', 'Shift')
server.workspace('DQMContent', 3, 'Summaries', 'Everything', '^')

server.workspace('DQMContent', 20, 'Calorimeter', 'HCAL', '^Hcal/',
                 'Hcal/Layouts/HCAL Digi Problems',
                 'Hcal/Layouts/HCAL Dead Cell Check',
                 'Hcal/Layouts/HCAL Hot Cell Check',
                 'Hcal/Layouts/HCAL Data Format',
                 "Hcal/Layouts/01 HCAL Shifter Checklist Plots - Summaries",
                 )
