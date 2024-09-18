import pytest
from django.urls import reverse_lazy


@pytest.mark.django_db
class TestView:
    def test_user_list(self, client, users):
        url = reverse_lazy('user-list')
