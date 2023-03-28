# Generated by Django 4.1.7 on 2023-03-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_tag_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='posts.tag'),
        ),
    ]