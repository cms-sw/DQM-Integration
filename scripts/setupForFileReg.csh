setenv CVS_RSH ssh
setenv CVSROOT :ext:cmscvs.cern.ch:/cvs_server/repositories/CMSSW
source ~cmssw2/cmsset_default.csh     # Get CMS commands like 'scramv1'

set dir = `pwd`
#scramv1 p CMSSW CMSSW_2_0_8
cd /cms/mon/data/dqm/CMSSW_2_0_8/src
#cvs -Q co DQMServices VisMonitoring/DQMServer
#cvs -Q up -r V03-00-03-for-18x DQMServices/Components
perl -p -i -e 's|";$|.,:%[]>";| if /s_safe =/' DQMServices/Core/src/DQMStore.cc
#scramv1 b -j 4

eval `scramv1 run -csh`
#source /home/dqm/rpms/slc4_ia32_gcc345/cms/webtools/1.0.0/etc/profile.d/dependencies-setup.csh
#source /home/dqm/rpms/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.csh
source /cms/mon/data/dqm/rpms/slc4_ia32_gcc345/cms/webtools/1.3.0/etc/profile.d/dependencies-setup.csh
cd $dir

setenv TNS_ADMIN /nfshome0/xiezhen/conddb
