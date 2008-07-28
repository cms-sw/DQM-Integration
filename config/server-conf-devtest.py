import pwd, os, os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("csc", "dt", "eb", "hcal", "hlt", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("csc", "dt", "eb", "hcal", "hlt", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]

modules = ("GuiDQM", "GuiEventDisplay")
basedir = "/tmp/$USER/dqmgui".replace("$USER", pwd.getpwuid(os.geteuid())[0])
envsetup = """
 source $BASE/rpms/cmsset_default.sh
 source $BASE/rpms/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 source $BASE/rpms/slc4_ia32_gcc345/external/py2-pil/1.1.6/etc/profile.d/init.sh
 source $BASE/rpms/slc4_ia32_gcc345/external/libpng/1.2.10/etc/profile.d/init.sh
 source $BASE/rpms/slc4_ia32_gcc345/external/libjpg/6b/etc/profile.d/init.sh
 source $BASE/rpms/slc4_ia32_gcc345/external/libtiff/3.8.2/etc/profile.d/init.sh
 export QUIET_ASSERT=a
""".replace("$BASE", basedir)

server.port        = 8888
server.serverDir   = basedir + "/gui"
server.baseUrl     = '/dqm/devtest'
server.title       = 'CMS data quality'
server.serviceName = 'GUI test'

server.source('DQMLive', 'dqm', '--listen 9191', '--collector localhost:9190')
server.source('DQMArchive', 'file', basedir + "/dqm.db", '--listen 9192')
server.source('DQMLayout', 'layout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
