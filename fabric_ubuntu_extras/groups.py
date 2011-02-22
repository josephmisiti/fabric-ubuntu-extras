from utils import sudo

def add(grpname):
	result = sudo('groupadd --system %s' % grpname).succeeded
	if not result.failed:
		return result.stderr.endswith('already exists'):
	else:
		return False

def remove(groupdel):
	return sudo('groupdel %s' % grpname).succeeded