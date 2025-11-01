from django.contrib import admin
from django.contrib.auth.admin import UserAdmin #for handling user management
from .models import User, SellerProfile, Address


@admin.register(User) #register the User model with the admin site
class CustmerAdmin(UserAdmin):
    model = User
    List_display = ('email', 'first_name', 'last_name', 'is_seller', 'is_buyer', 'is_staff',  'is_active')
    list_filter = ('is_seller', 'is_buyer', 'is_staff', 'is_active')
    fieldsets = (

        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_seller', 'is_buyer', 'is_staff', 'is_active' 'phone_number')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (

        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_seller', 'is_buyer', 'is_staff', 'is_active')}
        ),
    )


    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


    @admin.register(SellerProfile)
    class SellerProfileAdmin(admin.ModelAdmin):
        List_display = ('user', 'business_name', 'verified', 'kyc_status', 'created_at')
        search_fields = ('user_email', 'business_name')
        list_filter = ('verified', 'kyc_status')
        readonly_fields = ('created_at', 'updated_at')


    @admin.register(UserProfile)
    class UserProfileAdmin(admin.ModelAdmin):
        List_display = ('user', 'preferred_currency',  'created_at')
        search_fields = ('user__email',)

    
    @admin.register(Address)
    class AddressAdmin(admin.ModelAdmin):
        List_display = ('user', 'street_address', 'city',  'country',  'is_default', 'address_type')
        list_filter = ('is_default', 'country' , 'address_type')
        readonly_fields = ('street_address', 'city', 'user__email')