# Generated by Django 4.0 on 2023-06-18 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_post_published_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 18, 21, 8, 12, 755916)
            ),
        ),
    ]
