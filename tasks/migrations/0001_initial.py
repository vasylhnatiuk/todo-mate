# Generated by Django 4.0.6 on 2022-07-11 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=255)),
                ('datetime', models.DateTimeField()),
                ('deadline', models.DateTimeField(blank=None, null=True)),
                ('done', models.BooleanField()),
                ('tags', models.ManyToManyField(related_name='tasks', to='tasks.tag')),
            ],
            options={
                'ordering': ['done'],
            },
        ),
    ]
