from pydantic import BaseModel, IPvAnyAddress


class KafkaClientTestConfig(BaseModel):
    """
    Kafka-client config in test environment
    Used for publishing events in event-driven test scenarios.
    """

    port: int = 9092
    address: IPvAnyAddress

    @property
    def bootstrap_servers(self) -> str:
        """
        Kafka-broker address, host:port.
        Used by Kafka-producers in tests.
        """
        return f'{self.address}:{self.port}'
