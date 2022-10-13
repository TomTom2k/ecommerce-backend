from rest_framework.serializers import ModelSerializer, SerializerMethodField
from product.models import Product

from product.serializer import ProductSerializer, ListProductSerializer
from .models import User, Order, OrderDetail


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone_number",
                  "is_active", "is_staff"]


class OrderDetailSerializer(ModelSerializer):
    queryProduct = Product.objects.all()
    product = ProductSerializer(queryProduct, many=False)

    class Meta:
        model = OrderDetail
        fields = ['product', 'amount']


class OrderSerializer(ModelSerializer):

    orderDetails = SerializerMethodField('get_orderDetails')

    class Meta:
        model = Order
        fields = ["id", "user", "address", "orderDetails"]

    def get_orderDetails(self, obj):
        queryOrderDetail = OrderDetail.objects.all()
        orderDetails = OrderDetailSerializer(queryOrderDetail, many=True)
        return orderDetails.data
