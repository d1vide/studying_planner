# Generated by Django 4.2.11 on 2024-04-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_alter_priority_options_alter_priority_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='plan',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
