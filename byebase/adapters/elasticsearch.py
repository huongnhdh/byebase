#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Create by: @huongnhd
"""
import logging
from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk
from byebase.settings import ELASTICSEARCH
from byebase.decorators import suppress_errors

# end import

logger = logging.getLogger(__name__)


class ElasticSearch(Elasticsearch):
  """ Adapter for ElasticSearch client  """

  def __init__(self, config=ELASTICSEARCH):
    self.conn = self.setup_connection(config)

  @staticmethod
  @suppress_errors
  def setup_connection(connection):
    """Set up connection """
    els_conn = Elasticsearch(connection['host_name'],
                             http_auth=connection['http_auth'],
                             port=connection['port'])
    try:
      els_conn.ping()
    except BaseException:
      logger.error('Elasticsearch can not connecting to' %
                   connection['host_name'])
      raise ValueError('CAN_NOT_CONNECT to %s' % connection['host_name'])
    return els_conn

  def parallel_bulk(self, bulk_data):
    """
            Using parallel for bulk data into ElasticSearch
            thread_count is x  & chunk_size=y( we can set thread_count another adapt program and cpu)
            :return:
            """
    logger.debug('Start bulk parallel data into ES')
    for ok, result in parallel_bulk(self.conn, bulk_data, thread_count=4):
      action, result = result.popitem()
      doc_id = 'commits/%s' % (result['_id'])
      # process the information from ES whether the document has been
      # successfully indexed
      if not ok:
        logger.error('Failed to %s document %s: %r' % (action, doc_id, result))
      else:
        logger.debug(doc_id)
    logger.debug('End bulk parallel data into ES')

  def indices_exists_type(self, index, doc_type):
    """Determine indicate elasticsearch are exist """
    return self.conn.indices.exists_type(index=index, doc_type=doc_type)
