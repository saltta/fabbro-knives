# Generated by Django 3.2 on 2023-02-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_remove_product_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]