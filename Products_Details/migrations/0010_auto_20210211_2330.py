# Generated by Django 3.0.8 on 2021-02-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products_Details', '0009_auto_20210211_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='number_of_people',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='other_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
