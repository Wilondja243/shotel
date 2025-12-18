import re
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from shotel.app.core.models import BaseModel


class User(AbstractUser):
    ROLE_CHOISES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'user'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    is_my_follower = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices=ROLE_CHOISES)

    def clean(self):
        email_validate = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        errors = {}

        if not self.username:
            errors["username"] = "This field is required."

        if not re.match(email_validate, self.email):
            errors["email"] = "Email is not valid."

        if errors:
            raise ValidationError(errors)
        

class Address(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20, null=True, blank=True)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.city}, {self.country}"
