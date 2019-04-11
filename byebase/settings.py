
"""
@author huongnhd
"""

import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
ELASTICSEARCH = {
    'host_name': 'abc.dns.net',
    # 'http_auth': ('', '********'),
    'port': 9200
}
# link for dev
# AMQPURL = 'amqp://cfpzarme:MqsdI8OBcuTy_C1C1JP1B2a8APAWQzf1@mustang.rmq.cloudamqp.com/cfpzarme'
AMQPURL = 'amqp://guest:guest@localhost:5672/%2F'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# folder storage file downloaded from google storage
GLOBAL_MAIN_TEMP_DIR = '/tmp'
LOG_COF = 'settings'
