import allure

from contracts.services.operations.operation_pb2 import Operation
from contracts.services.operations.rpc_get_operations_pb2 import GetOperationsResponse
from tests.assertions.base import assert_equal
from tests.clients.postgres.operations.model import OperationsTestModel
from tests.schema.operations import OperationEventTestSchema
from tests.tools.date import to_proto_test_datetime
from tests.tools.logger import get_test_logger
from tests.types.operations import StatusToProtobufMap, TypeToProtobufMap

logger = get_test_logger('OPERATIONS_ASSERTIONS')


@allure.step('Check operation from event')
def assert_operation_from_event(
        actual: Operation,
        expected: OperationEventTestSchema
) -> None:

    logger.info('Check operation from event')

    assert_equal(actual.type, TypeToProtobufMap[expected.type], 'type')
    assert_equal(actual.status, StatusToProtobufMap[expected.status], 'status')
    assert_equal(actual.amount, expected.amount, 'amount')
    assert_equal(actual.user_id, expected.user_id, 'user_id')
    assert_equal(actual.card_id, expected.card_id, 'card_id')
    assert_equal(actual.category, expected.category, 'category')
    assert_equal(actual.created_at, to_proto_test_datetime(expected.created_at), 'created_at')
    assert_equal(actual.account_id, expected.account_id, 'account_id')


@allure.step('Check operation from model')
def assert_operation_from_model(
        actual: Operation,
        expected: OperationsTestModel
) -> None:
    """
    Assertion for operation where expected data is obtained from DB.

    In this scenario, the operation id is a part of the contract and must meet the expected value.
    """
    logger.info('Check operation from model')

    assert_equal(actual.id, expected.id, 'id')
    assert_equal(actual.type, TypeToProtobufMap[expected.type], 'type')
    assert_equal(actual.status, StatusToProtobufMap[expected.status], 'status')
    assert_equal(actual.amount, expected.amount, 'amount')
    assert_equal(actual.user_id, expected.user_id, 'user_id')
    assert_equal(actual.card_id, expected.card_id, 'card_id')
    assert_equal(actual.category, expected.category, 'category')
    assert_equal(actual.created_at, to_proto_test_datetime(expected.created_at), 'created_at')
    assert_equal(actual.account_id, expected.account_id, 'account_id')


@allure.step('Check get operations response from events')
def assert_get_operations_response_from_events(
        actual: GetOperationsResponse,
        expected: list[OperationEventTestSchema]
) -> None:
    logger.info('Check get operations response from events')

    assert_equal(len(actual.operations), len(expected), 'operations count')
    for index, event in enumerate(expected):
        assert_operation_from_event(actual.operations[index], event)


@allure.step('Check get operations response from models')
def assert_get_operations_response_from_models(
        actual: GetOperationsResponse,
        expected: list[OperationsTestModel]
) -> None:
    logger.info('Check get operations response from models')

    assert_equal(len(actual.operations), len(expected), 'operations count')
    for index, model in enumerate(expected):
        assert_operation_from_model(actual.operations[index], model)
