from os import path
from fabric.contrib import files
from utils import sudo, sudo_put

def start(job):
	return sudo('start %s' % job).succeeded

def stop(job):
	return sudo('stop %s' % job).succeeded

def status(job, status='start/running'):
	result = sudo('status %s' % job)
	
	if result.succeeded:
		return result.find(status) > -1
	else:
		return False

def print_status(job):
	if status(job):
		print "%s is currently running" % job
	else:
		print "%s is currently not running" % job

def reload():
	return sudo('initctl reload-configuration')

def add(name, filename):
	return sudo_put(filename, '/etc/init/%s.conf' % name, 0644)

def remove(name):
	return sudo('rm -f /etc/init/%s.conf' % name)

def exists(name):
	return files.exists('/etc/init/%s.conf' % name)

def add_jobs(jobs):
	for job in jobs:
		add(job['name'], job['file'])

def remove_jobs(jobs):
	for job in jobs:
		remove(job['name'])

def start_jobs(jobs):
	for job in jobs:
		start(job['name'])

def stop_jobs(jobs):
	for job in jobs:
		stop(job['name'])
