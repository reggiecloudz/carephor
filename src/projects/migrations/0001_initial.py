# Generated by Django 3.2.18 on 2023-04-07 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.BooleanField(blank=True, default=False, verbose_name='selected')),
                ('qualifications', models.TextField(blank=True, null=True, verbose_name='qualifications')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'applicant',
                'verbose_name_plural': 'applicants',
            },
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('item', models.CharField(blank=True, max_length=128, verbose_name='item')),
                ('purpose', models.TextField(blank=True, null=True, verbose_name='purpose')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='cost')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'expenditure',
                'verbose_name_plural': 'expenditures',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='title')),
                ('details', models.TextField(blank=True, null=True, verbose_name='details')),
                ('open', models.BooleanField(default=True, verbose_name='open')),
                ('people_needed', models.PositiveIntegerField(blank=True, default=1, verbose_name='people_needed')),
                ('positions_filled', models.PositiveIntegerField(blank=True, default=0, verbose_name='positions filled')),
                ('requirements', models.TextField(blank=True, null=True, verbose_name='requirements')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'position',
                'verbose_name_plural': 'positions',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='name')),
                ('overview', models.TextField(blank=True, default='', verbose_name='overview')),
                ('vision', models.TextField(blank=True, default='', verbose_name='vision')),
                ('beneficiaries', models.JSONField(blank=True, default=list, null=True, verbose_name='beneficiaries')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='projects/%Y/%m/%d/')),
                ('closed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('Manager', 'Manager'), ('Staff', 'Staff'), ('Supporter', 'Supporter'), ('Donor', 'Donor')], default='Supporter', max_length=10, verbose_name='role')),
                ('position', models.CharField(blank=True, max_length=128, verbose_name='position')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'project member',
                'verbose_name_plural': 'project members',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('task', models.CharField(blank=True, max_length=128, verbose_name='task')),
                ('details', models.TextField(blank=True, null=True, verbose_name='details')),
                ('results', models.TextField(blank=True, null=True, verbose_name='results')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='deadline')),
                ('complete_date', models.DateField(blank=True, null=True, verbose_name='complete date')),
                ('complete', models.BooleanField(blank=True, default=False, verbose_name='complete')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='projects.task')),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'action',
                'verbose_name_plural': 'actions',
            },
        ),
    ]
