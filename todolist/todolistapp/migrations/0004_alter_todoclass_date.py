# Generated by Django 4.2.7 on 2024-01-02 12:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0003_alter_todoclass_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoclass',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
