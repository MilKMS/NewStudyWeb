from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=256, verbose_name="Password")
    point = models.IntegerField(verbose_name="Point", default=0)
    # level = models.CharField(max_length=8, verbose_name='Permission',
    #     choices=(
    #         ('admin', 'admin'),
    #         ('user', 'user'),
    #     ))

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = 'users'
        verbose_name_plural = 'users'
        