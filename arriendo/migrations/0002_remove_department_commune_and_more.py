# Generated by Django 4.0.7 on 2022-09-22 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arriendo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='commune',
        ),
        migrations.RemoveField(
            model_name='department',
            name='department_type',
        ),
        migrations.DeleteModel(
            name='Commune',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='DepartmentType',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
