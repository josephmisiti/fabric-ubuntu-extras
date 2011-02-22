from utils import sudo


def add(username, uid=False, verbose=False):
	cmd = 'useradd --no-create-home --system'
	if uid:
		cmd += '--uid %s' % uid
	
	cmd += username
	
	return sudo(cmd).succeeded

def remove(username, verbose=False):
	cmd = 'userdel --system %s' % username
	return sudo(cmd).succeeded