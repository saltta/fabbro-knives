# Generated by Django 3.2 on 2023-01-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20230109_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='test',
            field=models.ManyToManyField(related_name='test', to='stock.Category'),
        ),
    ]