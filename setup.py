from setuptools import setup

version = '0.3.8.dev0'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Pillow',
    'celery',
    'celery[redis]',
    'gdal',
    'h5py>=2.3.1',
    'matplotlib',
    'numpy',
    'pandas',
    'pytz',
    'raster-store',
    'redis',
    'rpy2',
    'scipy>=0.13.3',
    'setuptools',
    'supervisor',
    'turn',
    ],

tests_require = [
    ]

setup(name='openradar',
      version=version,
      description="TODO",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords=[],
      author='TODO',
      author_email='TODO@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['openradar'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
              # Main tasks
              'master = openradar.scripts.master:main',
              'sync = openradar.scripts.sync:main',
              'cleanup = openradar.scripts.cleanup:main',
              'sync_radar_to_ftp = openradar.scripts.sync_radar_to_ftp:main',
              # Subtasks
              'aggregate = openradar.scripts.aggregate:main',
              'calibrate = openradar.scripts.calibrate:main',
              'rescale = openradar.scripts.rescale:main',
              'publish = openradar.scripts.publish:main',
              'nowcast = openradar.scripts.nowcast:main',
              # Tools
              'clutter = openradar.scripts.clutter:main',
              'histogram = openradar.scripts.histogram:main',
              'organize = openradar.scripts.organize:main',
              'report = openradar.scripts.report:main',
              'repair = openradar.scripts.repair:main',
              'image = openradar.scripts.image:main',
              'elevation_image = openradar.scripts.elevation_image:main',
              # Store interaction
              'atomic-init = openradar.atomic.init:main',
              'atomic-merge = openradar.atomic.merge:main',
              'atomic-move = openradar.atomic.move:main',
              'atomic-nowcast = openradar.atomic.nowcast:main',
              'atomic-report = openradar.atomic.report:main',
              'atomic-store = openradar.atomic.store:main',
          ]},
      )
