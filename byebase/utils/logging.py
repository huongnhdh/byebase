#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Create by: @huongnhd
"""
import os
import logging

import yaml
from byebase.settings import LOG_CFG
from byebase.decorators import suppress_errors


@suppress_errors
def setup_logging(default_level=logging.NOTSET, path_config = LOG_CFG):
  """Setup logging configuration"""
  try :
    with open(path_config, 'rt') as file_config:
      config_logging = yaml.safe_load(file_config.read())
    logging.config.dictConfig(config_logging)
  except:
      logging.basicConfig(level=default_level)

# run in init running
setup_logging()
