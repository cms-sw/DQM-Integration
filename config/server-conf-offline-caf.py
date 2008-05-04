import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
 source /data/sw/cmsset_default.sh
 source /data/sw/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 export QUIET_ASSERT=a
"""

server.port        = 8040
server.serverDir   = '/data/dqm/caf/gui'
server.baseUrl     = '/dqm/caf'
server.title       = 'CMS data quality'
server.serviceName = 'CERN CAF'

server.source('file', 'DQMArchive', '/data/dqm/caf/dqm.db', '--listen 8041')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/caf/upload')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-caf.py")
