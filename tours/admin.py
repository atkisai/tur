from django.contrib import admin
from tours.models import Tour, Location, Period


class TourAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Tour._meta.fields]

    class Meta:
        model = Tour
admin.site.register(Tour, TourAdmin)



class LocationAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Location._meta.fields]

    class Meta:
        model = Location
admin.site.register(Location, LocationAdmin)



class PeriodAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Period._meta.fields]

    class Meta:
        model = Period
admin.site.register(Period, PeriodAdmin)