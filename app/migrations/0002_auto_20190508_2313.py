# Generated by Django 2.2.1 on 2019-05-09 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='info',
            field=models.CharField(max_length=20),
        ),
    ]