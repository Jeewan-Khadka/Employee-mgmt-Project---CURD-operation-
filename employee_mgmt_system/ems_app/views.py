from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html')

def view_emp(request):
    emps=Employee.objects.all()
    context={
        'emps' : emps
    }
    return render(request,'view_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        hire_date=request.POST['hire_date']
        new_emp=Employee(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary, 
                         bonus=bonus, role_id=role, phone=phone, hire_date=hire_date)
        new_emp.save()
        return HttpResponse('<h1 style="text-align: center;">Employee detail added successfully</h1>')
    elif request.method=='GET':
       return render(request,'add_emp.html')
   
    else:
        return HttpResponse('exception')

def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            employee_to_be_removed=Employee.objects.get(id=emp_id)
            employee_to_be_removed.delete()
            return HttpResponse('<h1>Employee deleted successfully</h1>')
        except:
            return HttpResponse('plz enter valid id')
    
    emps=Employee.objects.all()
    contex={
        'emps': emps
    }

    return render(request,'remove_emp.html',contex)

def filter_emp(request):
    if request.method == 'POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps= emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))

        if dept:
            emps = emps.filter(dept__name = dept)

        if role:
            emps = emps.filter(role__name = role)   

        context = {
            'emps': emps
        } 
        return render(request,'view_emp.html',context) 

    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    
    else:
        return HttpResponse('An exception occured')
    
    
        