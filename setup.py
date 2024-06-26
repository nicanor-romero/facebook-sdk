#!/usr/bin/env python
from setuptools import setup

exec(open("facebook/version.py").read())

setup(
    name='facebook-sdk-nromero',
    version=__version__,                # noqa: F821
    description='This client library (fork) is designed to support the Facebook '
                'Graph API (v16) and the official Facebook JavaScript SDK, which '
                'is the canonical way to implement Facebook authentication.',
    author='Facebook',
    maintainer='Nicanor Romero',
    maintainer_email='martey+facebook-sdk@mobolic.com',
    url='https://github.com/nicanor-romero/facebook-sdk',
    license='Apache',
    packages=["facebook"],
    long_description=open("README.rst").read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=['requests'],
    tests_require=["coverage"],
)
