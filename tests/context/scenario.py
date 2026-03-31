from enum import StrEnum


class Scenario(StrEnum):
    """
    Passed as a header in requests to gateway-service.
    
    Mock-server uses the header as a key to chose specific mock-data.
    """
    USER_WITH_ACTIVE_DEBIT_CARD_ACCOUNT = 'user_with_active_debit_card_account'
    USER_WITH_ACTIVE_CREDIT_CARD_ACCOUNT = 'user_with_active_credit_card_account'
