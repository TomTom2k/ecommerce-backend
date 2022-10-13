from ast import Or
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, OrderSerializer, OrderDetailSerializer
from .models import Order, OrderDetail, User
from product.models import Product


# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getUser(request, user):
    if request.method == "GET":
        user = User.objects.get(username=user)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def createUser(request):
    if request.method == "GET":
        return Response("Get success")

    if request.method == "POST":
        data = request.data
        user = User.objects.create_user(
            username=data['username'],
            phone_number=data['phone_number'],
            email=data['email'],
            password=data['password']
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


@api_view(["GET", "POST"])
def getOrder(request, user):
    client = User.objects.get(username=user)
    if request.method == "GET":
        orders = Order.objects.filter(user=client.id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        data = request.data
        order = Order.objects.create(
            user=client,
            address=data['address'],
        )

        for orderDetail in data['orderDetails']:
            product = Product.objects.get(id=orderDetail['product'])
            orderDetail = OrderDetail.objects.create(
                product=product,
                order=order,
                amount=orderDetail['amount']
            )

        return Response("create order success")


@api_view(["GET", "POST"])
def getOrderDetail(request, user, id):
    order = Order.objects.get(id=id)
    if request.method == "GET":
        ordersDetail = OrderDetail.objects.filter(order=order.id)
        serializer = OrderDetailSerializer(ordersDetail, many=True)
        return Response(serializer.data)
