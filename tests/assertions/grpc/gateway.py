from datetime import date

import allure

from contracts.services.accounts.account_pb2 import Account, AccountStatus, AccountType
from contracts.services.cards.card_pb2 import Card, CardPaymentSystem, CardStatus, CardType
from contracts.services.gateway.account_details_pb2 import AccountDetails
from contracts.services.gateway.rpc_get_account_details_pb2 import GetAccountDetailsResponse
from contracts.services.gateway.rpc_get_user_details_pb2 import GetUserDetailsResponse
from contracts.services.gateway.user_details_pb2 import UserDetails
from contracts.services.users.user_pb2 import User
from tests.assertions.base import assert_equal
from tests.assertions.grpc.accounts import assert_account
from tests.assertions.grpc.cards import assert_card
from tests.assertions.grpc.users import assert_user
from tests.tools.date import to_proto_test_date
from tests.tools.logger import get_test_logger

logger = get_test_logger('GATEWAY_ASSERTIONS')


@allure.step('Check user details')
def assert_user_details(actual: UserDetails, expected: UserDetails) -> None:
    logger.info('Check user details')

    assert_user(actual.user, expected.user)

    assert_equal(len(actual.accounts), len(expected.accounts), 'accounts count')
    for index, account in enumerate(expected.accounts):
        assert_account(actual.accounts[index], account)


@allure.step('Check account details')
def assert_account_details(actual: AccountDetails, expected: AccountDetails) -> None:
    logger.info('Check account details')

    assert_account(actual.account, expected.account)

    assert_equal(len(actual.cards), len(expected.cards), 'cards count')
    for index, card in enumerate(expected.cards):
        assert_card(actual.cards[index], card)


@allure.step('Check get user details response')
def assert_get_user_details_response(
        actual: GetUserDetailsResponse,
        expected: GetUserDetailsResponse
) -> None:
    logger.info('Check get user details response')

    assert_user_details(actual.details, expected.details)


@allure.step('Check get account details response')
def assert_get_account_details_response(
        actual: GetAccountDetailsResponse,
        expected: GetAccountDetailsResponse
) -> None:
    logger.info('Check get account details response')

    assert_account_details(actual.details, expected.details)


@allure.step('Check get user details response. User with active credit card account')
def assert_get_user_details_response_user_with_active_credit_card_account(
        actual: GetUserDetailsResponse,
) -> None:
    logger.info('Check get user details response. User with active credit card account')

    expected = GetUserDetailsResponse(
        details=UserDetails(
            user=User(
                id='8b0e7c2a-1b6a-4e5d-9f1a-1b3f2a7c9e21',
                email='john.doe@example.com',
                last_name='Doe',
                first_name='John',
                middle_name='White',
                phone_number='+1111111111',
            ),
            accounts=[
                Account(
                    id='99999999-aaaa-4bbb-8ccc-000000000001',
                    type=AccountType.ACCOUNT_TYPE_CREDIT_CARD,
                    status=AccountStatus.ACCOUNT_STATUS_ACTIVE,
                    user_id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                    balance=-15230.75,
                )
            ],
        )
    )
    assert_get_user_details_response(actual, expected)


@allure.step('Check get account details response. User with active debit card account')
def assert_get_account_details_response_user_with_active_debit_card_account(
        actual: GetAccountDetailsResponse,
) -> None:
    logger.info('Check get account details response. User with active debit card account')

    expected = GetAccountDetailsResponse(
        details=AccountDetails(
            account=Account(
                id='bbaf6357-177c-416c-8096-3d06937157a8',
                type=AccountType.ACCOUNT_TYPE_DEBIT_CARD,
                status=AccountStatus.ACCOUNT_STATUS_ACTIVE,
                user_id='e56fcbd4-dc23-4e20-95eb-922ab8886143',
                balance=-15230.75,
            ),
            cards=[
                Card(
                    id='9441d479-ac30-4ea6-a469-e3db8dcc0ea9',
                    pin='3333',
                    cvv='987',
                    type=CardType.CARD_TYPE_VIRTUAL,
                    status=CardStatus.CARD_STATUS_ACTIVE,
                    account_id='bbaf6357-177c-416c-8096-3d06937157a8',
                    card_number='5555111111111111',
                    card_holder='MARK SMITH',
                    expiry_date=to_proto_test_date(date(2029, 9, 30)),
                    payment_system=CardPaymentSystem.CARD_PAYMENT_SYSTEM_VISA,
                ),
                Card(
                    id='dda95f49-01a1-44e8-a955-fddd7de4efda',
                    pin='8888',
                    cvv='654',
                    type=CardType.CARD_TYPE_PHYSICAL,
                    status=CardStatus.CARD_STATUS_ACTIVE,
                    account_id='bbaf6357-177c-416c-8096-3d06937157a8',
                    card_number='7777000000000004',
                    card_holder='MARK SMITH',
                    expiry_date=to_proto_test_date(date(2030, 1, 31)),
                    payment_system=CardPaymentSystem.CARD_PAYMENT_SYSTEM_MASTERCARD,
                ),
            ],
        )
    )
    assert_get_account_details_response(actual, expected)
