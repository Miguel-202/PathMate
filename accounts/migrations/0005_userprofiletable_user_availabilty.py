# Generated by Django 4.2.5 on 2023-09-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofiletable_needs_visa_sponsorship'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiletable',
            name='User_Availabilty',
            field=models.CharField(default=-1, max_length=100),
            preserve_default=False,
        ),
    ]
