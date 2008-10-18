import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

#LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in ("sistrip")]
LAYOUTS = ["%s/shift_%s_T0_layout.py" % (CONFIGDIR, x) for x in ("eb", "ee", "hcal", "sistrip", "pixel", "l1t", "l1temulator", "hlt", "dt", "muons", "egamma", "jetmet")]

modules = ("GuiDQM",)
envsetup = """
  export YUI_ROOT=/data/sw/$SCRAM_ARCH/external/yui/2.4.1
  export QUIET_ASSERT=a
"""

server.port        = 8060
server.serverDir   = '/data/dqm/dev/gui'
server.baseUrl     = '/dqm/dev'
server.title       = 'CMS data quality'
server.serviceName = 'CERN Development'

server.source('DQMLive', 'live', '--collector localhost:8061', '--listen 8062')
server.source('DQMArchive', 'file', '/data/dqm/dev/dqm.db', '--listen 8063')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/dev/upload')

server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-dev.py")
