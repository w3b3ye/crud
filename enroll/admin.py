from django.contrib import admin
from .models import User
from enroll import models

# Register your models here.
#@admin.register(User) #This is called decorators. You can use this or do as mention on line 11 to register with admin portal.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    search_fields = ('email', 'name')

admin.site.register(User, UserAdmin)