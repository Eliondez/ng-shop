# Generated by Django 2.1.2 on 2019-02-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myitem',
            name='category',
        ),
        migrations.AddField(
            model_name='myitem',
            name='category',
            field=models.ManyToManyField(to='main.Category'),
        ),
    ]
