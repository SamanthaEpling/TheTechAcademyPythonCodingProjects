# Generated by Django 3.0.3 on 2020-02-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200203_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('treats', 'treats')], max_length=60),
        ),
    ]
