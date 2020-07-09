from datetime import datetime, timedelta


import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestUser:

    def test_model(self):
        obj = mixer.blend('gobe.User')
        assert obj.pk == 1, 'Should create a User object'