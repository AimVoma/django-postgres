# Generated by Django 3.1.1 on 2020-09-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0002_sessionmodel_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='thoughtmodel',
            name='sentiment',
            field=models.IntegerField(default=-1),
        ),
    ]
