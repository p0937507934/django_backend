# Generated by Django 3.0.5 on 2020-05-18 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20200424_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='Measurement_Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]