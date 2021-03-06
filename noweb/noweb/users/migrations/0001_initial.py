# Generated by Django 3.2.7 on 2021-09-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=64, verbose_name='Password')),
                ('point', models.IntegerField(verbose_name='Point')),
            ],
            options={
                'verbose_name': 'users',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
    ]
