# Generated by Django 4.2.7 on 2024-01-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoclass',
            name='date',
            field=models.DateTimeField(),
        ),
    ]