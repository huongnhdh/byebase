"""
@author huongnhd
"""

import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
#  BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ELASTICSEARCH = {
    'host_name': 'localhost',
    # 'http_auth': ('', '********'),
    'port': 9200
}

# link for monitor amqp: https://eagle.rmq.cloudamqp.com/#/connections
# AMQPURL = 'amqp://sbeftlyb:b7aSqyzBjHmZo-H5s8G7mM1bW8u55e0V@eagle.rmq.cloudamqp.com/sbeftlyb'
AMQPURL = 'amqp://guest:guest@localhost:5672/%2F'

# folder storage file downloaded from google storage
TEMP_DIR = os.getenv('TEMP_DIR', '/tmp')

PYTHON_ENV = os.getenv('PYTHON_ENV', 'development')

LOG_CFG = os.getenv('LOG_CFG', os.path.join(BASE_DIR, 'conf/logging.yml'))