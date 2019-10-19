from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Facility)
admin.site.register(Menu)
admin.site.register(Item)
admin.site.register(Person)
admin.site.register(Order)