# Generated by Django 3.1.6 on 2021-03-01 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210228_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='InTransit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='earnings',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='packages_ready',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='signees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]