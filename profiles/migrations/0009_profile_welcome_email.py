# Generated by Django 3.1.6 on 2021-03-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20210303_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='welcome_email',
            field=models.BooleanField(default=False),
        ),
    ]
