#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='lang_dynmcs',
    version='0.1.0',
    description="Langevin Dynamics program for computing particle",
    long_description=readme + '\n\n' + history,
    author="Orkhan Abdullayev",
    author_email='spectrum_touch@yahoo.com',
    url='https://github.com/spectrumtouch/lang_dynmcs',
    packages=[
        'lang_dynmcs',
    ],
    package_dir={'lang_dynmcs':
                 'lang_dynmcs'},
    entry_points={
        'console_scripts': [
            'lang_dynmcs=lang_dynmcs.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='lang_dynmcs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
