# Generated by Django 4.2.11 on 2024-04-08 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_alter_plan_time_required'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('priority', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
            ],
        ),
        migrations.AlterField(
            model_name='plan',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.priority', verbose_name='Приоритет'),
        ),
    ]
