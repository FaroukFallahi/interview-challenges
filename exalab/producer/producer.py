import logging
from requests import get
from time import sleep
from json import dumps
from kafka import KafkaProducer
from os import environ as env

# reading configs from environment variables
servers = env['KAFKA_SERVERS'].split(',')
topic = env['KAFKA_TOPIC']
webApi = env.get('IP_WEB_API', 'https://api.ipify.org/') 
logLevel = env.get('LOG_LEVEL','WARNING')

# logging config
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logLevel)

# waiting for kafka and zookeeper being ready
sleep(6)

producer = KafkaProducer(
    bootstrap_servers=servers,
    api_version=(0,11,5),
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

while True:
    ip = get(webApi).text
    data = {'ip': ip}
    producer.send(topic, value=data)
    logging.info('sent -- '+ str(data))
    sleep(5)

