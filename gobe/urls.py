from django.urls import path
from . import views
from .api import SignupAPI

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('api/signup', SignupAPI.as_view(), name='signup_view'),
]