# Generated by Django 2.2.7 on 2020-12-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20201228_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='Percentage',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='result',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
