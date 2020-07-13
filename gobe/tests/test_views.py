from django.test import RequestFactory

from .. import views, models

class TestSignUpView:

    def test_signup_page_loads(self):
        req = RequestFactory().get('signup/')
        resp = views.SignUpView.as_view()(req)

        assert resp.status_code == 200, 'Should be callable by anyone'

    def test_home_page_loads(self):
        req = RequestFactory().get('home/')
        resp = views.HomeView.as_view()(req)

        assert resp.status_code == 200, 'Should be callable by anyone'