# Generated by Django 5.0.2 on 2024-08-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pricewebsiteapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="site",
            field=models.CharField(default="default_site", max_length=50),
        ),
    ]
