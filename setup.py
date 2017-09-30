#!/usr/bin/env python
"""
Python package setup file.
"""
from setuptools import setup, find_packages


# Dynamically retrieve the version information from the PACKAGE
PACKAGE = __import__('environment_file')
VERSION = PACKAGE.__version__
AUTHOR = PACKAGE.__author__
AUTHOR_EMAIL = PACKAGE.__email__
URL = PACKAGE.__url__
DOWNLOAD_URL = PACKAGE.__download__
DESCRIPTION = PACKAGE.__doc__
LONG_DESCRIPTION = '''
Environment File
================
'''

setup(
    name='environment-file',
    version=VERSION,
    url=URL,
    download_url=DOWNLOAD_URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    include_package_data=False,
    license='MIT',
    zip_safe=True,
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python PACKAGEs',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests'
)
