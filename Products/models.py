from django.db import models
from django.utils.text import slugify
from users.models import User, SellerProfile

class Category(models.model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    discription = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.ImageField(upload_to='categoies/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Product(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
        ('suspended', 'Suspended'),
    ]

    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compare_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=3, default='NGN')
    sku = models.CharField(max_length=100, unique=True)
    stock = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products')
    attributes = models.JSONField(null=True, blank=True)
    weight_mode = models.CharField(max_length=50, choices = [('kg', 'KG', )('g', 'G')], default='kg')
    dimensions = models.JSONField(null=True, blank=True)
    seo_title = models.CharField(max_length=100,  blank=True) 
    seo_description = models.TextField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.FoereignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)


    class Meta:
        db_table = 'product_images'
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.product.title}"


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    sku = models.CharField(max_length=100, unique=True) # Stock Keeping Unit
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    attributes = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'product_variants'
       

    def __str__(self):
    
        return f"{self.product.title} - {self.attributes}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table  = 'tags'
        ordering = ['name']


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='product_tags')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'product_tags'
        unique_together = ('product', 'tag')