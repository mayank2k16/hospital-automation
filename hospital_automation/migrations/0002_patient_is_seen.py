# Generated by Django 2.1.1 on 2018-10-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_automation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]
