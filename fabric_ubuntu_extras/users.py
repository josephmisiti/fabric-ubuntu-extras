from utils import sudo


def add(username, uid=False, verbose=False):
	cmd = 'useradd --no-create-home --system'
	if uid:
		cmd += '--uid %s' % uid
	
	cmd += username
	
	result = sudo(cmd).succeeded
	if not result.succeeded:
		print result
	return result

def remove(username, verbose=False):
	cmd = 'userdel --system %s' % username
	return sudo(cmd).succeeded