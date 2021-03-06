#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='nerve-tools',
    version='0.11.2',
    provides=['nerve_tools'],
    author='John Billings',
    author_email='billings@yelp.com',
    description='Nerve-related tools for use on Yelp machines',
    packages=find_packages(exclude=['tests']),
    setup_requires=['setuptools'],
    include_package_data=True,
    install_requires=[
        'argparse>=1.2.1',
        'environment_tools>=1.1.0,<1.2.0',
        'kazoo>=2.0.0',
        'PyYAML>=3.11',
        'paasta-tools==0.32.2',
        'requests>=2.6.2',
        'service-configuration-lib==0.10.1',
        'functools32==3.2.3-2',
    ],
    entry_points={
        'console_scripts': [
            'clean_nerve=nerve_tools.clean_nerve:main',
            'configure_nerve=nerve_tools.configure_nerve:main',
            'updown_service=nerve_tools.updown_service:main',
        ],
    },
)
