# Generated by Django 3.2.18 on 2023-03-28 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_auto_20230327_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='campaign',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='campaigns.campaign', verbose_name='campaign'),
        ),
    ]
