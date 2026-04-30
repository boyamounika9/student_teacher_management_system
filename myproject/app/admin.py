from django.contrib import admin

# Register your models here.
from . models import student

admin.site.register(student)





from . models import teacher

admin.site.register(teacher)