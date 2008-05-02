import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

modules = ("GuiDQM",)
envsetup = """
 source /data/sw/cmsset_default.sh
 source /data/sw/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 export QUIET_ASSERT=a
"""

server.port        = 8030
server.serverDir   = '/data/dqm/tier-0/gui'
server.baseUrl     = '/dqm/tier-0'
server.title       = 'CMS data quality'
server.serviceName = 'CERN Tier-0'

server.source('file', 'DQMArchive', '/data/dqm/tier-0/dqm.db', '--listen 8031')
server.extend('DQMFileAccess', '/dev/null', '/data/dqm/tier-0/upload')

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-tier-0.py")
