# Generated by Django 4.1.7 on 2023-03-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='posts.tag'),
        ),
    ]
