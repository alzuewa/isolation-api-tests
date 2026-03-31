from pydantic import BaseModel

from tests.schema.accounts import AccountTestSchema
from tests.schema.cards import CardTestSchema
from tests.schema.users import UserTestSchema


class AccountDetailsTestSchema(BaseModel):
    cards: list[CardTestSchema]
    account: AccountTestSchema


class GetAccountDetailsResponseTestSchema(BaseModel):
    details: AccountDetailsTestSchema


class UserDetailsTestSchema(BaseModel):
    user: UserTestSchema
    accounts: list[AccountTestSchema]


class GetUserDetailsResponseTestSchema(BaseModel):
    details: UserDetailsTestSchema
