from django.urls import path
from . import views

urlpatterns = [
    path('', views.getListProduct),
    path('<int:pk>/', views.getProduct),
    path('category/', views.getCategory),
    path('event/', views.getEvent),
]
