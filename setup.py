# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='py_subsea_opt',
    version='0.0.1',
    description='Package for Submarine Cable System Development and Deployment',
    long_description=readme,
    author='Mitsunobu Iwasaki',
    author_email='mi2.postbox@gmail.com',
    install_requires=['numpy'],
    url='https://github.com/th1nkd0g/py_subsea_opt',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

