from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .forms import SignUpForm

#Create your views here
class HomeView(View):
    """
    Handles request for home directory
    """

    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)

class SignUpView(View):
    """Handles requests for sign up page"""


    template_name = 'signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
        
            

