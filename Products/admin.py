from django.contrib import admin
from .models import Product, ProductImage, ProuctVariant, Tag, ProductTag, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductVariantInline(admin.TabularInline):
    model = ProuctVariant
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'is_active')
   list_filter = ('is_active', 'parent')
   search_fields = ('name', 'description')
   prepopulated_fields = {'slug': ('name',)}
   readonly_fields = ('created_at', 'updated_at')


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('seller', 'price', 'stock', 'category', 'created_at' 'status' 'title')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'description', 'sku')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProductImageInline, ProductVariantInline]


@admin.register(ProductImage)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'is_primary', 'other')
    list_filter = ('is_primary',)
    search_fields = ('product__title',)
    

