# Generated by Django 3.2.7 on 2021-11-09 21:03

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.FileField(upload_to=product.models.file_path),
        ),
    ]