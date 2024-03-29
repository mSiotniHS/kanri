# Generated by Django 5.0.1 on 2024-02-04 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text content')),
                ('someday', models.BooleanField(default=False, verbose_name='Until someday')),
            ],
            options={
                'verbose_name': 'Inbox entry',
                'verbose_name_plural': 'Inbox entries',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('archived', models.BooleanField(default=False, verbose_name='Is archived')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Space',
                'verbose_name_plural': 'Spaces',
            },
        ),
        migrations.CreateModel(
            name='InboxFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='inbox_files', verbose_name='File')),
                ('inbox_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.inbox', verbose_name='Inbox entry')),
            ],
            options={
                'verbose_name': 'Inbox entry file',
                'verbose_name_plural': 'Inbox entry files',
            },
        ),
        migrations.CreateModel(
            name='ProjectLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timestamp')),
                ('text', models.TextField(verbose_name='Log text')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.project', verbose_name="Log's project")),
            ],
            options={
                'verbose_name': 'Project log',
                'verbose_name_plural': 'Project changelog',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.space', verbose_name='Related space'),
        ),
        migrations.AddField(
            model_name='inbox',
            name='space',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.space', verbose_name='Related space'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('status', models.SmallIntegerField(choices=[(0, 'To do'), (1, 'In work'), (2, 'Canceled'), (3, 'Waiting'), (4, 'Done')], default=0, verbose_name='Status')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Deadline')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.project', verbose_name='Parent project')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
