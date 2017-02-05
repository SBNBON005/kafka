# kafka

## setting Kafka
https://dtflaneur.wordpress.com/2015/10/05/installing-kafka-on-mac-osx/

## Topic creation
start kafka server
```
kafka-server-start /usr/local/etc/kafka/server.properties
```

Produce to the topic
```
kafka-console-producer --broker-list localhost:9092 --topic <topic name>
```

## list of topics
```
kafka-topics --list --zookeeper localhost:2181
```

## Getting started with pyKafka
https://pykafka.readthedocs.io/en/latest/

```
>>> from pykafka import KafkaClient
>>> client = KafkaClient(hosts='127.0.0.1:9092')
```

```
>>> import json

with client.topics['sage_integration_service'].get_sync_producer() as producer:
    producer.produce(json.dumps({'name': 'bongani', 'surnamce': 'sibanda'}))
```