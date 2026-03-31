from pydantic import ConfigDict, UUID4, BaseModel
from pydantic.alias_generators import to_camel

from tests.types.accounts import AccountTestType, AccountTestStatus


class AccountTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    id: UUID4
    type: AccountTestType
    status: AccountTestStatus
    user_id: UUID4
    balance: float


class GetAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema


class GetAccountsResponseTestSchema(BaseModel):
    accounts: list[AccountTestSchema]
