from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer, MyTokenObtainPairSerializer

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)