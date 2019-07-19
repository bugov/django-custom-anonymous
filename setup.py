#!/usr/bin/env python
# coding: utf-8

import os
from setuptools import setup, find_packages

from custom_anonymous import __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires=[
    'django',
]

setup(
    name='django-custom-anonymous',
    version=__version__,
    author='Georgy Bazhukov',
    author_email='georgy.bazhukov@gmail.com',
    description='Library provides customization of AnonymousUser in Django',
    long_description=read('README.rst'),
    long_description_content_type='text/markdown',
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
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
)
