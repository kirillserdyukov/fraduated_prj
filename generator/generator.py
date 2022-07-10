import random

from data.data import Person
from faker import Faker

faker_en = Faker("ru_RU")
Faker.seed()


def person_generator():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        age=random.randint(10, 80),
        salary=random.randint(5000, 10000),
        department=faker_en.job(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
    )