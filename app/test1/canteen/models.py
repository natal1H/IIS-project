from django.db import models

# Create your models here.


class Facility (models.Model):
    id_facility =       models.AutoField(primary_key=True) # basically IntegerField but with autoincrementation so after all Primary Key
    address =           models.CharField(max_length=150)
    name =              models.CharField(max_length=150)
    deadline =          models.DateTimeField()
    max_ordered_meals = models.IntegerField()

class Menu (models.Model):
    type =      models.CharField(max_length=150)
    date=       models.DateTimeField()
    max_items=  models.IntegerField()

class Item(models.Model):
    diet_type =     models.CharField(max_length=50)
    name =          models.CharField(max_length=100)
    description =   models.CharField(max_length=320)
    price =         models.IntegerField()
    image =         models.ImageField()

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    surname =   models.CharField(max_length=50)
    address =   models.CharField(max_length=150)
    telephone = models.CharField(max_length=25)

class Order(models.Model):
    status = models.CharField(max_length=1)
    payment_form = models.CharField(max_length=10)

