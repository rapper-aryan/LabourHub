from django.contrib import admin
from .models import Users,Employees
# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','aadhar','contact','password')

@admin.register(Employees)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','fullname','email','contact','password')

