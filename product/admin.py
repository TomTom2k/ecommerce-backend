from django.contrib import admin
from .models import Product, Category, Event


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "sale", "is_active",
                    "created_date", "updated_date"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "start_time", "end_time"]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
