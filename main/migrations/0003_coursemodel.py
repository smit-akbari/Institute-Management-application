# Generated by Django 4.2.6 on 2023-11-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_teachersmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_name', models.CharField(max_length=100)),
                ('course_duration', models.CharField(max_length=50)),
                ('course_fees', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
