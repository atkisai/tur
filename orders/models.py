from django.db import models

from customers.models import Customer
from tours.models import Tour, Location, Period

class Status(models.Model):

    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'



class Order(models.Model):
    customer = models.ForeignKey(Customer)
    customer2 = models.ForeignKey(Customer, related_name='customer2', blank=True, null=True, default=None)
    customer3 = models.ForeignKey(Customer, related_name='customer3', blank=True, null=True, default=None)
    customer4 = models.ForeignKey(Customer, related_name='customer4', blank=True, null=True, default=None)
    customer5 = models.ForeignKey(Customer, related_name='customer5', blank=True, null=True, default=None)
    customer6 = models.ForeignKey(Customer, related_name='customer6', blank=True, null=True, default=None)
    tour = models.ForeignKey(Tour)
    created  = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.ForeignKey(Status)

    # tour_value = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    # tour_discount = models.DecimalField(max_digits=3, decimal_places=2, default=1)
    # discount_location = models.DecimalField(max_digits=3, decimal_places=2, default=1)

    def __str__(self):
        return "%s" % self.tour

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # def save(self, *args, **kwargs):
    #     discount_tour = self.tour.discount
    #     self.discount_tour = discount_tour
    #
    #     # discount_location = self.location.discount
    #     # self.discount_location = discount_location
    #
    #     tour_value = self.tour.value
    #     self.tour_value = tour_value
    #
    #     self.total_value = discount_tour-(discount_tour * tour_value)
    #
    #     super(Order, self).save(*args, **kwargs)


