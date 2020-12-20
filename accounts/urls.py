from django.urls import path
from django.conf.urls import include

from rest_framework import routers
from rest_framework.routers import DefaultRouter

import accounts.views as acv

router = DefaultRouter(trailing_slash=False)
app_router = routers.DefaultRouter()

app_router.register('subscribe', acv.SubscribeUserToNewsLetter, basename='subscribe')

urlpatterns = [
    path('users/', include(app_router.urls))
]