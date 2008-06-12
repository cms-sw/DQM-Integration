import os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("csc", "dt", "eb", "hcal", "l1t", "pixel", "rpc", "sistrip")]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("csc", "dt", "eb", "hcal", "l1t", "pixel", "sistrip")]

modules = ("GuiDQM",)
envsetup = """
 source /home/dqm/rpms/cmsset_default.sh
 source /home/dqm/rpms/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 source /home/dqm/rpms/slc4_ia32_gcc345/external/py2-pil/1.1.6/etc/profile.d/init.sh
 source /home/dqm/rpms/slc4_ia32_gcc345/external/libpng/1.2.10/etc/profile.d/init.sh
 source /home/dqm/rpms/slc4_ia32_gcc345/external/libjpg/6b/etc/profile.d/init.sh
 source /home/dqm/rpms/slc4_ia32_gcc345/external/libtiff/3.8.2/etc/profile.d/init.sh
 export QUIET_ASSERT=a
"""

server.serverDir   = '/home/dqm/gui'
server.baseUrl     = '/dqm/online-playback'
server.title       = 'CMS data quality'
server.serviceName = 'Online Playback'

server.source('dqm', 'DQMLive', '--listen 9091', '--collector localhost:9090')
server.source('file', 'DQMArchive', '/home/dqm/dqm.db', '--listen 9097')
server.source('layouts', 'DQMLayout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
