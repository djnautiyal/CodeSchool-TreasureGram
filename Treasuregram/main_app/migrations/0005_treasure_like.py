# Generated by Django 2.2.5 on 2019-11-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20191114_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
