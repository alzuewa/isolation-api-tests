import uuid
from datetime import datetime

from faker import Faker
from faker.providers.python import TEnum


class Fake:

    def __init__(self, faker: Faker):
        self.faker = faker

    def uuid(self) -> uuid.UUID:
        return self.faker.uuid4(cast_to=None)

    def enum(self, value: type[TEnum]) -> TEnum:
        return self.faker.enum(value)

    def category(self) -> str:
        return self.faker.random_element([
            'gas',
            'taxi',
            'tolls',
            'water',
            'beauty',
            'mobile',
            'travel',
            'parking',
            'catalog',
            'internet',
            'satellite',
            'education',
            'government',
            'healthcare',
            'restaurants',
            'electricity',
            'supermarkets',
        ])

    def float(self, start: int = 1, end: int = 100) -> float:
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        return self.float(1, 1000)

    def date_time(self) -> datetime:
        return self.faker.date_time()


fake = Fake(faker=Faker())
