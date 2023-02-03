from kafka import KafkaConsumer
from json import loads
from time import sleep
from os import environ as env
import logging

# reading configs from environment variables
servers = env['KAFKA_SERVERS'].split(',')
topic = env['KAFKA_TOPIC']
auto_offset_reset_plan = env.get('AUTO_OFFSET_RESET', 'latest') 
logLevel = env.get('LOG_LEVEL','WARNING')

# logging config
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logLevel)

# waiting for kafka and zookeeper being ready
sleep(5)

consumer = KafkaConsumer(
    topic,
    bootstrap_servers = servers,
    auto_offset_reset = auto_offset_reset_plan,
    api_version=(0,11,5),
    session_timeout_ms=10000,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for msg in consumer:
    data = msg.value
    print(data)
    logging.info('received --' +str(data))
