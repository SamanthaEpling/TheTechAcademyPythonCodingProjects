# Generated by Django 3.0.3 on 2020-02-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200203_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]