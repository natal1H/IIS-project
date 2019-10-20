# Generated by Django 2.2.6 on 2019-10-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_info', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='')),
                ('email', models.CharField(max_length=32)),
                ('login', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]
