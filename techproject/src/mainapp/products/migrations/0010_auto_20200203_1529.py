# Generated by Django 3.0.3 on 2020-02-03 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200203_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
