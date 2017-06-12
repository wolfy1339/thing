from setuptools import setup, find_packages
from sys import version_info
import sys

if version_info < (2, 7, 0) or (version_info[0] == 3 and version_info < (3, 2, 0)):
    sys.stderr.write('zIRC requires Python 2.7 or 3.2 and higher')
    sys.exit(-1)

setup(name='thingdb',
      version='4.0.0',
      description="Python database using dict's",
      url='https://github.com/itslukej/thing',
      author='Luke James',
      author_email='me@lukej.me',
      license='GNU',
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ])
