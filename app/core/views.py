from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer, MyTokenObtainPairSerializer
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
    
    
    


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer