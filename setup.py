#!/usr/bin/env python

"""
Setting up program for pyjpmesh.
"""

import setuptools

setuptools.setup(
    name='pyjpmesh',
    description='Japan mesh code (JIS X 0410) utility for Python.',
    version='0.0.0',
    author='Yu Mochizuki',
    author_email='ymoch.dev@gmail.com',
    url='https://github.com/ymoch/pyjpmesh',
    packages=setuptools.find_packages(),
    test_suite='nose.collector',
    tests_require=['nose', 'mock'],
)
