# Generated by Django 4.2.7 on 2024-01-02 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0002_alter_todoclass_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoclass',
            name='date',
            field=models.DateTimeField(default=datetime.timezone),
        ),
    ]
