from django.db import models
from datetime import datetime
from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe

# Create your models here.

from django.contrib.auth.models import User



class Facility (models.Model):
    id_facility = models.AutoField(primary_key=True)  # basically IntegerField but with autoincrementation so after all Primary Key
    address = models.CharField(max_length=150, blank=False)
    name = models.CharField(max_length=150, blank=False)
    deadline = models.TimeField(blank=False)
    max_ordered_meals = models.IntegerField(default=1)

    def get_absolute_url(self):
        return f"facility/{self.id_facility}"
        #return reverse("facility-view", kwargs={"id":self.id_facility})#f""

class testItem(models.Model):
    id_testItem = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    Facility = models.ForeignKey(Facility, on_delete=models.CASCADE)


class testOrder(models.Model):
    id_order =models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    testItem = models.ForeignKey(testItem, on_delete=models.CASCADE)

class Menu (models.Model):
    id_menu = models.AutoField(primary_key=True)
    date = models.DateField()
    max_items = models.IntegerField(default=10)

    MENU_TYPES = (
        ('d', 'Daily'),   # Changes every day
        ('s', 'Static'),  # Doesn't change
    )

    type = models.CharField(
        max_length=1,
        choices=MENU_TYPES,
        default='s',  # By default will be static menu
    )


class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=320, blank=True)
    price = models.IntegerField(blank=False)
    image = models.ImageField(blank=True)

    DIET_TYPES = (
        ('n', 'normal'),
        ('v', 'vegetarian'),
        ('g', 'gluten-free'),
    )

    diet_type = models.CharField(
        max_length=1,
        choices=DIET_TYPES,
        default='n',
    )


"""
admin,
operator, 
vodic,
stravnik

neregistrovany

Authentication(Login)
Authorization(Permission)

class User_model(AbstractUser):
    is_student  = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    is_driver   = models.BooleanField(default=False)
    is_client   = models.BooleanField(default=False) #stravník
"""




class Person(models.Model):
    id_person = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, blank=False)
    telephone = models.CharField(max_length=25, blank=False)


class Registered(models.Model):
    email = models.CharField(max_length=32, unique=True, blank=False, primary_key=True)
    profile_info = models.CharField(max_length=300)
    image = models.ImageField(max_length=50)
    login = models.CharField(max_length=32, unique=True, blank=False)
    password = models.CharField(max_length=32, blank=False)
    Person = models.OneToOneField(Person, on_delete=models.CASCADE)


class Employee(models.Model):
    Registered = models.OneToOneField(Registered, primary_key=True, on_delete=models.CASCADE)

    ROLES = (
        ('a', 'administrator'),
        ('o', 'operator'),
        ('d', 'driver')
    )

    role = models.CharField(
        max_length=1,
        choices=ROLES,
        blank=False,
    )


class Food_order(models.Model):
    id_food_order = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(default=datetime.now)
    date_paid = models.DateTimeField()
    date_approved = models.DateTimeField()
    date_delivered = models.DateTimeField()
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    Approved_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Approved_by')
    Delivered_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Delivered_by')

    FOOD_ORDER_STATUS = (
        ('o', 'ordered'),
        ('a', 'approved'),
        ('c', 'canceled'),
        ('d', 'delivered'),
    )

    PAYMENT_FORM = (
        ('m', 'meal ticket'),
        ('n', 'card now'),
        ('d', 'card on delivery'),
        ('h', 'cash on delivery'),
    )

    status = models.CharField(
        max_length=1,
        choices=FOOD_ORDER_STATUS,
        default='o',
    )

    payment_form = models.CharField(
        max_length=1,
        choices=PAYMENT_FORM,
        default='h',
    )
class Roles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver= models.BooleanField(default=False)
    is_operator =models.BooleanField(default=False)



class Facility_menus(models.Model):
    id_facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_facility', 'id_menu'),)


class Menu_items(models.Model):
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    id_item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_menu', 'id_item'),)