import os.path
global CONFIGDIR
BASEDIR   = os.path.dirname(os.path.dirname(__file__))
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

#LAYOUTS = ["%s/shift_%s-layout.py" % (CONFIGDIR, x) for x in
LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in
           ("castor","eb", "ee","es", "csc", "rpc", "hcal", "hcalcalib", "hlt","l1t", "l1temulator", "pixel", "sistrip", "dt", "muons", "jetmet", "egamma")]
LAYOUTS += ["%s/%s_overview_layouts.py" % (CONFIGDIR, x) for x in
            ("sistrip","ecal","hcal","beammonitor","l1t","hlt")]
#LAYOUTS += ["%s/%s_-layouts.py" % (CONFIGDIR, x) for x in
LAYOUTS += ["%s/%s_T0_layouts.py" % (CONFIGDIR, x) for x in
           ("castor","pixel","sistrip","hcal", "hcalcalib", "eb", "ee","es", "rpc")]
LAYOUTS += ["%s/%s_caf_layouts.py" % (CONFIGDIR, x) for x in
           ("tkal",)]
LAYOUTS += [CONFIGDIR + "/shift_hlt_relval_layout.py"]
LAYOUTS += [CONFIGDIR + "/hlt_relval-layouts.py"]

modules = ("GuiDQM",)
envsetup = "export QUIET_ASSERT=a"

#server.instrument  = 'valgrind --num-callers=999 `cmsvgsupp` --error-limit=no'
#server.instrument  = 'valgrind --tool=helgrind --num-callers=999 --error-limit=no'
#server.instrument  = 'igprof -d -t python -pp'
#server.instrument  = 'igprof -d -t python -mp'
server.port        = 8070
server.serverDir   = '/data/dqm/dqmtest/gui'
server.baseUrl     = '/dqm/testing'
server.title       = 'CMS data quality'
server.serviceName = 'Test'

server.plugin('render', "/data/dqm/dqmtest/style/*.cc")
server.extend('DQMRenderLink', server.pathOfPlugin('render'))
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/dqmtest/uploads',
	      { 'ROOT': '/data/dqm/dqmtest/repository/data',
	        'ZIP': '/data/dqm/dqmtest/repository/zipped' })
server.source('DQMUnknown')
server.source('DQMOverlay')
server.source('DQMStripChart')
server.source('DQMArchive', '/data/dqm/dqmtest/ix', '^/Global/')
server.source('DQMLayout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
