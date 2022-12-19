from django.contrib import admin
from .models import Country, Continent


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    pass
