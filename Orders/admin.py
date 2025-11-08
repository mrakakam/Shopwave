# Import the Django admin module — used to register and manage models in the admin site
from django.contrib import admin

# Import all the models you want to manage through the admin interface
from .models import Order, OrderItem, ShippingMethod, OrderShipping, Cart, CartItem


# Inline allows related OrderItem objects to appear on the Order admin page
class OrderItemInline(admin.TabularInline):
    model = OrderItem  # Connect this inline to the OrderItem model
    extra = 0  # Prevents showing extra empty forms by default
    readonly_fields = ('product_name', 'product_sku', 'price')  # These fields can’t be edited in admin


# Register the Order model to appear in the admin dashboard
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('order_number', 'buyer', 'status', 'total_amount', 'created_at')
    # Add filter options on the right side of the admin
    list_filter = ('status', 'created_at')
    # Allow search by order number or buyer’s email
    search_fields = ('order_number', 'buyer__email')
    # Fields that should not be editable
    readonly_fields = ('order_number', 'created_at', 'upated_at')  # ⚠️ Typo: should be 'updated_at'
    # Display related order items inline on the order page
    inlines = [OrderItemInline]


# Register the OrderItem model
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'quantity', 'price', 'created_at')
    list_filter = ('created_at',)  # ⚠️ You need a comma to make this a tuple
    search_fields = ('order__order_number', 'product_name')
    readonly_fields = ('created_at',)


# Register the ShippingMethod model
@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'estimated_days')
    list_filter = ('is_active',)
    search_fields = ('name',)


# Register the OrderShipping model
@admin.register(OrderShipping)
class OrderShippingAdmin(admin.ModelAdmin):
    list_display = ('order', 'shipping_method', 'tracking_number', 'shipped_at')  # ⚠️ Removed space after 'order'
    list_filter = ('shipped_at',)
    search_fields = ('order__order_number', 'tracking_number')


# Register the Cart model
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_items', 'updated_at', 'subtotal')  # ⚠️ Removed space after 'updated_at'
    list_filter = ('created_at', 'updated_at')


# Register the CartItem model
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'variant', 'quantity', 'updated_at')
    list_filter = ('updated_at',)
    search_fields = ('cart__user__email', 'product__title')
