from setuptools import setup

setup(name='ovcrypt',
      version='0.1',
      description='Ovcrypt',
      url='http://overhosting.ru',
      author='Dmitry Yakovlev',
      author_email='info@overhosting.ru',
      license='Copyright Overhosting.ru',
      packages=['ovcrypt'],
      scripts=[],
      install_requires=[
            'rsa',
            'bs4',
            'requests',
            'oe_common'
      ],
      # entry_points={
      #    'console_scripts': [
      #        'cpufreq = cpufreq.run:main',
      #    ],
      # },
      zip_safe=False)
