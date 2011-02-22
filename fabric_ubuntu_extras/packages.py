from fabric.contrib.console import confirm
from utils import sudo

def install(pkg):
	if not installed(pkg):
		return sudo('apt-get install -y %s' % pkg, statusOnly=True)
	else:
		return True

def uninstall(pkg, warn=True):
	print str(installed(pkg))
	
	if installed(pkg):
		cmd = 'apt-get remove -y %s' % pkg
	
		if warn:
		 	if confirm('Are you sure you want to uninstall %s from: %s?' % (pkg, env.host_string)):
				return sudo(cmd, statusOnly=True)
		else:
			return sudo(cmd, statusOnly=True)
	else:
		return True

def installed(pkg):
	result = sudo('aptitude show %s' % pkg)
	if not result.failed:
		return 'State: Installed' == result.splitlines()[0]
	else:
		return False