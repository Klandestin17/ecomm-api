# Generated by Django 5.0.6 on 2024-10-11 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rating',
            new_name='ratings',
        ),
        migrations.AlterField(
            model_name='product',
            name='clothesType',
            field=models.CharField(default='unisex', max_length=255),
        ),
    ]