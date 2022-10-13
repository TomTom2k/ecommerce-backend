from rest_framework.serializers import ModelSerializer
from .models import Product, Category, Event


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ListProductSerializer(ModelSerializer):
    query = Category.objects.all()
    category = CategorySerializer(query, many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "image", "price", "category", "sale"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
