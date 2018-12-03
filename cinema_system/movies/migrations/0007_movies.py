# Generated by Django 2.1 on 2018-12-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20181202_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('title', models.CharField(blank=True, default='', max_length=50, primary_key=True, serialize=False)),
                ('releaseDate', models.CharField(blank=True, default='', max_length=50)),
                ('director', models.CharField(blank=True, default='', max_length=50)),
                ('summary', models.CharField(blank=True, default='', max_length=550)),
                ('poster', models.CharField(blank=True, default='', max_length=50)),
                ('rating', models.CharField(blank=True, default='', max_length=10)),
                ('modelType', models.CharField(blank=True, default='', max_length=20)),
            ],
        ),
    ]
