# Generated by Django 4.0.6 on 2022-07-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
