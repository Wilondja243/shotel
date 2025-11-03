import re
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):
    ROLE_CHOISES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'user'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
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