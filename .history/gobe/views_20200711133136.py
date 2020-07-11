from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm

#Create your views here
def home(request):
    """
    Handles request for home directory
    """

    return render(request, 'base.html')


def signup(request):
    """Handles requests for sign up page"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

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
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                return render(request, 'login.html', {'message': "Invalid username or password."})
        else:
            return redirect(request, 'login.html', {'message': "Invalid username or password."})
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context = {"form":form})