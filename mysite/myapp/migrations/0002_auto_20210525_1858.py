# Generated by Django 3.0.5 on 2021-05-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
