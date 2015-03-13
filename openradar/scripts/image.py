#!/usr/bin/python
# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

from openradar import arguments
from openradar import config
from openradar import images
from openradar import loghelper
from openradar import products
from openradar import scans
from openradar import utils


def get_image_args():
    argument = arguments.Argument()
    parser = argument.parser(
        ['image_dir', 'range'],
        description='Create images from radar data.',
    )
    parser.add_argument('--postfix',
                        type=str,
                        default='',
                        help='Postfix for filename.')
    parser.add_argument('--label',
                        type=str,
                        default='',
                        help='Label text in image.')
    parser.add_argument('-p', '--prodcode',
                        choices=['r', 'n', 'a'],
                        default='r',
                        help='(r)ealtime, (n)ear-realtime or (a)fterwards')
    parser.add_argument('-c', '--product',
                        choices=['a', 'b', 'c', 'n'],
                        default='b',
                        help=('(a)ggregate, cali(b)rated, '
                              '(c)onsistent or (n)owcast'))
    parser.add_argument('-t', '--timeframe',
                        choices=['f', 'h', 'd'],
                        default='f',
                        help='(f)ive minute, (h)our or (d)ay')
    parser.add_argument('-f', '--format',
                        type=str,
                        default='png',
                        choices=['png', 'tif'],
                        help='Save "tif" or "png"')
    return vars(parser.parse_args())


def product_generator(product, prodcode, timeframe, datetimes):
    """ Return product generator. """
    if product == 'a':
        combinations = utils.get_aggregate_combinations(
            datetimes=datetimes,
            timeframes=timeframe,
        )
        for combination in combinations:
            yield scans.Aggregate(
                declutter=None,
                radars=config.ALL_RADARS,
                basedir=config.AGGREGATE_DIR,
                multiscandir=config.MULTISCAN_DIR,
                grid=scans.BASEGRID,
                **combination
            )
    else:
        combinations = utils.get_product_combinations(
            datetimes=datetimes,
            prodcodes=prodcode,
            timeframes=timeframe,
        )
        Product = dict(
            b=products.CalibratedProduct,
            c=products.ConsistentProduct,
            n=products.NowcastProduct,
        )[product]
        for combination in combinations:
            yield Product(**combination)


def main():
    """ Create images for a range of products. """
    loghelper.setup_logging()

    # Get products according to args
    args = get_image_args()

    multidaterange = utils.MultiDateRange(args['range'])
    products = product_generator(product=args['product'],
                                 prodcode=args['prodcode'],
                                 timeframe=args['timeframe'],
                                 datetimes=multidaterange.iterdatetimes())

    create = dict(png=images.create_png,
                  tif=images.create_tif)[args['format']]

    # Create images with those products
    kwargs = args.copy()
    map(kwargs.pop, ['range', 'product', 'timeframe', 'prodcode'])
    create(products, **kwargs)
