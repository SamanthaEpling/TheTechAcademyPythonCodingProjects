# Generated by Django 3.0.3 on 2020-02-04 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20200203_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
