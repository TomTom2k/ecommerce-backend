from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Order, OrderDetail


class UserAdmin(admin.ModelAdmin):
    fields = ["username", "email", "password", "phone_number",
              "is_active", "is_staff", "is_superuser", "date_joined"]
    list_display = ["id", "username", "email", "is_active", "date_joined"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "address", "status"]


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "amount"]
# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
