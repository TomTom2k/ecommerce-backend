from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator

# Create your models here.

username_validator = UnicodeUsernameValidator()


def only_int(value):
    if value.isdigit() == False:
        raise ValidationError('ID contains characters')


class User(AbstractUser):
    username = models.CharField(
        ("Tài khoản"),
        max_length=150,
        unique=True,
        help_text=("Yêu cầu 150 ký tự hoặc ít hơn. Ký tự, số và chỉ @/./+/-/_"),
        validators=[username_validator],
        error_messages={
            "unique": ("Tài khoản người dùng đã tồn tại."),
        },
    )
    email = models.EmailField(("Địa chỉ email"), unique=True)
    phone_number = models.CharField(
        ("Số điện thoại"), max_length=10, blank=True, validators=[only_int, MinLengthValidator(10)])
    is_active = models.BooleanField(
        ("Hoạt động"),
        default=True,
        help_text=(
            "Chỉ định xem người dùng này có nên được coi là đang hoạt động hay không. "
            "Bỏ chọn mục này thay vì xóa tài khoản."
        ),
    )
    is_staff = models.BooleanField(
        ("Nhân viên"), default=False, help_text=("Có thể đăng nhập vào trang quản lý")
    )
    is_superuser = models.BooleanField(("Quản trị viên"), default=False)
    date_joined = models.DateTimeField(
        ("ngày tham gia"), default=timezone.now())

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "khách hàng"
        verbose_name_plural = "danh sách khách hàng"


class Order(models.Model):
    user = models.ForeignKey(
        "User", verbose_name=("Khách hàng"), on_delete=models.CASCADE)
    address = models.CharField(("đia chỉ"), max_length=255)
    status = models.IntegerField(("Trạng thái đơn hàng"), help_text=(
        "0: Chờ xác nhận, 1: Đang giao:, 2:Đã giao, -1: Giao hàng thất bại"), default=0)
    created_date = models.DateTimeField(
        ("ngày xuất hóa đơn"), auto_now_add=True)
    product = models.ManyToManyField(
        "product.Product", verbose_name=("Chi tiết sản phẩm"), through='OrderDetail')

    def __str__(self):
        return self.user.username + " " + self.address

    @property
    def orderDetails(self):
        return self.objects.all()

    class Meta:
        verbose_name = "hóa đơn"
        verbose_name_plural = "danh sách hóa đơn"


class OrderDetail(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=(
        "Sản phẩm"), on_delete=models.CASCADE)
    order = models.ForeignKey(
        "Order", verbose_name=("Đơn hàng"), on_delete=models.CASCADE)
    amount = models.IntegerField(("Số sản phẩm"), default=1)

    def __str__(self):
        return self.product.name + " " + str(self.amount)

    class Meta:
        verbose_name = "chi tiết hóa đơn"
        verbose_name_plural = "danh sách chi tiết hóa đơn"
