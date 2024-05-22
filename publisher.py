import requests
import json
import time
from typing import Dict, Optional
from confluent_kafka import Producer


def get_binance_btc_price(symbol: str) -> Optional[Dict]:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.text}")
        return None

def send_to_kafka(topic: str, message: Dict) -> None:
    conf = {
        'bootstrap.servers': 'localhost:29092',
        'security.protocol': 'PLAINTEXT'
        }
    producer = Producer(conf)
    producer.produce(topic, json.dumps(message))
    producer.flush()

if __name__ == "__main__":
    # Set a topic name
    pub_topic = 'btc_price_topic'

    while True:
        # Fetch the BTCUSDT ticker
        btc_price = get_binance_btc_price(
            symbol='BTCUSDT'
        )

        # Send the Kafka topic ticker data
        if btc_price:
            print('Sending the Ticker data ...')
            send_to_kafka(
                topic=pub_topic,
                message=btc_price
            )

        # Rate limit
        time.sleep(0.1)
