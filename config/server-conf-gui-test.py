import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("castor","csc", "dt", "eb", "ee", "es","hcal", "hlt", "hlx", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("castor","csc", "dt", "eb", "ee", "es","hcal", "hlt", "hlx", "l1t", "l1temulator", "rpc", "pixel", "sistrip" , "fed" )]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
server.serverDir   = '/home/dqm/gui'
server.baseUrl     = '/dqm/gui-test'
server.title       = 'CMS data quality'
server.serviceName = 'GUI test'

server.plugin('render', BASEDIR + "/style/*.cc")
server.extend('DQMFileAccess', None, None,
	      { "dqm": "/dqmdata/dqm/merged",
	        "ispy": "/dqmdata/EventDisplay/dropbox/000" })
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
#server.extend('EVDSnapshotUpload', '/home/dqm/iguana-snapshots')
#server.source('EVDSnapshot', 'evd', '/home/dqm/iguana-snapshots')
server.source('DQMUnknown', 'unknown')
server.source('DQMOverlay', 'overlay')
server.source('DQMStripChart', 'stripchart')
server.source('DQMLive', 'dqm', 'localhost:9090')
server.source('DQMArchive', 'file', '/home/dqm/idx', '^/Global/')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
