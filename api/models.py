from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    common_name = models.CharField(max_length=50, blank=False)
    official_language = models.CharField(max_length=50, blank=False)
    cca3 = models.CharField(max_length=3, blank=False)
    population = models.PositiveIntegerField(blank=False)
    currency = models.CharField(max_length=50, blank=False)
    continent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="countries"
    )

    def __str__(self):
        return f"{self.common_name}:{self.continent}"
