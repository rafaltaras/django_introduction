# Generated by Django 4.1.7 on 2023-03-28 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_borrow'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 27, 10, 26, 36, 181570)),
        ),
    ]