# Generated by Django 4.0.4 on 2022-09-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]