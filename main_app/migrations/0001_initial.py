# Generated by Django 5.0.1 on 2024-01-10 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
                ('genre', models.TextField(max_length=250)),
                ('release_year', models.IntegerField()),
            ],
        ),
    ]
