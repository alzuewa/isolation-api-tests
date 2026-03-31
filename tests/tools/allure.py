from enum import StrEnum


class AllureTag(StrEnum):
    GRPC = 'GRPC'
    HTTP = 'HTTP'
    KAFKA = 'KAFKA'
    POSTGRES = 'POSTGRES'

    GATEWAY_SERVICE = 'GATEWAY_SERVICE'
    OPERATIONS_SERVICE = 'OPERATIONS_SERVICE'


class AllureStory(StrEnum):
    OPERATION_EVENTS = 'Operation Events'
    OPERATION_FILTERS = 'Operation Filters'

    GET_USER_DETAILS = 'Get User Details'
    GET_ACCOUNT_DETAILS = 'Get Account Details'


class AllureFeature(StrEnum):
    GATEWAY_SERVICE = 'Gateway Service'
    OPERATIONS_SERVICE = 'Operations Service'
