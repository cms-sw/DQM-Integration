import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in
           ("castor","eb", "ee", "csc", "rpc", "hcal", "l1t", "l1temulator", "hlt", "pixel", "sistrip", "dt", "muons", "jetmet", "egamma")]
LAYOUTS += ["%s/%s_T0_layouts.py" % (CONFIGDIR, x) for x in
           ("castor","pixel","sistrip","hcal", "eb", "ee", "hltmuon")]
LAYOUTS += [CONFIGDIR + "/shift_hlt_relval_layout.py"]
LAYOUTS += [CONFIGDIR + "/hlt_relval-layouts.py"]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

server.port        = 8080
server.serverDir   = '/data/dqm/offline/gui'
server.baseUrl     = '/dqm/offline'
server.title       = 'CMS data quality'
server.serviceName = 'Offline'

server.plugin('render', BASEDIR + "/style/*.cc")
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/offline/uploads',
	      { 'ROOT': '/data/dqm/offline/repository/data',
	        'ZIP': '/data/dqm/offline/repository/zipped',
	        'iSpy':   '/data/ispy-files' })
server.source('DQMUnknown', 'unknown')
server.source('DQMOverlay', 'overlay')
server.source('DQMStripChart', 'stripchart')
server.source('DQMArchive', 'file', '/data/dqm/offline/ix', '^/Global/')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
