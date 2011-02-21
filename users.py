from utils import sudo


def add(username, uid=False, verbose=False):
	cmd = 'useradd --no-create-home --system %s' % username
	if uid:
		cmd += '--uid %s' % uid
	
	return sudo(cmd, statusOnly=True)

def remove(username, verbose=False):
	cmd = 'userdel --system %s' % username
	return sudo(cmd, statusOnly=True)