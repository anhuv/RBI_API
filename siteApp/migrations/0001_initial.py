# Generated by Django 3.2.5 on 2021-07-11 12:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('siteid', models.AutoField(db_column='SiteID', primary_key=True, serialize=False)),
                ('sitename', models.CharField(blank=True, db_column='SiteName', max_length=100, null=True)),
                ('create', models.DateTimeField(db_column='Create', default=datetime.datetime(2021, 7, 11, 19, 51, 48, 675155))),
                ('userID', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sites',
                'ordering': ('siteid',),
                'managed': True,
            },
        ),
    ]