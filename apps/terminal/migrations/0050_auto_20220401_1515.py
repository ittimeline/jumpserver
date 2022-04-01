# Generated by Django 3.1.14 on 2022-04-01 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0049_auto_20220401_1132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='protocol',
            options={'ordering': ('name',), 'verbose_name': 'Protocol'},
        ),
        migrations.AlterField(
            model_name='protocol',
            name='port',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65535)], verbose_name='Port'),
        ),
    ]
