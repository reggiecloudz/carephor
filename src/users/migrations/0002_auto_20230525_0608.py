# Generated by Django 3.2.18 on 2023-05-25 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
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
        migrations.RemoveField(
            model_name='member',
            name='religion',
        ),
        migrations.AddField(
            model_name='member',
            name='denomination',
            field=models.CharField(blank=True, choices=[('Assyrian', 'Assyrian'), ('Oriental Orthodox', 'Oriental Orthodox'), ('Eastern Orthodox', 'Eastern Orthodox'), ('Catholic', 'Catholic'), ('Protestant', 'Protestant'), ('Latter Day Saints', 'Latter Day Saints'), ('Independent', 'Independent'), ('Nontrinitarian', 'Nontrinitarian'), ('Non-denominational', 'Non-denominational')], default='Non-denominational', max_length=18, verbose_name='denomination'),
        ),
        migrations.AddField(
            model_name='member',
            name='is_church_leader',
            field=models.BooleanField(blank=True, default=False, verbose_name='church leader status'),
        ),
    ]
