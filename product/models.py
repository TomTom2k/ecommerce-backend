from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date

# Create your models here.


class Product(models.Model):
    class Meta:
        ordering = ['is_active', '-created_date', 'name']

    name = models.CharField(("Tên bánh"), max_length=255)
    image = models.ImageField(("Ản sản phẩm"), upload_to="images/%Y/%m/%d")
    price = models.IntegerField(("Đơn giá"))
    category = models.ManyToManyField(("category"), default=None)
    ingredient = models.CharField(
        ("Các nguyên liệu"), max_length=255, default="Đang cập nhật")
    describe = models.TextField(default="Đang cập nhật")
    sale = models.FloatField(("Mức giảm giá"), default=0, validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sản phẩm"
        verbose_name_plural = "danh sách sản phẩm"


class Category(models.Model):
    name = models.CharField(("Tên"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "loại"
        verbose_name_plural = "danh sách loại"


class Event(models.Model):
    name = models.CharField(("Tên sự kiện"), max_length=255)
    image = models.ImageField(("ảnh sự kiện"), upload_to="images/%Y/%m/%d")
    start_time = models.DateField(("Ngày bắt đầu"), default=date.today())
    end_time = models.DateField(("Ngày kết thúc"), default=date.today())
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "sự kiện"
        verbose_name_plural = "danh sách sự kiện"
