# Generated by Django 3.0.6 on 2020-07-11 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event',
            new_name='band',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
    ]
