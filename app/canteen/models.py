from django.db import models
from datetime import datetime
from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe

from django.contrib.auth.models import User

from django.core.exceptions import PermissionDenied


class Facility (models.Model):
    id_facility = models.AutoField(primary_key=True)  # basically IntegerField but with autoincrementation so after all Primary Key
    address = models.CharField(max_length=150, blank=False)
    name = models.CharField(max_length=150, blank=False)
    deadline = models.TimeField(blank=False)
    max_ordered_meals = models.IntegerField(default=1)

    def get_absolute_url(self):
        return f"facility/{self.id_facility}"
        #return reverse("facility-view", kwargs={"id":self.id_facility})#f""

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name


class Menu (models.Model):
    id_menu = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
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
    description = models.CharField(max_length=320, blank=True, null=True)
    price = models.IntegerField(blank=False)
    #image = models.ImageField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=False, null=True)

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

    def get_absolute_url(self):
        return f"{self.id_item}"

class Person(models.Model):

    id_person = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, blank=False)
    telephone = models.CharField(max_length=25, blank=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True) #we'll use blank and null true TODO TOCHECK

    

    ROLES = (
        ('a', 'administrator'),
        ('o', 'operator'),
        ('d', 'driver'),
        ('v', 'visitor'),
        ('r', 'registered')
    )
    role = models.CharField(
        max_length=1,
        choices=ROLES,
        blank=False,
        default='v'
    )

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.surname

    def get_absolute_url(self):
        return f"{self.id_person}"

    def is_admin(self):
        if self.role == 'a' or self.role == 'o' or self.role == 'd':
            pass
        else: 
            raise PermissionDenied()
    
    def is_operator(self):
        if self.role == 'o' or self.role == 'a':
            pass        
        else: 
            raise PermissionDenied()

    def is_driver(self):
        if self.role == 'd' or self.role == 'a':
            pass        
        else: 
            raise PermissionDenied()

class Registered(models.Model):
    email = models.CharField(max_length=32, unique=True, blank=False, primary_key=True)
    profile_info = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=32, unique=True, blank=False)
    password = models.CharField(max_length=32, blank=False)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)


class Employee(models.Model):
    registered = models.OneToOneField(Registered, primary_key=True, on_delete=models.CASCADE)

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
    date_paid = models.DateTimeField(blank=True, null=True)
    date_approved = models.DateTimeField(blank=True, null=True)
    date_delivered = models.DateTimeField(blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)     #because if user isn't authenticated that's why we need it blank and null, It will be added later in the checkout 
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, blank=True, null=True) #because user can make an order just by seeing the cart and he also may remove all the items from cart and then order new items from another facility
    approved_by = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='Approved_by', blank=True, null=True)
    delivered_by = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='Delivered_by', blank=True, null=True)

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
    
    def get_absolute_url(self):
        return f"{self.id_food_order}"
        #return reverse('food_order', kwargs={'id': self.id_food_order})
    def get_absolute_url_id(self):
        return reverse('food_order', kwargs={'id': self.id_food_order})


class Roles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)


class Food_order_item(models.Model):
    id_food_order   = models.ForeignKey(Food_order, on_delete=models.CASCADE)
    id_item         = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity        = models.IntegerField(default=1)
    
    class Meta:
        unique_together = (('id_food_order', 'id_item'),)

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