from fabric.utils import abort
from utils import sudo

def add(username, uid=False, gid=False, verbose=False):
	cmd = 'useradd --no-create-home --system '
	if uid:
		cmd += '--uid %s ' % uid
	if gid:
		cmd += '--gid %s ' % uid
	
	cmd += username
	
	result = sudo(cmd)
	if result.succeeded:
		return True
	elif result.stderr.find('already exists') > -1:
		return True
	else:
		abort(result.stderr)

def remove(username, verbose=False):
	cmd = 'userdel --system %s' % username
	return sudo(cmd).succeeded