from django.contrib import admin
from .models import Resort, Building, Apartment


class ResortAdmin(admin.ModelAdmin):
    pass


class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'building_number', 'resort')


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('building', 'apartment_number', 'floor', 'bedrooms', 'covered_gross', 'balcony', 'position', 'price_in_gbp')


admin.site.register(Resort, ResortAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Apartment, ApartmentAdmin)
