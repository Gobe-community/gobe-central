from django.urls import path
# from .views import UserListAPIView, UserDetailAPIView
from .views import UserDetail, UserList
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Accounts API')
# app_name = 'accounts'
urlpatterns = [
    # path('users/', UserListAPIView().as_view()),
    # path('users/<int:pk>', UserDetailAPIView().as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('swagger-docs/', schema_view),

]