# Generated by Django 4.1.7 on 2023-03-15 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=5)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('author_bio', models.TextField(blank=True, null=True)),
                ('author_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.author')),
            ],
        ),
    ]
