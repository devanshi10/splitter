# Generated by Django 4.2.1 on 2023-05-25 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_group_debts_group_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='debts',
        ),
    ]
