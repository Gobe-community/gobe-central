from django.urls import path
from .views import UserListAPIView, UserDetailAPIView

# app_name = 'accounts'
urlpatterns = [
    path('users/', UserListAPIView().as_view()),
    path('users/<int:pk>', UserDetailAPIView().as_view()),

]