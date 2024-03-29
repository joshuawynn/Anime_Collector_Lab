# Generated by Django 5.0.1 on 2024-01-11 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('rating', models.CharField(choices=[('B', 'Bad'), ('G', 'Good'), ('A', 'Awesome')], default='B', max_length=1)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.anime')),
            ],
        ),
    ]
