# Generated by Django 3.2.15 on 2022-08-16 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_rename_last_name_user_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='option',
            new_name='add_info',
        ),
    ]
