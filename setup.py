#!/usr/bin/env python
# coding: utf-8

import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-custom-anonymous',
    version='0.1',
    author='Georgy Bazhukov',
    author_email='georgy.bazhukov@gmail.com',
    description='Library provides customization of AnonymousUser in Django',
    long_description=read('README.markdown'),
    url='https://github.com/bugov/django-custom-anonymous',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
    ],
    test_suite="runtests",
)
