# Generated by Django 3.0.3 on 2020-02-05 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20200204_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('treats', 'treats'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
