# Generated by Django 4.0 on 2022-01-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_show_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='episodes',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='show',
            name='progress',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='show',
            name='runtime',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='show',
            name='timestop',
            field=models.CharField(max_length=20),
        ),
    ]
