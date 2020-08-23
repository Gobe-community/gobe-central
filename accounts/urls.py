from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserGenericViewSet, ProfileGenericViewSet

router = DefaultRouter()
router.register('accounts', UserGenericViewSet)
router.register('accounts/profiles', ProfileGenericViewSet)

# app_name = 'accounts'
urlpatterns = [

    path('v1/', include(router.urls)),
    
]