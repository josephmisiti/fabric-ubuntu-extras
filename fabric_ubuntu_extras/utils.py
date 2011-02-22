from fabric.api import sudo as _sudo
from fabric.context_managers import *

def sudo(cmd, verbose=False, statusOnly=False):
	if verbose:
		with settings(warn_only=True):
			return _sudo(cmd)
	else:
		# Otherwise, be quiet
		with settings(hide('everything'), warn_only=True):
			return _sudo(cmd)