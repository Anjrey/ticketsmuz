# Generated by Django 3.0.6 on 2020-07-11 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20200711_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='fan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.Fan'),
        ),
    ]