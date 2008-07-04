import pwd, os, os.path
global CONFIGDIR
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]
LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("csc", "dt", "eb", "ecal", "ee", "hcal", "l1t", "rpc")]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("dt", "eb", "hcal", "l1t", "l1temulator", "hlt")]

modules = ("GuiDQM",)
basedir = "/tmp/$USER/dqmgui".replace("$USER", pwd.getpwuid(os.geteuid())[0])
envsetup = """
 source $BASE/rpms/cmsset_default.sh
 source $BASE/rpms/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.sh
 export QUIET_ASSERT=a
""".replace("$BASE", basedir)

server.port        = 8888
server.serverDir   = basedir + "/gui"
server.baseUrl     = '/dqm/devtest'
server.title       = 'CMS data quality'
server.serviceName = 'GUI test'

server.source('dqm', 'DQMLive', '--listen 9191', '--collector localhost:9190')
server.source('file', 'DQMArchive', basedir + "/dqm.db", '--listen 9192')
server.source('layouts', 'DQMLayout', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
