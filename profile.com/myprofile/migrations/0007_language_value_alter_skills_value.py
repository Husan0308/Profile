# Generated by Django 5.0.6 on 2024-06-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0006_skills_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='value',
            field=models.DecimalField(decimal_places=0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='value',
            field=models.DecimalField(decimal_places=0, max_digits=7, null=True),
        ),
    ]
