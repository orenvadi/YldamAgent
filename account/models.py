from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# from pkg_resources import _

ROLES = (
    ("Administrator", "Administrator"),
    ("Producer", "Producer"),
    ("Store Owner", "Store Owner"),
    ("Store Manager", "Store Manager"),
)


class CustomUser(AbstractUser):
    status = models.CharField(choices=ROLES, max_length=100)
    email = models.EmailField(
        unique=True,
        error_messages='"unique": _("A user with that email already exists.")',
        blank=True,
        default="None",
    )
    can_add_orders = models.BooleanField(default=False)

    class Meta:
        swappable = "AUTH_USER_MODEL"

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]


class CustomUserManager(
    BaseUserManager
):  # Is used to make a function that allows to add administrators straightly in the web-site
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(username, password, **extra_fields)


class Store(models.Model):  # Store-Owners can add their stores into this table
    TIN = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{10,}$",  # Exactly 10 digits, not more not less
                message="The field should contain exactly 10 digits",
                code="invalid_data",
            )
        ],
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class StoreManager(
    models.Model
):  # The Store Managers may be signed up by Store Owners to help them to make orders
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )


class Administrator(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )


class StoreOwner(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )


class ProductCategory(models.Model):
    title = models.CharField(max_length=100)


class ProductType(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Producer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    TIN = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^\d{10,}$",  # Exactly 10 digits, not more not less
                message="The field should contain exactly 10 digits",
                code="invalid_data",
            )
        ],
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+996\d+$",  # Phone Number (Only Kyrgyzstan)
                message="Phone Number",
                code="invalid_data",
            )
        ],
    )
    product = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
