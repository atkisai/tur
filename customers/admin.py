from django.contrib import admin
from customers.models import Customer


class CustomerAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields]

    class Meta:
        model = Customer
admin.site.register(Customer, CustomerAdmin)
