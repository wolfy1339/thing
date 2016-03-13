from setuptools import setup, find_packages

setup(name='thingdb',
      version='0.2.4',
      description="Python database using dict's",
      url='https://github.com/itslukej/thing',
      author='Luke James',
      author_email='me@lukej.me',
      license='GNU',
      packages=find_packages(),
      install_requires=['pycrypto'],
      zip_safe=False)
