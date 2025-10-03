from django.shortcuts import render,redirect
from myApp.models import*

def homePage(request):
    
    return render(request,"home.html")
def employeePage(request):
    if request.method == "POST":
        name=request.POST.get('name')
        employee_id=request.POST.get('employee_id')
        designation=request.POST.get('designation')
        salary=request.POST.get('salary')
        dept=request.POST.get('dept')
        dept_data=DepartmentModel.objects.get(id=dept)
        
        EmployeeModel.objects.create(
                name=name,
                employee_id=employee_id,
                dept=dept_data,
                designation=designation,
                salary=salary
        )
        
        return redirect('employee')
    dept_data=DepartmentModel.objects.all()
    employee_data=EmployeeModel.objects.all()
    context={
        "dept_data":dept_data,
        "employee_data":employee_data
    }
    return render(request,"employee.html",context)
def infoPage(request):
    if request.method == "POST":
        employee=request.POST.get('employee')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        
        emp=EmployeeModel.objects.get(id=employee)
        BasicInfoModel.objects.create(
            employee=emp,
            gender=gender,
            email=email,
            mobile=mobile,
            address=address
        )
    employee_data=EmployeeModel.objects.all()
    info_data=BasicInfoModel.objects.all()
    context={
        "employee_data":employee_data,
        "info_data":info_data
    }
    return render(request,"info.html",context)