# Generated by Django 3.0.6 on 2020-05-24 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ChatBot', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='QAForBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=255)),
                ('answer', models.CharField(default='', max_length=255)),
                ('chatbot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.ChatBot')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=255)),
                ('time', models.TimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('chatbot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.ChatBot')),
            ],
        ),
    ]
