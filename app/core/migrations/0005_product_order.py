# Generated by Django 4.0.1 on 2024-07-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
