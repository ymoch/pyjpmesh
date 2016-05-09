#!/usr/bin/env python

"""
Setting up program for pyjpmesh.
"""

import os
import setuptools

import jpmesh

def load_long_description():
    """
    Load the long description.
    """
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
        return f.read()


setuptools.setup(
    name='pyjpmesh',
    description='Japan mesh code (JIS X 0410) utility for Python.',
    long_description=load_long_description(),
    version=jpmesh.__version__,
    author=jpmesh.__author__,
    author_email=jpmesh.__author_email__,
    url='https://github.com/ymoch/pyjpmesh',
    py_modules=['jpmesh'],
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
