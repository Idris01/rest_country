# Generated by Django 4.1.4 on 2022-12-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("common_name", models.CharField(max_length=50)),
                ("official_language", models.CharField(max_length=50)),
                ("cca3", models.CharField(max_length=3)),
                ("population", models.PositiveIntegerField()),
                ("currency", models.CharField(max_length=50)),
                ("continent", models.CharField(max_length=50)),
            ],
        ),
    ]
