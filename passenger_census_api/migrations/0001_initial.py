# Generated by Django 2.0.1 on 2018-05-22 03:12

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerCensus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_begin_date', models.DateField(blank=True, null=True)),
                ('route_number', models.IntegerField(blank=True, null=True)),
                ('direction', models.IntegerField(blank=True, null=True)),
                ('service_key', models.TextField(blank=True, null=True)),
                ('stop_seq', models.IntegerField(blank=True, null=True)),
                ('location_id', models.IntegerField(blank=True, null=True)),
                ('public_location_description', models.TextField(blank=True, null=True)),
                ('ons', models.IntegerField(blank=True, null=True)),
                ('offs', models.IntegerField(blank=True, null=True)),
                ('x_coord', models.FloatField(blank=True, null=True)),
                ('y_coord', models.FloatField(blank=True, null=True)),
                ('geom_2913', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'passenger_census',
                'managed': False,
            },
        ),
    ]
