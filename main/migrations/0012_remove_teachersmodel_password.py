# Generated by Django 4.2.6 on 2023-11-02 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_studentmodel_is_active_studentmodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachersmodel',
            name='password',
        ),
    ]
