# Generated by Django 2.1.7 on 2019-03-20 08:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubmap', '0006_auto_20190320_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pub',
            name='opening_hours',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pub',
            name='place_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
