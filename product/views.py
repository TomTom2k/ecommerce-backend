from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category, Event
from .serializer import ProductSerializer, ListProductSerializer, CategorySerializer, EventSerializer

# Create your views here.


@api_view(["GET"])
def getListProduct(request):
    if request.method == "GET":
        products = Product.objects.filter(
            is_active=True).order_by("-created_date")
        serializer = ListProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    if request.method == "GET":
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


@api_view(["GET"])
def getCategory(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def getEvent(request):
    if request.method == "GET":
        events = Event.objects.filter(is_active=True)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
