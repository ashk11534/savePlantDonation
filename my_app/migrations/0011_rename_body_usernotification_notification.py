# Generated by Django 4.1.2 on 2023-08-15 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0010_usernotification"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usernotification", old_name="body", new_name="notification",
        ),
    ]
