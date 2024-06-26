# Generated by Django 4.2.11 on 2024-04-08 16:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_remove_plan_progress_alter_plan_time_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='time_required',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Примерное время на задачу (в часах)'),
        ),
    ]
