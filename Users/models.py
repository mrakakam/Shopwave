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


class SellerProfile(models.Model):
   KYC_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='seller_profile'
)

business_name = models.CharField(_('business name'), blank=True,  max_length=255, null=True)
business_address = models.TextField(  null=True)
business_phone_number = models.CharField(, max_length=20, blank=True, null=True)
business_address = models.TextField( blank=True)
verified= models.BooleanField(_('verified'), default=False)
kyc_status = models.CharField(
        max_length=20,
        choices=KYC_STATUS_CHOICES,
        default='pending'
    )

    kyc_documents = models.JSONField(default=dict, blank=True)
    payoutinfo = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)


    class Meta:
        db_table = 'seller_profile'

    def __str__(self):
        return f" {self.user.email} - {self.business_name}"

    class  Address(models.Model):
        ADDReSS_TYPE_CHOICES = [
        ('shipping', 'Shipping'),
        ('billing', 'Billing'),
        ('both', 'Both'),
    ]

    user= models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='addresses'
    )

    address_type = models.CharField(
        max_length=20,
        choices=ADDReSS_TYPE_CHOICES,
        default='shipping'
    )

    street_address = models.CharField(_('street address'), max_length=255)
    city = models.CharField(_('city'), max_length=100)
    state = models.CharField(_('state'), max_length=100)
    country = models.CharField(_('country'), max_length=100)
    postal_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)


class Meta:
        db_table = 'addresses'
        vrbose_name_plural = 'Addresses'

def  __str__(self):
        return f"{self.user.email} - {self.address_type} Address"


