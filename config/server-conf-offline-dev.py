import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
 source /data/sw/cmsset_default.sh
 source /data/sw/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 export QUIET_ASSERT=a
"""

server.port        = 8060
server.serverDir   = '/data/dqm/dev/gui'
server.baseUrl     = '/dqm/dev'
server.title       = 'CMS data quality'
server.serviceName = 'CERN Development'

server.source('live', 'DQMLive', '--collector 8061', '--listen 8062')
server.source('file', 'DQMArchive', '/data/dqm/dev/dqm.db', '--listen 8063')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/dev/upload')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-dev.py")
