# Generated by Django 3.0.3 on 2020-02-03 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200203_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], max_length=60),
        ),
    ]