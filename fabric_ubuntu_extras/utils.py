from os import path
from fabric.api import sudo as _sudo
from fabric.context_managers import *

def sudo(cmd, verbose=False):
	if verbose:
		with settings(warn_only=True):
			return _sudo(cmd)
	else:
		# Otherwise, be quiet
		with settings(hide('everything'), warn_only=True):
			return _sudo(cmd)

def sudo_put(local_path, remote_path, mode=None):
	name = path.basename(remote_path)
	put(local_path, '/tmp/%s' % name, mode)
	sudo('mv /tmp/%s %s' % (name, remote_path))