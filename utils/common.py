#!/usr/bin/env python
# coding=utf-8

import logging
import logging.config

from conf import config

logging.config.dictConfig(config.LOGGING)

logger = logging.getLogger('primary')
debug_logger = logging.getLogger('debug')
