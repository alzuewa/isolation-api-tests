from datetime import date

from pydantic import UUID4, ConfigDict, BaseModel
from pydantic.alias_generators import to_camel

from tests.types.cards import (
    CardTestType,
    CardTestStatus,
    CardTestPaymentSystem,
)


class CardTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    id: UUID4
    pin: str
    cvv: str
    type: CardTestType
    status: CardTestStatus
    account_id: UUID4
    card_number: str
    card_holder: str
    expiry_date: date
    payment_system: CardTestPaymentSystem


class GetCardResponseTestSchema(BaseModel):
    card: CardTestSchema


class GetCardsQueryTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    account_id: UUID4


class GetCardsResponseTestSchema(BaseModel):
    cards: list[CardTestSchema]
