# Generated by Django 2.2.3 on 2019-08-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='attempt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='submission',
            name='subTime',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email1',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email2',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='latestSubTime',
            field=models.TimeField(default='00:00'),
        ),
    ]
