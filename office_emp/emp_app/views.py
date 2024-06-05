from django.shortcuts import render,HttpResponse
from .models import Department,Employee,Role
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(requests):
    return render(requests,"index.html")

def view_emp(requests):
    emps= Employee.objects.all()
    context = {
        "emps": emps
    }
    # print(context)
    return render(requests,"view_emp.html",context)

def add_emp(requests):
    if requests.method=="POST":
        first_name= requests.POST["first_name"]
        last_name= requests.POST["last_name"]
        dept=int(requests.POST["dept"])
        role=int(requests.POST["role"])
        phone=int(requests.POST["phone"])
        salary=int(requests.POST["salary"])
        bonus=int(requests.POST["bonus"])
       
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,role_id=role,phone=phone,salary=salary,bonus=bonus,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully!")
    elif requests.method=="GET":

        return render(requests,"add_emp.html")    
    else:
        print("An Exception Occured! Employee has not been added.")


def rem_emp(requests,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!")
        except:
            return HttpResponse("Please Enter a Valid EMP ID")
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    return render(requests,"rem_emp.html",context)

def filter_detail(requests):
    if requests.method=="POST":
        name=requests.POST["name"]
        dept=requests.POST["dept"]
        role=requests.POST["role"]
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)| Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)

        context={
            "emps":emps
        }
        return render(requests,"view_emp.html",context)
    elif requests.method=="GET":
        return render(requests,"filter_detail.html")

    
    
    