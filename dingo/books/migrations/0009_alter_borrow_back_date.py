# Generated by Django 4.1.7 on 2023-05-09 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_borrow_back_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 8, 22, 29, 41, 718146)),
        ),
    ]