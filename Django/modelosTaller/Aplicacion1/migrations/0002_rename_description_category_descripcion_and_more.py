# Generated by Django 4.2.7 on 2024-06-20 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='date_added',
            new_name='fecha_anadida',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
    ]
