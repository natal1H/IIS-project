# Generated by Django 2.2.2 on 2019-11-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0004_auto_20191127_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('a', 'administrator'), ('o', 'operator'), ('d', 'driver'), ('v', 'visitor'), ('r', 'registered')], default='v', max_length=1),
        ),
    ]
