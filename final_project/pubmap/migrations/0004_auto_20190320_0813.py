# Generated by Django 2.1.7 on 2019-03-20 08:13

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubmap', '0003_pub_open_now'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pub',
            name='open_now',
        ),
        migrations.AlterField(
            model_name='pub',
            name='formatted_phone_number',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='pub',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pub',
            name='longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pub',
            name='opening_hours',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='pub',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
