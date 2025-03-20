#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import requirements as reqs
import os

# Extract the requirements from the deps file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "requirements.txt")) as f:
    requirements = [r.line for r in reqs.parse(f)]

with open(os.path.join(here, "requirements_dev.txt")) as f:
    test_requirements = [r.line for r in reqs.parse(f)]

with open(os.path.join(here, 'README.md')) as f:
    readme = f.read()

setup(
    name='prueba_lib_pyspark',
    version='1.0.1',
    description='Library Python project',
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='tests',
    packages=find_packages(),
)
