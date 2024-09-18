import pytest

from users.tests.factories import UserFactory


@pytest.fixture
def users():
    UserFactory.create_batch(20)