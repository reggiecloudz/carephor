# Generated by Django 3.2.18 on 2023-05-27 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230526_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='orientation',
        ),
        migrations.RemoveField(
            model_name='member',
            name='political_ideology',
        ),
    ]
