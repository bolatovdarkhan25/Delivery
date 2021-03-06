# Generated by Django 3.0.6 on 2020-05-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200522_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='postal_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
