#!/usr/bin/env python
sdict = {
    'name' : 'fabric-ubuntu-extras',
    'version' : '0.0.1',
    'description' : 'A few extras for fabric on Ubuntu systems',
    'long_description' : 'A few extras for fabric on Ubuntu systems',
    'url': 'http://github.com/votizen/fabric-ubuntu-extras',
    'author' : 'Micheil Smith',
    'author_email' : 'micheil@votizen.com',
    'maintainer' : 'Micheil Smith',
    'maintainer_email' : 'micheil@votizen.com',
    'keywords' : ['Fabric', 'Ubuntu'],
    'license' : 'MIT',
    'classifiers' : [
        'Programming Language :: Python'
    ],
    'install_requires': ['fabric'],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
setup(**sdict)
