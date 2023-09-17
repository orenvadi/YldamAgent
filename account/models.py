from django.core.validators import RegexValidator
from django.db import models


ROLES = (
    ("Administrator", "Administrator"),
    ("Producer", "Producer"),
    ("Store Owner", "Store Owner"),
    ("Store Manager", "Store Manager"),
)


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


class StoreManager(models.Model):  # The Store Managers may be signed up by Store Owners to help them to make orders
    username = models.CharField(
        max_length=100,
        unique=True,
        error_messages={None: 'A user with that username already exists.'},
        blank=True, default='AnonymousProducer'
    )
    email = models.EmailField(
        unique=True,
        error_messages={None: 'A user with that email already exists.'},
        blank=True,
        default="None",
    )
    password = models.CharField(
        max_length=30,
        null=True,
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+996\d+$",  # Phone Number (Only Kyrgyzstan)
                message="Phone Number",
                code="invalid_data",
            )
        ],
        default='+996',
        null=True,
        blank=True
    )
    status = models.CharField(
        choices=ROLES,
        max_length=100,
        default='',
    )


class Administrator(models.Model):
    username = models.CharField(
        max_length=100,
        unique=True,
        error_messages={None: 'A user with that username already exists.'},
        blank=True, default='AnonymousProducer'
    )
    email = models.EmailField(
        unique=True,
        error_messages={None: 'A user with that email already exists.'},
        blank=True,
        default="None",
    )
    password = models.CharField(
        max_length=30,
        null=True,
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+996\d+$",  # Phone Number (Only Kyrgyzstan)
                message="Phone Number",
                code="invalid_data",
            )
        ],
        default='+996',
        null=True,
        blank=True
    )
    status = models.CharField(
        choices=ROLES,
        max_length=100,
        default='',
    )


class StoreOwner(models.Model):
    username = models.CharField(
        max_length=100,
        unique=True,
        error_messages={None: 'A user with that username already exists.'},
        blank=True, default='AnonymousProducer'
    )
    email = models.EmailField(
        unique=True,
        error_messages={None: 'A user with that email already exists.'},
        blank=True,
        default="None",
    )
    password = models.CharField(
        max_length=30,
        null=True,
    )
    managers = models.ManyToManyField(
        StoreManager, related_name="manager"
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+996\d+$",  # Phone Number (Only Kyrgyzstan)
                message="Phone Number",
                code="invalid_data",
            )
        ],
        default='+996',
        null=True
    )
    status = models.CharField(
        choices=ROLES,
        max_length=100,
        default='',
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
    username = models.CharField(
        max_length=100,
        unique=True,
        error_messages={None: 'A user with that username already exists.'},
        blank=True, default='AnonymousProducer'
    )
    email = models.EmailField(
        unique=True,
        error_messages={None: 'A user with that email already exists.'},
        blank=True,
        default="None",
    )
    password = models.CharField(
        max_length=30,
        null=True,
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
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+996\d+$",  # Phone Number (Only Kyrgyzstan)
                message="Phone Number",
                code="invalid_data",
            )
        ], default='+996'
    )
    status = models.CharField(
        choices=ROLES,
        max_length=100,
        default='',
    )
    product = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True)
