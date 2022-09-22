#!/usr/bin/env python3

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

keywords = [
    'patroni',
    'infoblox',
    'patroni-callback',
    'patroni-infoblox'
]

with open('README.rst') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

platforms = 'OS Independent'

classifiers = [
    'Development Status :: 1 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3 :: Only',
]

def main():
    if sys.version_info[:2] < (3, 0):
        sys.stderr.write("patroni-infoblox-integration requires Python version 3.0 or higher.\n")
        sys.exit(1)

    if sys.argv[-1] == 'setup.py':
        sys.stdout.write("To install, run 'python3 setup.py install'\n\n")

    setup_options = dict(
        author='Goran Kuzmanovic',
        author_email='goran.kuzmanovic@protonmail.com',
        classifiers=classifiers,
        description='Integration between Patroni and Infoblox using WAPI',
        keywords=keywords,
        include_package_data=True,
        license='Apache',
        long_description=long_description,
        name='patroni-infoblox-integration',
        platforms=platforms,
        scripts=['scripts/infoblox-callback.py'],
        url='https://github.com/goran-kuzmanovic/patroni-infoblox-integration',
        version='1.0.0',
        install_requires=install_requires,
    )

    setup(**setup_options)

if __name__ == "__main__":
    main()
