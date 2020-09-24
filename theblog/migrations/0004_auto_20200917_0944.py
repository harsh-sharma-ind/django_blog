# Generated by Django 3.1.1 on 2020-09-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
