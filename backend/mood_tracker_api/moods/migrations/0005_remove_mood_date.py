# Generated by Django 3.1.1 on 2020-09-25 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moods', '0004_auto_20200925_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mood',
            name='date',
        ),
    ]