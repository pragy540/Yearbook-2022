from django.contrib import admin

# Register your models here.
from . import models

# class ProfileAdmin(admin.ModelAdmin):
#   list = ('name', 'rollno')

# admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Student)
admin.site.register(models.Student_Profile)