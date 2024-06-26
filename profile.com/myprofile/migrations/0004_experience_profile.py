# Generated by Django 5.0.6 on 2024-06-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0003_education_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_company', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('aboutjob', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=255)),
            ],
        ),
    ]
