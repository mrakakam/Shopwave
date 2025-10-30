from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    # Basic Info
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=20,  null=True, blank=True)

    # User type
    is_seller = models.BooleanField (_('is seller'), default=False)
    is_buyer = models.BooleanField (_('is buyer'), default==True)

    # Verification fields
    email_verified = models.BooleanField (_('email verified') , default=False)
     email_verified = models.BooleanField (_('phone verified') , default=False)

    # Auto timestamps
    created_at = models.DateTimeField(_('created at') , auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at') , auto_now=True)

    # Use email instead of username for login
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

   class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email
