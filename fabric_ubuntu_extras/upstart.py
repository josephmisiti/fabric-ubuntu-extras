from utils import sudo

def start(job):
	return sudo('start %s' % job, statusOnly=True)

def stop(job):
	return sudo('stop %s' % job, statusOnly=True)

def status(job, status='start/running'):
	result = sudo('status %s' % job)
	
	if not result.failed:
		return result.find(status) > -1
	else:
		return False

def print_status(job):
	print ""
	
	if status(job):
		print "%s is currently running" % job
	else:
		print "%s is currently not running" %job

def reload():
	return sudo('initctl reload-configuration')

