# Generated by Django 3.0.4 on 2020-07-08 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200708_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='product',
            new_name='productmen',
        ),
    ]
