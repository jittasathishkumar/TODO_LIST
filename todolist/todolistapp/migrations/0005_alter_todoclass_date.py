# Generated by Django 4.2.7 on 2024-01-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0004_alter_todoclass_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoclass',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
