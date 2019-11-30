# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User

def create_users(apps, schema_editor):
    #Person = apps.get_model('canteen', 'Person')
    #person1 = Person.objects.get(pk=1)
    #person2 = Person.objects.get(pk=2)
    #person3 = Person.objects.get(pk=3)
    #person4 = Person.objects.get(pk=4)

    user1 = User.objects.create_user(username="mrkva1", password="123456", email=None)
    user2 = User.objects.create_user(username="mrkva2", password="123456")
    user3 = User.objects.create_user(username="mrkva3", password="123456")
    user4 = User.objects.create_user(username="mrkva4", password="123456")

    #user1, created = User.objects.create_user(username="mrkva1", email=None)
    #if created:
    #    print("CREATED USER")
    #    user1.set_password("123456")  # This line will hash the password

    #    user1.save()  # DO NOT FORGET THIS LINE
    #else:
    #    print("GET USER")
    #user1 = User(username="mrkva1")
    #user1.save()
    #user1.set_password("123456")
    user1.save()

    user2.save()
    user3.save()
    user4.save()

    #print(user1)
    #person1.user = user1
    #person2.user = user2
    #person3.user = user3
    #person4.user = user4

    #person1.save()
    #person2.save()
    #person3.save()
    #person4.save()


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0002_insert_initial_data'),
    ]

    operations = [
        migrations.RunPython(create_users)
    ]
