# Generated by Django 2.1.1 on 2018-10-15 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_automation', '0003_auto_20181015_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_type',
            name='specialization',
            field=models.CharField(default='NULL', max_length=1200),
        ),
    ]
