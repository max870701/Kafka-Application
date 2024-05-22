import json
from confluent_kafka import Consumer, KafkaError


def consume_messages(topic):
    conf = {
        'bootstrap.servers': 'localhost:29092',
        'group.id': 'group-1',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(conf)
    consumer.subscribe([topic])

    while True:
        # Retrieve a message in 1 second interval
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        print(f"Received message: {json.loads(msg.value().decode('utf-8'))}")

if __name__ == "__main__":
    # Subscription topic
    sub_topic = 'btc_price_topic'

    # Consume messages
    consume_messages(
        topic=sub_topic
    )
