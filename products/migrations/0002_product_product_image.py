# Generated by Django 4.1.2 on 2022-10-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.URLField(blank=True),
        ),
    ]
