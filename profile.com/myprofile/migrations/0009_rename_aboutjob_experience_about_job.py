# Generated by Django 5.0.6 on 2024-06-11 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0008_rename_user_customer_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='aboutjob',
            new_name='about_job',
        ),
    ]
