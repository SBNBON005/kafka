from kafka.topics.schemas.user import USER_TYPE_SCHEMA 

TOPIC_INFO = {
    'user': {
        'event_schemas': USER_TYPE_SCHEMA,
        'partition_key': '',
    },
}

def get_topics():
    return TOPIC_INFO.keys()

def get_topic_info(topic):
    try:
        topic_info = TOPIC_INFO[topic]
    except KeyError:
        raise KeyError('Topic {0} not found'.format(topic))
    return topic_info
    

def get_event_schema(topic, event_type):
    topic_info = get_topic_info(topic)
    topic_schema = topic_info['event_schemas']
    try:
        schema = topic_schema[event_type]
    except KeyError:
        raise SchemaNotFound('Event {0} not found on topic {1}'.format(
            event_type, topic))
    return schema()

def get_partition_key(topic):
    topic_info = get_topic_info(topic)
    return topic_info.get('partition_key')


