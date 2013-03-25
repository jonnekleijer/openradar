# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

import datetime
import os
import re

# Directories
BUILDOUT_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..',
)

# Likely to be overwritten
AGGREGATE_DIR = os.path.join(BUILDOUT_DIR, 'var', 'aggregate')
CALIBRATE_DIR = os.path.join(BUILDOUT_DIR, 'var', 'calibrate')
CONSISTENT_DIR = os.path.join(BUILDOUT_DIR, 'var', 'consistent')
GROUND_DIR = os.path.join(BUILDOUT_DIR, 'var', 'ground')
IMG_DIR = os.path.join(BUILDOUT_DIR, 'var', 'img')
MISC_DIR = os.path.join(BUILDOUT_DIR, 'var', 'misc')
MULTISCAN_DIR = os.path.join(BUILDOUT_DIR, 'var', 'multiscan')
RADAR_DIR = os.path.join(BUILDOUT_DIR, 'var', 'radar')
SOURCE_DIR = os.path.join(BUILDOUT_DIR, 'var', 'source')
THREDDS_DIR = os.path.join(BUILDOUT_DIR, 'var', 'thredds')

# Unlikely to be overwritten
CELERY_DIR = os.path.join(BUILDOUT_DIR, 'var', 'celery')
LOG_DIR = os.path.join(BUILDOUT_DIR, 'var', 'log')

# Celery
CELERY_DB = os.path.join(CELERY_DIR, 'celerydb.sqlite')

# Default nodatavalue
NODATAVALUE = -9999

# Declutter defaults
DECLUTTER_HISTORY = 50
DECLUTTER_SIZE = 4

# Radar codes
DWD_RADARS_2011 = ('ase', 'nhb', 'emd')
DWD_RADARS = ('ess', 'nhb', 'emd')
KNMI_RADARS = ('NL60', 'NL61')
ALL_RADARS = DWD_RADARS + KNMI_RADARS

# New DWD files have an id that corresponds to the radar code
RADAR_ID = {
    'emd': '10204',
    'ess': '10410',
    'nhb': '10605',
}

# Regex patterns
RADAR_PATTERNS = [
    # KNMI
    re.compile(
        'RAD_(?P<code>.*)_VOL_NA_(?P<timestamp>[0-9]{12})\.h5',
    ),
    # DWD 2011
    re.compile(
        'raa00-dx_(?P<code>.*)-(?P<timestamp>[0-9]{10})-dwd---bin',
    ),
    # DWD
    re.compile(
        'raa00-dx_(?P<id>.*)-(?P<timestamp>[0-9]{10})-(?P<code>.*)---bin',
    ),
]
GROUND_PATTERN = re.compile(
    '(?P<timestamp>[0-9]{14})_Grondstations_(?P<code>.*)\.csv',
)
CALIBRATION_PATTERN = re.compile(
    'GEO *= *(?P<a>[-.0-9]+) *\* *PV *\+ *(?P<b>[-.0-9]+)',
)

# Templates that reveal datetime format when code and id are substituted
TEMPLATE_KNMI = 'RAD_{code}_VOL_NA_%Y%m%d%H%M.h5'
TEMPLATE_DWD_2011 = 'raa00-dx_{code}-%y%m%d%H%M-dwd---bin'
TEMPLATE_DWD = 'raa00-dx_{id}-%y%m%d%H%M-{code}---bin'
TEMPLATE_GROUND = '%Y%m%d%H%M%S_Grondstations_{code}.csv'

# Format for all-digit timestamp
TIMESTAMP_FORMAT = '%Y%m%d%H%M%S'

# Gridproperties for resulting composite (left, right, top, bottom)
COMPOSITE_EXTENT = (-110000, 390000, 700000, 210000)
COMPOSITE_CELLSIZE = (1000, 1000)

# DWD coordinates using standard transformation from EPSG:4314 to EPSG:4326
DWD_COORDINATES = dict(
    ase=(51.405659776445475, 6.967144448033989),
    emd=(53.33871596412482, 7.023769628293414),
    ess=(51.405659776445475, 6.967144448033989),
    nhb=(50.1097523464156, 6.548542364687092),
)

# Radar altitudes
# To be merged and stored in km.
ANTENNA_HEIGHT = dict(
    ase=185.10,
    emd=58.00,
    ess=185.10,
    nhb=585.15,
    NL60=44,
    NL61=51,
)

# KNMI scan selection
KNMI_SCAN_NUMBER = 2
KNMI_SCAN_TYPE = 'Z'

# Naming of products and files
MULTISCAN_CODE = 'multiscan'
GROUND_CODE = {'f': '5min', 'h': 'uur', 'd': '24uur'}
TIMEFRAME_DELTA = {
    'f': datetime.timedelta(minutes=5),
    'h': datetime.timedelta(hours=1),
    'd': datetime.timedelta(days=1),
}
FRAMESTAMP = dict(f='0005', h='0100', d='2400')
PRODUCT_CODE = {t: {p: 'TF{}_{}'.format(FRAMESTAMP[t], p.upper())
                    for p in 'rna'}
                for t in 'fhd'}
PRODUCT_TEMPLATE = 'RAD_{code}_{timestamp}.h5'

# Delays for waiting-for-files
WAIT_SLEEP_TIME = 10  # Seconds
WAIT_EXPIRE_DELTA = datetime.timedelta(minutes=3)

# Productcopy settings, for fews import, for example.
COPY_TARGET_DIRS = []

# Root path to opendap data, for retrieval only.
OPENDAP_ROOT = 'http://opendap.nationaleregenradar.nl/thredds/dodsC/radar'

# FTP settings
# Publishing
FTP_HOST = ''  # Empty to skip ftp publishing
FTP_USER = 'MyUser'
FTP_PASSWORD = 'MyPassword'
# Imports and throughputs
FTP_RADARS = {}
# Throughputs of radar related data to client ftp.
FTP_THROUGH = {}

# Import local settings
try:
    from openradar.localconfig import *
except ImportError:
    pass


