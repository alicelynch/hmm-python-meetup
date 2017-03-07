#! /usr/bin/env python

from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3.4'
    ]

setup(
    name='hmm-python-meetup',
    version='0.0.1',
    description='Demo HMM',

    author='Alice Lynch',
    author_email='alice.lynch@zalando.ie',

    packages=find_packages(),
    package_data={'hmm-python-meetup': ['resources/*']},
    include_package_data=True,
    install_requires=[],

    test_suite='test')
