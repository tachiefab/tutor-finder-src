# Generated by Django 3.0.4 on 2020-03-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
