#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

VERSION = "0.2.0"

setup(
    name='jetstream.core',
    version=VERSION,
    description='Boilerplate for a namespaced Python package.',
    long_description=readme + '\n\n' + history,
    author='Petri Savolainen',
    author_email='petri.savolainen@koodaamo.fi',
    url='https://github.com/koodaamo/jetstream.core',
    namespace_packages = ["jetstream"],
    packages = ['jetstream.core'],
    include_package_data=True,
    install_requires=[
        "setuptools",
        "pyyaml",
    ],
    license="GPLv3",
    zip_safe=False,
    keywords='jetstream',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    extras_require={
       "docs": ["sphinxcontrib.programoutput", "sphinx-better-theme"]
    },
    tests_require = ("colorama"),
    test_suite='tests.test_suite',
)
