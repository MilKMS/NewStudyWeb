import os

from django.db import models

from users.models import Users

def file_path(instance,filename):
    path = "media/"
    format = "uploaded-" + filename
    return os.path.join(path,format)

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=256, verbose_name="Product Name")
    image = models.ImageField(upload_to="image/")
    video = models.FileField(upload_to=file_path)
    price = models.IntegerField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="RegisterDate")

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Product'