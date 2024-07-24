from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer, MyTokenObtainPairSerializer
from .models import Product, Category, Order
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated

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
    
    
    



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderHistoryAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # To Ensure only authenticated users can access this

    def get_queryset(self):
        user = self.request.user
        #print(f"Authenticated user: {user}, ID: {user.id}")  
        return Order.objects.filter(user=user)