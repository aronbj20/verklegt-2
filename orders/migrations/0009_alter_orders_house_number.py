# Generated by Django 3.2 on 2021-05-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_rename_pvc_orders_cvc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='house_number',
            field=models.CharField(max_length=10),
        ),
    ]
