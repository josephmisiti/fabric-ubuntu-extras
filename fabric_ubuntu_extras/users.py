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
	if not result.failed:
		return result.stderr.endswith('already exists')
	else:
		return False
	

def remove(username, verbose=False):
	cmd = 'userdel --system %s' % username
	return sudo(cmd).succeeded