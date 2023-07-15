# Generated by Django 3.2.18 on 2023-05-17 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('small_groups', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='users.member'),
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='small_groups.smallgroup', verbose_name='group'),
        ),
        migrations.AddField(
            model_name='poll',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='users.member', verbose_name='creator'),
        ),
        migrations.AddField(
            model_name='poll',
            name='group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='small_groups.smallgroup', verbose_name='group'),
        ),
        migrations.AddField(
            model_name='choicevotecount',
            name='choice',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice_votes', to='posts.choice', verbose_name='choice'),
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='posts.poll', verbose_name='poll'),
        ),
        migrations.AlterUniqueTogether(
            name='choicevotecount',
            unique_together={('choice', 'voter')},
        ),
    ]
