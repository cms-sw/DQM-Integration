import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/%s_caf_layouts.py" % (CONFIGDIR, x) for x in
	   ("tkal",)]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

server.port        = 8040
server.serverDir   = '/data/dqm/caf/gui'
server.baseUrl     = '/dqm/caf'
server.title       = 'CMS data quality'
server.serviceName = 'CERN CAF'

server.plugin('render', BASEDIR + "/style/*.cc")
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/caf/uploads',
              { 'CAF': '/data/dqm/caf/repository/data'})
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')
server.source('DQMArchive', '/data/dqm/caf/ix', '^/Global/')
server.source('DQMLayout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-caf.py")
