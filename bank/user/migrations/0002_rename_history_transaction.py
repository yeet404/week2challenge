# Generated by Django 3.2.8 on 2021-11-05 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='Transaction',
        ),
    ]
