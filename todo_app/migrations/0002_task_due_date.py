# Generated by Django 3.1.3 on 2020-11-25 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]