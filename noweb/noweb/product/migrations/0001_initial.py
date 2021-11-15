# Generated by Django 3.2.7 on 2021-09-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Product Name')),
                ('image', models.ImageField(upload_to='image/')),
                ('video', models.FileField(upload_to='video/')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='RegisterDate')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
                'db_table': 'product',
            },
        ),
    ]
