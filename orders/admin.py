from django.contrib import admin

from orders.models import Order, Status

class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)



class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

