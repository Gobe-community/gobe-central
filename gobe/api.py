from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import SignupSerializer, UserSerializer

#Signup APIView
class SignupAPI(generics.GenericAPIView):
    serializer_class = SignupSerializer

    #Post function
    def post(self, request, *args, **kwargs):
        #takes any request from the function parameter into the serializer variable
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response({
            "user": UserSerializer(user,
            context=self.get_serializer_context()).data,
            "message": "Welcome " + user.last_name
        })

#Get user API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user