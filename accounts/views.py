from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from .models import User
from .serializers import UserSerializer

# Create your views here.
@csrf_exempt
class UserListAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
class UserDetailAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, pk, format=None):

        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    def put(self, request, pk, format=None):

        user = get_object_or_404(User, id=pk)
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    def delete(self, request, pk, format=None):

        user = get_object_or_404(User, id=pk)
        user.delete()
        return HttpResponse(status=204)
        

