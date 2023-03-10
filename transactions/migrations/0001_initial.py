# Generated by Django 4.1.5 on 2023-01-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("type", models.IntegerField()),
                ("date", models.DateField()),
                ("value", models.DecimalField(decimal_places=2, max_digits=8)),
                ("cpf", models.CharField(max_length=11)),
                ("card", models.CharField(max_length=12)),
                ("hour", models.TimeField()),
                ("store_owner", models.CharField(max_length=14)),
                ("store_name", models.CharField(max_length=19)),
            ],
        ),
    ]
