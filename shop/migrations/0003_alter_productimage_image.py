# Generated by Django 3.2 on 2021-05-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rating_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/products'),
        ),
    ]