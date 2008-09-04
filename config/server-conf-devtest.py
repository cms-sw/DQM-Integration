import pwd, os, os.path
global CONFIGDIR
BASEDIR   = "/tmp/$USER/dqmgui".replace("$USER", pwd.getpwuid(os.geteuid())[0])
CONFIGDIR = os.path.normcase(os.path.abspath(__file__)).rsplit('/', 1)[0]

LAYOUTS = ["%s/%s-layouts.py" % (CONFIGDIR, x) for x in
	   ("csc", "dt", "eb", "hcal", "hlt", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]
LAYOUTS += ["%s/shift_%s_layout.py" % (CONFIGDIR, x) for x in
            ("csc", "dt", "eb", "hcal", "hlt", "l1t", "l1temulator", "rpc", "pixel", "sistrip")]

modules = ("GuiDQM", "GuiEventDisplay")
envsetup = "export QUIET_ASSERT=a"

server.port        = 8888
server.serverDir   = basedir + "/gui"
server.baseUrl     = '/dqm/devtest'
server.title       = 'CMS data quality'
server.serviceName = 'GUI test'

server.source('DQMLive', 'dqm', '--listen 9191', '--collector localhost:9190')
server.source('DQMArchive', 'file', basedir + "/dqm.db", '--listen 9192')
server.source('DQMLayout', 'layouts', *LAYOUTS)

execfile(CONFIGDIR + "/dqm-services.py")
execfile(CONFIGDIR + "/workspaces-online.py")
