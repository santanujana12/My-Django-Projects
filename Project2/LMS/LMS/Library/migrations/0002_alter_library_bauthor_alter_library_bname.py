# Generated by Django 4.0.3 on 2022-04-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='bauthor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='library',
            name='bname',
            field=models.CharField(max_length=30),
        ),
    ]
