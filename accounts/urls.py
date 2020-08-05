from django.urls import path, include
# from .views import UserListAPIView, UserDetailAPIView
from .views import UserDetail, UserList, Register

# app_name = 'accounts'
urlpatterns = [
    # path('users/', UserListAPIView().as_view()),
    # path('users/<int:pk>', UserDetailAPIView().as_view()),
    path('register/', Register.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('auth/', include('rest_auth.urls')),
]