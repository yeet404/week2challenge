# Generated by Django 3.2.8 on 2021-11-06 23:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 23, 52, 57, 576441, tzinfo=utc)),
        ),
    ]
