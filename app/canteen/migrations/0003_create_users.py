# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User


def create_users(apps, schema_editor):
    user1 = User.objects.create_user(username="mrkva1", password="123456", email=None)
    user2 = User.objects.create_user(username="mrkva2", password="123456")
    user3 = User.objects.create_user(username="mrkva3", password="123456")
    user4 = User.objects.create_user(username="mrkva4", password="123456")

    user1.save()
    user2.save()
    user3.save()
    user4.save()


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0002_insert_initial_data'),
    ]

    operations = [
        migrations.RunPython(create_users)
    ]
