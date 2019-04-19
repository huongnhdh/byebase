#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""suppress_errors

 @author: huongnhd
"""

import logging
import functools
_log = logging.getLogger(__name__)


def suppress_errors(log_func=None):
  """[summary]

    Keyword Arguments:
        log_func {[type]} -- [description] (default: {None})

    Returns:
        [type] -- [description]
    """

  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      try:
        return func(*args, **kwargs)
      except Exception as e:
        _log.error(func.__name__)
        if log_func is not None:
          log_func(str(e))
        return None

    return (wrapper)

  return (decorator)
