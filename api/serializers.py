from rest_framework import serializers
from .models import Country, Continent


class ContinentSerializer(serializers.ModelSerializer):
    country_count = serializers.SerializerMethodField()

    class Meta:
        model = Continent
        fields = ["name", "country_count"]

    def get_country_count(self, obj):
        return obj.countries.count()


class CountrySerializer(serializers.ModelSerializer):
    continent_name = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = [
            "common_name",
            "currency",
            "official_language",
            "cca3",
            "continent",
            "continent_name",
        ]

    def get_continent_name(self, obj):
        return obj.continent.name
