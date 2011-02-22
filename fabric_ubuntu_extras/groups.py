from utils import sudo

def add(grpname, gid=False):
	cmd = 'groupadd --system %s' % grpname
	if gid:
		cmd = 'groupadd --system --gid %i %s' % (gid, grpname)
	
	result = sudo(cmd)
	if not result.failed:
		return result.stderr.endswith('already exists'):
	else:
		return False

def remove(groupdel):
	return sudo('groupdel %s' % grpname).succeeded