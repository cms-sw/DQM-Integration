import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("csc", "eb", "ecal", "ee", "hcal", "rpc")]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("eb", "hcal")]
# LAYOUTS = ("%s/%s-layouts.py" % (CONFIGDIR, x) for x in
# 	   ("csc", "dt", "eb", "ecal", "ee", "hcal", "l1temulator", "l1t",
# 	    "pixel", "rpc", "strip"))

modules = ("GuiDQM",)
envsetup = """
 source /home/dqm/rpms/cmsset_default.sh
 source /home/dqm/rpms/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 export QUIET_ASSERT=a
"""

server.serverDir   = '/home/dqm/gui'
server.baseUrl     = '/dqm/gui-test'
server.title       = 'CMS data quality'
server.serviceName = 'GUI test'

server.source('dqm', 'DQMLive', '--listen 9091', '--collector localhost:9090')
server.source('file', 'DQMArchive', '/home/dqm/dqm.db', '--listen 9097')
server.source('layouts', 'DQMLayout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/online-workspaces.py")
