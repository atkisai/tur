from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    phone2 = models.CharField(max_length=128, blank=True, null=True, default=None)
    email = models.CharField(max_length=128)
    email2 = models.CharField(max_length=128, blank=True, null=True, default=None)
    address = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
