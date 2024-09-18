from datetime import UTC

import factory
from pytest_factoryboy import register

from users.models import User


@register
class UserFactory(factory.django.DjangoModelFactory):
    last_name = factory.Faker('last_name')
    first_name = factory.Faker('first_name')
    phone_number = factory.Faker('phone_number')
    created_at = factory.Faker('date_time', tzinfo=UTC)
    email = factory.Faker('email')

    class Meta:
        model = User

    # class Params:
    #     words_ = factory.Faker('words', nb=2)
    #
    # @factory.lazy_attribute
    # def username(self):
    #     return '_'.join(self.words_)

    @factory.lazy_attribute
    def username(self):
        return '{}_{}'.format(self.first_name, self.last_name).lower()
