from datetime import date

import allure

from tests.assertions.base import assert_equal
from tests.assertions.http.accounts import assert_account
from tests.assertions.http.cards import assert_card
from tests.assertions.http.users import assert_user
from tests.schema.accounts import AccountTestSchema
from tests.schema.cards import CardTestSchema
from tests.schema.gateway import (
    UserDetailsTestSchema,
    AccountDetailsTestSchema,
    GetUserDetailsResponseTestSchema,
    GetAccountDetailsResponseTestSchema
)
from tests.schema.users import UserTestSchema
from tests.tools.logger import get_test_logger
from tests.types.accounts import AccountTestType, AccountTestStatus
from tests.types.cards import CardTestPaymentSystem, CardTestStatus, CardTestType

logger = get_test_logger('GATEWAY_ASSERTIONS')


@allure.step('Check user details')
def assert_user_details(actual: UserDetailsTestSchema, expected: UserDetailsTestSchema) -> None:
    logger.info('Check user details')

    assert_user(actual.user, expected.user)

    assert_equal(len(actual.accounts), len(expected.accounts), 'accounts count')
    for index, account in enumerate(expected.accounts):
        assert_account(actual.accounts[index], account)


@allure.step('Check account details')
def assert_account_details(actual: AccountDetailsTestSchema, expected: AccountDetailsTestSchema) -> None:
    logger.info('Check account details')

    assert_account(actual.account, expected.account)

    assert_equal(len(actual.cards), len(expected.cards), 'cards count')
    for index, card in enumerate(expected.cards):
        assert_card(actual.cards[index], card)


@allure.step('Check get user details response')
def assert_get_user_details_response(
        actual: GetUserDetailsResponseTestSchema,
        expected: GetUserDetailsResponseTestSchema
) -> None:
    logger.info('Check get user details response')

    assert_user_details(actual.details, expected.details)


@allure.step('Check get account details response')
def assert_get_account_details_response(
        actual: GetAccountDetailsResponseTestSchema,
        expected: GetAccountDetailsResponseTestSchema
) -> None:
    logger.info('Check get account details response')

    assert_account_details(actual.details, expected.details)


@allure.step('Check get user details response. User with active credit card account')
def assert_get_user_details_response_user_with_active_credit_card_account(
        actual: GetUserDetailsResponseTestSchema,
) -> None:
    logger.info('Check get user details response. User with active credit card account')

    expected = GetUserDetailsResponseTestSchema(
        details=UserDetailsTestSchema(
            user=UserTestSchema(
                id='8b0e7c2a-1b6a-4e5d-9f1a-1b3f2a7c9e21',
                email='john.doe@example.com',
                last_name='Doe',
                first_name='John',
                middle_name='White',
                phone_number='+1111111111',
            ),
            accounts=[
                AccountTestSchema(
                    id='99999999-aaaa-4bbb-8ccc-000000000001',
                    type=AccountTestType.CREDIT_CARD,
                    status=AccountTestStatus.ACTIVE,
                    user_id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
                    balance=-15230.75,
                )
            ],
        )
    )
    assert_get_user_details_response(actual, expected)


@allure.step('Check get account details response. User with active debit card account')
def assert_get_account_details_response_user_with_active_debit_card_account(
        actual: GetAccountDetailsResponseTestSchema,
) -> None:
    logger.info('Check get account details response. User with active debit card account')

    expected = GetAccountDetailsResponseTestSchema(
        details=AccountDetailsTestSchema(
            account=AccountTestSchema(
                id='bbaf6357-177c-416c-8096-3d06937157a8',
                type=AccountTestType.DEBIT_CARD,
                status=AccountTestStatus.ACTIVE,
                user_id='e56fcbd4-dc23-4e20-95eb-922ab8886143',
                balance=-15230.75,
            ),
            cards=[
                CardTestSchema(
                    id='9441d479-ac30-4ea6-a469-e3db8dcc0ea9',
                    pin='3333',
                    cvv='987',
                    type=CardTestType.VIRTUAL,
                    status=CardTestStatus.ACTIVE,
                    account_id='bbaf6357-177c-416c-8096-3d06937157a8',
                    card_number='5555111111111111',
                    card_holder='MARK SMITH',
                    expiry_date=date(2029, 9, 30),
                    payment_system=CardTestPaymentSystem.VISA,
                ),
                CardTestSchema(
                    id='dda95f49-01a1-44e8-a955-fddd7de4efda',
                    pin='8888',
                    cvv='654',
                    type=CardTestType.PHYSICAL,
                    status=CardTestStatus.ACTIVE,
                    account_id='bbaf6357-177c-416c-8096-3d06937157a8',
                    card_number='7777000000000004',
                    card_holder='MARK SMITH',
                    expiry_date=date(2030, 1, 31),
                    payment_system=CardTestPaymentSystem.MASTERCARD,
                ),
            ],
        )
    )
    assert_get_account_details_response(actual, expected)