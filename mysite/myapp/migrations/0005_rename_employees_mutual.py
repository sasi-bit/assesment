# Generated by Django 3.2.3 on 2021-05-26 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_employees_emp_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='employees',
            new_name='mutual',
        ),
    ]
