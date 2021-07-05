#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Manas Mengle",
    author_email='manmenonsense@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="An Isometric 3D port of tejmen/bordertale, written using Python and the Pygame module.",
    entry_points={
        'console_scripts': [
            'bordertale_3d=bordertale_3d.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bordertale_3d',
    name='bordertale_3d',
    packages=find_packages(include=['bordertale_3d', 'bordertale_3d.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/appcreatorguy/bordertale_3d',
    version='0.0.1',
    zip_safe=False,
)
