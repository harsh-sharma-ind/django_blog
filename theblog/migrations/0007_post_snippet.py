# Generated by Django 3.1.1 on 2020-09-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20200919_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read blog post...', max_length=255),
        ),
    ]
