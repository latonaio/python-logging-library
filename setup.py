#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
	name='custom_logger',
	version='0.1.0',
	description='logging library',
	long_description='logging library',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'python-json-logger==2.*',
	],
	entry_points='''
''')
