import logging

import allure
from confluent_kafka import Producer

from tests.tools.config.kafka import KafkaClientTestConfig


class KafkaProducerTestClient:

    def __init__(
        self,
        config: KafkaClientTestConfig,
        logger: logging.Logger,
    ):
        self.logger = logger
        self.producer = Producer({'bootstrap.servers': config.bootstrap_servers})

    @allure.step('Produce message to topic {topic}')
    def produce(self, topic: str, value: str | bytes):
        try:
            self.producer.produce(topic, value)

            # poll(0) allows to handle internal producer's events:
            # messages acks, errors, etc.
            self.producer.poll(0)

            self.logger.info(f'Kafka message produced to {topic}')
        except Exception as error:
            self.logger.exception(f'Kafka produce failed {topic}:{error}')
            raise

    @allure.step('Flush all messages')
    def flush_all(self, timeout: float = 10.0):
        """
        Mandatory expectation for all the messages to be sent.

        Used in tests requiring all the events to be delivered to Kafka
        before next steps execution (e.g. invoking API-calls).
        """
        self.logger.info('Kafka producer flush started')
        self.producer.flush(timeout=timeout)
        self.logger.info('Kafka producer flush finished')
