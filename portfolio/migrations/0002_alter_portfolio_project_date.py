# Generated by Django 4.2.7 on 2024-02-28 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="project_date",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 2, 28, 10, 30, 52, 259773)
            ),
        ),
    ]