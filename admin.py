from django.contrib import admin

from myApp.models import*
admin.site.register(DepartmentModel)
admin.site.register(EmployeeModel)
admin.site.register(BasicInfoModel)
