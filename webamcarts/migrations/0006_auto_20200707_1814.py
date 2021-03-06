# Generated by Django 3.0.7 on 2020-07-07 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webamcarts', '0005_auto_20200707_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmen',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cartmen',
            name='productmen',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webamcarts.Cartmen'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='line_total',
            field=models.DecimalField(decimal_places=2, default=10.99, max_digits=1000),
        ),
    ]
