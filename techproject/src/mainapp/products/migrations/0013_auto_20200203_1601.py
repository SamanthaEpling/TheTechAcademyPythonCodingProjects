# Generated by Django 3.0.3 on 2020-02-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20200203_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
