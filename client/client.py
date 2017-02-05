import pykafka
import logging
from kafka.topics import topic_registry
from kafka.producer import BongzKafkaProducer
from IPython import embed

class BongzKafkaClient(object):
    def __init__(self, brokers, zookeeper_hosts):
        if not isinstance(brokers, (basestring, list)):
            raise TypeError("Brokers must be string or list - got {0}".format(brokers))
        if not isinstance(zookeeper_hosts, (basestring, list)):
            raise TypeError("Zookeeper hosts must be string or list - got {0}".format(zookeeper_hosts))
        self.kafka_client = pykafka.KafkaClient(hosts=brokers)
        self.zookeeper_hosts = zookeeper_hosts

    def get_producer(self, topic=None, event_type, block_on_queue_full=True, required_acks=None, max_retries=3):

        topic = self.validate_topic(topic)

        kwargs = {
            'block_on_queue_full': block_on_queue_full,
            'max_retries': max_retries
        }
        if required_acks is not None:
            kwargs['required_acks'] = required_acks

        pykafka_producer = self.kafka_client.topics[topic].get_producer(partitioner=partitioner, **kwargs)
        bongz_producer = BongzKafkaProducer(pykafka_producer, topic)
        return bongz_producer

    @staticmethod
    def validate_topic(topic):
        """Ensure that a topic exists and is correctly encoded

        Args:
            topic (str or unicode): Topic name.

        Returns:
            str: UTF-8 encoded topic if `topic` is valid.

        Raises:
            KeyError: If `topic` is not a valid topic.
        """
        if isinstance(topic, unicode):
            topic = topic.encode('utf-8')
        if topic not in topic_registry.get_topics():
            raise KeyError("Topic not found - got {0}".format(topic))
        return topic
