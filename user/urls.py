from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.createUser),
    path('<str:user>/', views.getUser),
    path('<str:user>/order/', views.getOrder),
    path('<str:user>/order/<int:id>/order-detail/', views.getOrderDetail),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
