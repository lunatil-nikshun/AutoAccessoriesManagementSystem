from django.contrib import admin
from .models import Accessories, Cart, CartItems
# Register your models here.
admin.site.register(Accessories)
admin.site.register(Cart)
admin.site.register(CartItems)