# Generated by Django 3.0 on 2020-09-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200921_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]