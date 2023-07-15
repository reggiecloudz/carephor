# Generated by Django 3.2.18 on 2023-05-24 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, verbose_name='text'),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='posts/%Y/%m/%d/', verbose_name='media')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='description')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='posts.post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'media',
                'verbose_name_plural': 'media',
            },
        ),
    ]
