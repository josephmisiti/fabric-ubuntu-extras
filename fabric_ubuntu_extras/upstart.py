from os import path
from utils import *

def start(job):
	return sudo('start %s' % job).succeeded

def stop(job):
	return sudo('stop %s' % job).succeeded

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
		print "%s is currently not running" % job

def reload():
	return sudo('initctl reload-configuration')

def add_job(name, filename):
	return sudo_put(filename, '/etc/init/%s.conf' % name, 0644)

def remove_job(name):
	return sudo('rm -f /etc/init/%s' % (name, name))
