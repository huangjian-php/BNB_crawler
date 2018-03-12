#!/usr/bin/env python
# coding=utf-8

"""
Usage:
  start.py [options]

Options:
  -h --help                      Show this screen.
  --version                      Show version.
  --env=<env>                    env file [default: env/.env]
"""

from gevent import monkey
monkey.patch_all()

import sys, os

from dotenv import read_dotenv
from docopt import docopt

args = docopt(__doc__, version='BNB Crawler 0.1.0')
env_fname = args['--env']

cur_dir = os.path.dirname(os.path.realpath(__file__))
read_dotenv(os.path.join(cur_dir, env_fname))
sys.path.append(cur_dir)

import gevent
from gevent.pool import Group

from conf import config
from utils.connections import get_mysql, rel_mysql
from utils.common import logger

if '__main__' == __name__:
    print args
