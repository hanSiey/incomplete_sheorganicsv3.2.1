# Generated by Django 3.2.4 on 2021-12-31 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='distributor',
        ),
    ]
