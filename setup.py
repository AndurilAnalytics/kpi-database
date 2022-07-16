# -*- coding: utf-8 -*-
import os
import sys
import io

from setuptools import find_packages, setup

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

# When executing the setup.py, we need to be able to import ourselves, this
# means that we need to add the src/ directory to the sys.path.
sys.path.insert(0, src_dir)

with io.open(os.path.join(base_dir, "README.md"), 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
      name = 'anduril_kpi',
      version = '0.1',
      maintainer = 'groyster',
      maintainer_email = 'royster.giles@gmail.com',
      description = 'Anduril KPI project',
      long_description=readme,
      package_dir={"": "src"},
      packages=find_packages(where="src"),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'pandas',
          'numpy',
          'scikit-learn',
          'pandera',
          'pytest'
        ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )
