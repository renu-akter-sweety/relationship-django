from django.db import models

class DepartmentModel(models.Model):
    dept_name = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.dept_name

class EmployeeModel(models.Model):
    DESIGNATION_TYPES = [
        ('Manager','Manager'),
        ('CEO','CEO'),
        ('Supervisor','Supervisor'),
        ('Staff','Staff'),
    ]
    name = models.CharField(max_length=200, null=True)
    employee_id=models.PositiveIntegerField(null=True, unique=True)
    dept = models.ForeignKey(DepartmentModel, on_delete=models.SET_NULL,null=True, related_name="employee_dept")
    designation = models.CharField(choices=DESIGNATION_TYPES, max_length=20, null=True)
    salary = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.name
    
class BasicInfoModel(models.Model):
    gender_type=[
        ('Male','Male'),
        ('Female','Female'),
        ('ThirdGender','ThirdGender'),
        
    ]
    employee = models.OneToOneField(EmployeeModel, on_delete=models.CASCADE, related_name='employee_info', null=True)
    email = models.EmailField(null=True)
    gender=models.CharField(choices=gender_type, max_length=20, null=True)
    address = models.TextField(null=True)
    mobile = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.employee.name