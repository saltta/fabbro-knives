# Generated by Django 3.2 on 2023-01-11 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20230111_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='test',
        ),
    ]
