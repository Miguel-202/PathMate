# Generated by Django 4.2.5 on 2023-09-16 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=300)),
                ('User_Country', models.CharField(max_length=300)),
                ('Job', models.CharField(max_length=300)),
                ('User_Age', models.CharField(max_length=100)),
                ('User_Major', models.CharField(max_length=300)),
                ('User_GraduationDate', models.DateField()),
                ('Level_Study', models.CharField(max_length=300)),
                ('Location', models.CharField(max_length=300)),
                ('Goals', models.CharField(max_length=300)),
                ('Goal_DeathLine', models.DateField()),
                ('Skill_set', models.CharField(max_length=300)),
                ('Needs_Visa_Sponsorship', models.BooleanField()),
            ],
        ),
    ]