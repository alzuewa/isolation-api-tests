from pydantic_settings import BaseSettings, SettingsConfigDict

from tests.tools.config.grpc import GRPCClientTestConfig, GRPCServerTestConfig
from tests.tools.config.http import HTTPClientTestConfig, HTTPServerTestConfig
from tests.tools.config.kafka import KafkaClientTestConfig
from tests.tools.config.postgres import PostgresClientTestConfig


class TestSettings(BaseSettings):
    """
    Root test environment configuration.
    Aimed to be a single entry point for all the settings used in tests and clients.
    """

    model_config = SettingsConfigDict(
        extra='allow',
        env_file='./tests/.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.',
    )

    mock_http_server: HTTPServerTestConfig
    mock_grpc_server: GRPCServerTestConfig

    operations_postgres_client: PostgresClientTestConfig

    gateway_http_client: HTTPClientTestConfig
    gateway_grpc_client: GRPCClientTestConfig

    operations_http_client: HTTPClientTestConfig
    operations_grpc_client: GRPCClientTestConfig
    operations_kafka_client: KafkaClientTestConfig

    operations_processing_wait_timeout: float
    """
    Timeout for async operations processing.

    Used in event-driven tests to wait for event processing is finished
    before synchronous test-checks.
    """


test_settings = TestSettings()
