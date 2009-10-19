import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in
           ("eb", "ee", "csc", "rpc", "hcal", "hlt","l1t", "l1temulator", "pixel", "sistrip", "dt", "muons", "jetmet", "egamma")]
LAYOUTS += ["%s/%s_T0_layouts.py" % (CONFIGDIR, x) for x in
           ("pixel","sistrip","hcal", "eb", "ee")]
LAYOUTS += [CONFIGDIR + "/shift_hlt_relval_layout.py"]
LAYOUTS += [CONFIGDIR + "/hlt_relval-layouts.py"]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

server.port        = 8070
server.serverDir   = '/data/dqm/dqmtest/gui'
server.baseUrl     = '/dqm/testing'
server.title       = 'CMS data quality'
server.serviceName = 'DQM Testing'

server.plugin('render', "/data/dqm/dqmtest/style/*.cc")
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/dqmtest/data',
	      { 'Current_Offline': '/data/dqm/offline/data',
	        'Test_1': '/data/dqm/dqmtest/datatest1',
	        'Test_2': '/data/dqm/dqmtest/datatest2' })
server.source('DQMUnknown', 'unknown', 8071)
server.source('DQMArchive', 'file', '/data/dqm/dqmtest/idx', '^/Global/', '--listen 8071',
              '--load ' + server.pathOfPlugin('render'))
	      
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
