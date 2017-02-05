from jsonschema import validate

import kafka.topics.topic_registry as tr

class BongzKafkaProducer(object):
    def __init__(self, pykafka_producer, topic):
        self.producer = pykafka_producer
        self.topic = topic
        self.partition_key = tr.get_partition_key(self.topic)

    def send(self,message, event_type):
        schema = tr.get_event_schema(self.topic, event_type):
        validate(message, schema)
        partition_value = message[self.partition_key]
        self.producer.produce(message, partition_value)

    def stop(self):
        """Stops the asynchronous producer safely. Ensures that all messages have been sent."""
        self.producer.stop()
