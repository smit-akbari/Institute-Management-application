# Generated by Django 4.2.6 on 2023-11-02 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_coursemodel_course_faculaty_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='course_faculaty_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='students_course_faculaty_name', to='main.coursemodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_course_name', to='main.coursemodel'),
        ),
    ]