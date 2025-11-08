import re
import sys
from pathlib import Path
from setuptools import Extension, find_packages, setup
import os

# Get the version number:
with open('hotcent/__init__.py') as f:
    version = re.search("__version__ = '(.*)'", f.read()).group(1)

compile_args = ['-O3']
if not os.environ.get('CI'):
    compile_args.append('-march=native')

extensions = [
    Extension('_hotcent',
              sources=['hotcent/extensions.c'],
              language='c',
              extra_compile_args=compile_args,
              ),
]

files = [
    'hotcent-basis',
    'hotcent-concat',
    'hotcent-tables',
]
scripts = [str(Path('tools') / f) for f in files]

install_requires = [
    'ase>=3.22.0',
    'matplotlib',
    'numpy',
    'pytest',
    'pyyaml',
    'scipy',
]

setup(
  ext_modules=extensions,
  install_requires=install_requires,
  license='LICENSE',
  name='hotcent',
  packages=find_packages(),
  python_requires='>=3.6',
  scripts=scripts,
  url='https://gitlab.com/mvdb/hotcent',
  version=version,
)
