from datetime import datetime, timedelta


import pytest
from mixer.backend.django import mixer
from ..models import User
pytestmark = pytest.mark.django_db

class TestUser:

    def test_that_User_is_created(self):
        obj = mixer.blend('gobe.User')
        assert obj.pk == 1, 'Should create a User object'

    def test_User_has_profile(self):
        obj = User.objects.create_user(email="samkotlin@gmail.com", password='segtw766')
        assert obj.profile != None, 'Should Bind a profile object to User'
