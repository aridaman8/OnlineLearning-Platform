# Generated by Django 3.0.1 on 2020-02-21 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200220_0045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]