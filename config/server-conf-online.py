import os.path, socket
global CONFIGDIR
HOST      = socket.gethostname().lower()
BASEDIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
if HOST.find("-c2d04-") > 0:
  SRVDIR  = '/home/dqmlocal'
  CHOST   = 'srv-c2d05-19'
elif HOST.find("-c2d05-") > 0:
  SRVDIR  = '/home/dqm'
  CHOST   = 'localhost'

LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("castor","csc", "dt", "eb", "ee", "es","hcal", "hcalcalib", "hlt", "hlx", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]
LAYOUTS += ["%s/%s_overview_layouts.py" % (CONFIGDIR, x) for x in
            ("sistrip",)]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("castor","csc", "dt", "eb", "ee", "es","hcal", "hcalcalib", "hlt", "hlx", "l1t", "l1temulator", "rpc", "pixel", "sistrip" , "fed" )]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -t python -pp'
server.serverDir   = '%s/gui' % SRVDIR
server.baseUrl     = '/dqm/online'
server.title       = 'CMS data quality'
server.serviceName = 'Online'

server.plugin('render', BASEDIR + "/style/*.cc")
server.extend('DQMFileAccess', None, "/dqmdata/dqm/uploads",
              { "Original": "/dqmdata/dqm/repository/original",
                "iSpy": "/dqmdata/EventDisplay/done" })
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.source('DQMUnknown', 'unknown')
server.source('DQMOverlay', 'overlay')
server.source('DQMStripChart', 'stripchart')
server.source('DQMLive', 'dqm', '%s:9090' % CHOST)
server.source('DQMArchive', 'file', '%s/ix' % SRVDIR, '^/Global/')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
