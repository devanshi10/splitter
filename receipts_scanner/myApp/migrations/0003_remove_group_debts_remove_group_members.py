# Generated by Django 4.2.1 on 2023-05-25 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_debt_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='debts',
        ),
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
    ]
