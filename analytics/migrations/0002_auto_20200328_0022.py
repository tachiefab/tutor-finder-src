# Generated by Django 3.0.4 on 2020-03-28 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objectviewed',
            old_name='counter',
            new_name='count',
        ),
    ]
