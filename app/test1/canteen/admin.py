from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Facility)
admin.site.register(Menu)
admin.site.register(Item)
admin.site.register(Person)
admin.site.register(Registered)
admin.site.register(Employee)
admin.site.register(Food_order)
admin.site.register(Facility_menus)
admin.site.register(Menu_items)

admin.site.register(Roles)

admin.site.register(testItem)
admin.site.register(testOrder)


"""
admin,
operator, 
vodic,
stravnik

neregistrovany

->Create an extra table to store the users types and add M:M field to user model

Authentication(Login)
Authorization(Permission)


"""