from django.contrib import admin

from sqlapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
	list_display=('name','address')

admin.site.register(Employee,EmployeeAdmin)