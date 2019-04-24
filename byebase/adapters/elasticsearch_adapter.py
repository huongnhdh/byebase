#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Create by: @huongnhd
"""
import logging as _log
from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk
from byebase.settings import ELASTICSEARCH as default_config
from byebase.decorators import suppress_errors

# end import

class ElasticSearchAdapter():
  """
    Returns a ```ElasticSearch```
  """
  __default_index = None
  __default_doc_type = '_doc'
  __default_client = None

  def __init__(self,config=default_config, *args, **kwargs):
    """[summary]

    Keyword Arguments:
      config {[type]} -- [description] (default: {ELASTICSEARCH})
      index_db {[string]}: -- [description] (default: {indicator})
    """
    self.__default_client = self.__setup_connection(config)

    if kwargs['index']:
      self.__default_index = kwargs['index']
    if kwargs.get('doc_type', None):
      self.__default_doc_type = kwargs['doc_type']

  # @suppress_errors
  def create(self, doc={}, **kwargs):
    # import pdb; pdb.set_trace()
    index = kwargs.get('index', self.__default_index)
    doc_type= kwargs.get('doc_type', self.__default_doc_type)
    self.__default_client.index(index=index,doc_type = doc_type,body = doc)

  def _create(self, docs=[]):
    pass

  def _update(self, doc={}):
    pass

  def _update(self, doc=[]):
    pass

  def _delete(self, doc={}):
    pass

  def _delete(self, docs=[]):
    pass

  def index(self, params={}, **kwargs):
    index = kwargs.get('index', self.__default_index)
    doc_type= kwargs.get('doc_type', self.__default_doc_type)
    return self.__default_client.search(index=index,doc_type = doc_type,body = params)

  def __parallel_bulk(self, bulk_data):
    """
      Using parallel for bulk data into ElasticSearch
      thread_count is x  & chunk_size=y( we can set thread_count another adapt program and cpu)
      :return:
    """
    _log.debug('Start bulk parallel data into ES')
    for ok, result in parallel_bulk(self._conn, bulk_data, thread_count=4):
      action, result = result.popitem()
      doc_id = 'commits/%s' % (result['_id'])
      # process the information from ES whether the document has been
      # successfully indexed
      if not ok:
        _log.error('Failed to %s document %s: %r' % (action, doc_id, result))
      else:
        _log.debug(doc_id)
    _log.debug('End bulk parallel data into ES')

  def __indices_exists_type(self, index, doc_type):
    """Determine indicate elasticsearch are exist """
    return self.__conn.indices.exists_type(index=index, doc_type=doc_type)

  @staticmethod
  def __setup_connection(connection):
    """Set up connection """
    conn = Elasticsearch(
        connection['host_name'],
        #  http_auth=connection['http_auth'],
        port=connection['port'])
    conn.ping()

    return conn