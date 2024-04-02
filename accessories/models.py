from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings


# CrAccessorieseate your models here.

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{ self.name }"


class Accessories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to='part_images/', null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    


    
class Cart(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.user.username }"

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        f"{ self.quantity } * { self.accessories.name } in cart for {self.cart.user.username }"