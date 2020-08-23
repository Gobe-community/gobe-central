from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins

from .models import User
from .serializers import UserSerializer, ProfileSerializer


class UserGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
                        mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProfileGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
                        mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = ProfileSerializer
    queryset = User.objects.all()