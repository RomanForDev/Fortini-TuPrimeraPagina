# Generated by Django 5.1.6 on 2025-03-20 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_piedra_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piedra',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Imagen'),
        ),
    ]
