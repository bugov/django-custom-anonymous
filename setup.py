#!/usr/bin/env python
# coding: utf-8

import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires=[
    'django',
]

setup(
    name='django-custom-anonymous',
    version='0.4',
    author='Georgy Bazhukov',
    author_email='georgy.bazhukov@gmail.com',
    description='Library provides customization of AnonymousUser in Django',
    long_description=read('README.markdown'),
    url='https://github.com/bugov/django-custom-anonymous',
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite="runtests",
    requires=requires,
    tests_require=requires,
    setup_requires=requires,
)
