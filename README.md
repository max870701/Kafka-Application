# Kafka Service
[Pub/Sub service](https://medium.com/@chihsuan/introduction-to-apache-kafka-1cae693aa85e)
## Configuration
1. One zookeeper
2. One kafka broker
## Usage
1. Build up `docker-compose.yml` images and run in the background.

    ```bash
    docker compose up -d
    ```
2. Use `docker ps` to check the docker processes.
3. Publish a message to a topic.
    - In the same docker network: port 9092
    - Not in the same docker network: port 29092
4. Consume a message from a topic.
    - In the same docker network: port 9092
    - Not in the same docker network: port 29092
## Python Packages Installation
```bash
python -m pip install -r requirements.txt
```
## Python Examples
1. `publisher.py` used to send message to a topic.

    ```bash
    python publisher.py
    ```
2. `subscriber.py` used to receive message from a topic.

    ```bash
    python consumer.py
    ```