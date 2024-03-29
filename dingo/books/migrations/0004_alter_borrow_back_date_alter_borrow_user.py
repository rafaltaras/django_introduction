# Generated by Django 4.1.7 on 2023-03-28 08:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_borrow_back_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 27, 10, 58, 15, 341150)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
