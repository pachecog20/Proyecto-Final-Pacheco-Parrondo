# Generated by Django 4.2 on 2023-06-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacionextra',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
