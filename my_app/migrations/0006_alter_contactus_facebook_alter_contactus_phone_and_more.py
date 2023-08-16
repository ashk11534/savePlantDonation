# Generated by Django 4.1.2 on 2023-08-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0005_contactus_alter_aboutus_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactus",
            name="facebook",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="phone",
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="twitter",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="whatsapp",
            field=models.CharField(max_length=14, null=True),
        ),
    ]
