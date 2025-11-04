from django.contrib import admin
from .models import Product, ProductImage, ProuctVariant, Tag, ProductTag, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
