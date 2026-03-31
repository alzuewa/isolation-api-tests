from datetime import datetime, date


def to_proto_test_date(value: date) -> str:
    """
    Used in protobuf-contracts
    """
    return value.strftime('%Y-%m-%d')


def to_proto_test_datetime(value: datetime) -> str:
    """
    Used in protobuf-contracts
    """
    return value.strftime('%Y-%m-%d %H:%M:%S')
