# Generated by Django 4.2.1 on 2023-07-16 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_expense_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='id',
            new_name='id_given',
        ),
    ]