from django.db import models
from django.db import models


class Period(models.Model):

    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'


class Location(models.Model):
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    hotel = models.CharField(max_length=128)
    period = models.ForeignKey(Period, blank=True, null=True, default=None)
    image = models.ImageField(upload_to="images/", blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s %s" % (self.country, self.city, self.hotel)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Tour(models.Model):
    location = models.ForeignKey(Location)
    title = models.CharField(max_length=128)
    description = models.TextField()
    rating = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    value = models.IntegerField(default=0)
    nights = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    departure = models.DateField(blank=True, null=True)


    def __str__(self):
        return "Тур в отель %s" % self.location.hotel

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


