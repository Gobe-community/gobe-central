from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
            return redirect('home')
        
            

def login_view(request):
    """Handles request for log in page"""
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'message': "Invalid username or password."})
        else:
            return render(request, 'login.html', {'message': "Invalid username or password."})
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context = {"form":form})