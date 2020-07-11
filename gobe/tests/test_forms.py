from .. import forms

class TestSignUpForm:

    def test_empty_data_is_invalid(self):
        form = forms.SignUpForm(data={})
        assert form.is_valid() == False, 'Should be invalid if no data given'


    def test_that_email_is_required(self):
        form = forms.SignUpForm(data={'email': None})
        assert form.is_valid() == False, 'Should be invalid if no email given'
        assert 'email' in form.errors, 'Should have email field in error'

