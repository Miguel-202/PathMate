# Generated by Django 4.2.5 on 2023-09-16 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0005_userprofiletable_user_availabilty"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofiletable",
            name="User_id",
            field=models.IntegerField(default=0),
        ),
    ]
