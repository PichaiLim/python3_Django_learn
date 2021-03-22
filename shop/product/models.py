from django.db import models

# Create your models here.
class AllProduct(models.Model):
    product_name = models.CharField(max_length=100)
    product_pricet = models.CharField(max_length=100)
    product_detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product_name
    