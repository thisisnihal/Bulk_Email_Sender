# Generated by Django 5.1.4 on 2024-12-29 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_email_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Desgination',
            new_name='f_Desgination',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Email',
            new_name='f_Email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Id',
            new_name='f_Id',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Name',
            new_name='f_Name',
        ),
    ]
