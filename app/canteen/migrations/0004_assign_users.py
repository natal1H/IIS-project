# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
#from django.contrib.auth.models import User

def assign_users(apps, schema_editor):
    User = apps.get_model('auth', 'user')
    Person = apps.get_model('canteen', 'Person')
    person1 = Person.objects.get(pk=1)
    person2 = Person.objects.get(pk=2)
    person3 = Person.objects.get(pk=3)
    person4 = Person.objects.get(pk=4)

    user1 = User.objects.get(username="mrkva1")
    user2 = User.objects.get(username="mrkva2")
    user3 = User.objects.get(username="mrkva3")
    user4 = User.objects.get(username="mrkva4")

    person1.user = user1
    person2.user = user2
    person3.user = user3
    person4.user = user4

    person1.save()
    person2.save()
    person3.save()
    person4.save()

class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0003_create_users'),
    ]

    operations = [
        migrations.RunPython(assign_users)
    ]
