# Generated by Django 4.2.4 on 2023-10-22 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_producto_cantidad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]