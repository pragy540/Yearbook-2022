from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
  list = ('name', 'rollno')

admin.site.register(Profile, ProfileAdmin)