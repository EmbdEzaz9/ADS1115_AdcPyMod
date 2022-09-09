'''
	Python library for the ADS1115 Analog to Digital Converter
	modified by EmbdEzaz9 from DavidH
'''

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(name='ADS1115',
      version='0.2.1',
      description='Python library for interacting with the ADS1115 Analog to Digital Converter.',
      url='http://github.com/EmbdEzaz9/ADS1115_AdcPyMod',
      author='EmbdEzaz9',
      author_email='embdezaz9@gmail.com',
      license='MIT',
      keywords=['ADS1115', 'analog to digital converter', 'adc'],
      packages=['ADS1115'],
      install_requires=[
          'smbus2'
	  ],
      zip_safe=False)
