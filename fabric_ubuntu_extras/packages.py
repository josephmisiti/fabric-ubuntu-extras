from fabric.utils import abort
from fabric.contrib.console import confirm
from utils import sudo

def _msg(msg, silent):
	if not silent:
		print msg

def install(pkg, silent=False):
	status = installed(pkg)
	
	if status == True:
		_msg('Already installed: %s' % pkg, silent)
		return True
	elif status == False:
		_msg('Installing %s...' % pkg, silent)
		# Update result, as generally you want to know 
		# if something did actually install
		result = sudo('apt-get install -y %s' % pkg)
		if result.failed:
			abort(result.stderr)
		else:
			_msg('Installed %s' % pkg, silent)
			return result
	else:
		abort(result.stderr)

def uninstall(pkg, warn=True, silent=False):
	status = installed(pkg)
	
	if status == True:
		_msg('Uninstalling %s...' % pkg, silent)
		cmd = 'apt-get remove -y %s' % pkg
	
		if warn:
			if confirm('Are you sure you want to uninstall %s from: %s?' % (pkg, env.host_string)):
				result = sudo(cmd)
		else:
			result = sudo(cmd)
		
		if result.failed:
			about(result.stderr)
		else:
			_msg('Uninstalled %s' % pkg, silent)
			return 
	elif status == False:
		_msg('Not Already Installed %s: Skipped' % pkg, silent)
	else:
		abort(result.stderr)

def installed(pkg):
	result = sudo('aptitude show %s' % pkg)
	if result.failed:
		return result
	else:
		return 'State: installed' == result.splitlines()[1]