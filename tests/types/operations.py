from enum import StrEnum

from contracts.services.operations.operation_pb2 import OperationStatus, OperationType


class OperationTestType(StrEnum):
    FEE = 'FEE'
    TOP_UP = 'TOP_UP'
    PURCHASE = 'PURCHASE'
    CASHBACK = 'CASHBACK'
    TRANSFER = 'TRANSFER'
    REVERSAL = 'REVERSAL'
    UNSPECIFIED = 'UNSPECIFIED'
    BILL_PAYMENT = 'BILL_PAYMENT'
    CASH_WITHDRAWAL = 'CASH_WITHDRAWAL'


class OperationTestStatus(StrEnum):
    FAILED = 'FAILED'
    REVERSED = 'REVERSED'
    COMPLETED = 'COMPLETED'
    IN_PROGRESS = 'IN_PROGRESS'
    UNSPECIFIED = 'UNSPECIFIED'


TypeToProtobufMap = {
    OperationTestType.FEE: OperationType.OPERATION_TYPE_FEE,
    OperationTestType.TOP_UP: OperationType.OPERATION_TYPE_TOP_UP,
    OperationTestType.PURCHASE: OperationType.OPERATION_TYPE_PURCHASE,
    OperationTestType.CASHBACK: OperationType.OPERATION_TYPE_CASHBACK,
    OperationTestType.TRANSFER: OperationType.OPERATION_TYPE_TRANSFER,
    OperationTestType.REVERSAL: OperationType.OPERATION_TYPE_REVERSAL,
    OperationTestType.UNSPECIFIED: OperationType.OPERATION_TYPE_UNSPECIFIED,
    OperationTestType.BILL_PAYMENT: OperationType.OPERATION_TYPE_BILL_PAYMENT,
    OperationTestType.CASH_WITHDRAWAL: OperationType.OPERATION_TYPE_CASH_WITHDRAWAL,
}

StatusToProtobufMap = {
    OperationTestStatus.FAILED: OperationStatus.OPERATION_STATUS_FAILED,
    OperationTestStatus.REVERSED: OperationStatus.OPERATION_STATUS_REVERSED,
    OperationTestStatus.COMPLETED: OperationStatus.OPERATION_STATUS_COMPLETED,
    OperationTestStatus.IN_PROGRESS: OperationStatus.OPERATION_STATUS_IN_PROGRESS,
    OperationTestStatus.UNSPECIFIED: OperationStatus.OPERATION_STATUS_UNSPECIFIED,
}
