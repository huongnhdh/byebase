#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Create by: @huongnhd
"""
from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk
from settings import ELASTICSEARCH
# from comm.evar_logging import LOGGER, LogMsgERROR
import logging
logger = logging.getLogger(__name__)


class ElasticSearch(Elasticsearch):
  """
    Adapter for ElasticSearch api

    """

  def __init__(self):

    self.els_conn = self.es_setup_connection()

  @staticmethod
  def es_setup_connection():
    """Set up connection to api """
    els_conn = Elasticsearch(ELASTICSEARCH['host_name'],
                             http_auth=ELASTICSEARCH['http_auth'],
                             port=ELASTICSEARCH['port'])

    try:
      els_conn.ping()
    except:
      logger.error('can not connecting ' % els_conn.url)
      raise ValueError(LogMsgERROR.CAN_NOT_CONNECT % els_conn.url)
    return els_conn

  def evar_parallel_bulk(self, bulk_data):
    """
        Using parallel for bulk data into ElasticSearch
        thread_count is x  & chunk_size=y( we can set thread_count another adapt program and cpu)
        :return:
        """
    LOGGER.debug('Start bulk paralell data into ES')
    for ok, result in parallel_bulk(self.els_conn, bulk_data, thread_count=4):
      action, result = result.popitem()
      doc_id = 'commits/%s' % (result['_id'])
      # process the information from ES whether the document has been
      # successfully indexed
      if not ok:
        LOGGER.error('Failed to %s document %s: %r' % (action, doc_id, result))
      else:
        LOGGER.debug(doc_id)
    LOGGER.debug('End bulk paralell data into ES')

  def indices_exists_type(self, index, doc_type):
    """Determine indecate elasticsearch are exist """
    return self.els_conn.indices.exists_type(index=index, doc_type=doc_type)
