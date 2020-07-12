from rest_framework import generics, permissions
from rest_framework.responses import Response
from .serializers import SignupSerializer, UserSerializer

#Signup APIView
class SignupAPI(generics.GenericAPI):
    serializer_class = RegisterSerializer

    #Post function
    def post(self, request, *args, **kwargs):
        #takes any request from the function parameter into the serializer variable
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response({
            "user": 
        })