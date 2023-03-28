# Generated by Django 4.1.7 on 2023-03-28 09:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_borrow_back_date_alter_borrow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 27, 11, 3, 0, 874361)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book', unique=True),
        ),
    ]
