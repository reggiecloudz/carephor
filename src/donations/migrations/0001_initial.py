# Generated by Django 3.2.18 on 2023-05-24 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundraiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_goal', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='financial goal')),
                ('funds_raised', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='funds raised')),
                ('closed', models.BooleanField(default=False)),
                ('owner_id', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner_content_type', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'fundraiser',
                'verbose_name_plural': 'fundraisers',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='amount')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('donor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='users.member', verbose_name='donor')),
                ('fundraiser', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='donations.fundraiser', verbose_name='fundraiser')),
            ],
            options={
                'verbose_name': 'donation',
                'verbose_name_plural': 'donations',
            },
        ),
    ]
