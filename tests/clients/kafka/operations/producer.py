import time

import allure

from tests.clients.kafka.producer import KafkaProducerTestClient
from tests.config import test_settings
from tests.schema.operations import OperationEventTestSchema
from tests.tools.logger import get_test_logger
from tests.types.operations import OperationTestType, OperationTestStatus


class OperationsKafkaProducerTestClient(KafkaProducerTestClient):

    @allure.step('Produce operation event')
    def produce_operation_event_api(
            self,
            event: OperationEventTestSchema,
    ) -> OperationEventTestSchema:
        """
        Publish operation event to Kafka.

        - sends event to a specific topic;
        - guarantees message delivery;
        - waits for message processing to be finished on a server side.

        Returns an event itself so that tests can use it as an expected data model.
        """
        self.produce(
            topic='operations-service.operation-event.inbox',
            value=event.model_dump_json(),
        )

        # Guarantee that message was sent to Kafka.
        self.flush_all()
        
        time.sleep(test_settings.operations_processing_wait_timeout)

        return event

    @allure.step('Produce in-progress purchase operation event')
    def produce_in_progress_purchase_operation_event(self) -> OperationEventTestSchema:
        """
        Publish purchase operation event with IN_PROGRESS status.
        """
        return self.produce_operation_event_api(
            OperationEventTestSchema(
                type=OperationTestType.PURCHASE,
                status=OperationTestStatus.IN_PROGRESS
            )
        )

    @allure.step('Produce completed purchase operation event')
    def produce_completed_purchase_operation_event(self) -> OperationEventTestSchema:
        """
        Publish purchase operation event with COMPLETED status.
        """
        return self.produce_operation_event_api(
            OperationEventTestSchema(
                type=OperationTestType.PURCHASE,
                status=OperationTestStatus.COMPLETED
            )
        )


def build_operations_kafka_producer_test_client() -> OperationsKafkaProducerTestClient:
    return OperationsKafkaProducerTestClient(
        config=test_settings.operations_kafka_client,
        logger=get_test_logger('OPERATIONS_KAFKA_PRODUCER_TEST_CLIENT')
    )
