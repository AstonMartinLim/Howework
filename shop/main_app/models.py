from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils import timezone
from main_app.exceptions import NotEnoughProductException, NotEnoughMoneyException, ReturnTimeExpired

# Create your models here.


class CustomUser(AbstractUser):
    wallet = models.FloatField(default=10000.0)

    def __str__(self):
        return self.username


class Product(models.Model):
    name_of_product = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ['name_of_product', ]

    def __str__(self):
        return self.name_of_product


class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='buyer')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="order")
    quantity = models.PositiveIntegerField(default=1)
    time_of_purchase = models.DateTimeField(auto_now_add=True)
    total_sum = models.FloatField(default=0)

    class Meta:
        ordering = ['-time_of_purchase', ]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.product.quantity < self.quantity:
            raise NotEnoughProductException
        elif self.get_total_sum > self.user.wallet:
            raise NotEnoughMoneyException
        self.user.wallet -= self.get_total_sum
        self.product.quantity -= self.quantity
        self.user.save(update_fields=["wallet"])
        self.product.save(update_fields=["quantity"])
        self.purchase.save()
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    @property
    def get_total_sum(self):
        return self.quantity * self.product.price


class Return(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='returner')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='goods')
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase')
    time_of_return = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["time_of_return"]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if timezone.now() > self.purchase.time_of_purchase + timedelta(minutes=3):
            raise ReturnTimeExpired
        else:
            super().save(force_insert=False, force_update=False, using=None, update_fields=None)


