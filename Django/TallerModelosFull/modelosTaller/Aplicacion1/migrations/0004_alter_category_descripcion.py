# Generated by Django 5.0.7 on 2024-07-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0003_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
