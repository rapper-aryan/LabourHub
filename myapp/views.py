from django.shortcuts import render,redirect
from .forms import LabourRegistration,EmployeeRegistration
from .models import Users,Employees
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User,auth

#view for reguiater page
def HomePage(request):
    return render(request,'home.html')

def AboutPage(request):
    return render(request,'about.html')

def BookingPage(request):
    emp=Users.objects.all()

    context={
        'emp':emp,
    }
    return render(request,'booking.html',context)

def EmpLoginPage(request):
    return render(request, 'emplogin.html')

def EmpRegisterPage(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        emp = Employees(
            fullname=fullname,
            email=email,
            contact=contact,
            password=password
        )

        emp.save()
        return redirect('/emplogin/')

    return render(request, 'empregister.html')


def LoginPage(request):
    if request.method == 'POST':
        aadhar = request.POST['aadhar']
        password = request.POST['password']

        user = authenticate(request, aadhar=aadhar, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect('/home/')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/log/')
    else:
        return render(request, 'log.html')


def RegisterPage(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        aadhar = request.POST.get('aadhar')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        usr = Users(
            fullname=fullname,
            aadhar=aadhar,
            contact=contact,
            password=password
        )

        usr.save()
        return redirect('/log/')

    return render(request, 'register.html')


def ManageLab(request):
    emp=Users.objects.all()

    context={
        'emp':emp,
    }
    return render(request,'managelab.html',context)

def Add(request):
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        aadhar=request.POST.get('aadhar')
        contact=request.POST.get('contact')
        password=request.POST.get('password')

        emp=Users(
            fullname=fullname,
            aadhar=aadhar,
            contact=contact,
            password=password
        )

        emp.save()
        return redirect('managelab')

    return render(request, 'managelab.html')

def Edit(request):
    emp = Users.objects.all()

    context = {
        'emp': emp,
    }
    return redirect(request, 'managelab', context)


def Update(request,id):
    if request.method=='POST':
        fullname = request.POST.get('fullname')
        aadhar = request.POST.get('aadhar')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        emp = Users(
            id=id,
            fullname=fullname,
            aadhar=aadhar,
            contact=contact,
            password=password
        )
        emp.save()
        return redirect('managelab')


    return redirect(request,'managelab.html')

def Delete(request,id):
    emp=Users.objects.filter(id = id)
    emp.delete()


    context = {
        'emp': emp,
    }
    return redirect('managelab')




def ManageEmp(request):
    em=Employees.objects.all()

    context={
        'em':em,
    }
    return render(request,'manageemp.html',context)


def AddEmp(request):
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        password=request.POST.get('password')

        em=Employees(
            fullname=fullname,
            email=email,
            contact=contact,
            password=password
        )

        em.save()
        return redirect('manageemp')

    return render(request, 'manageemp.html')

def EditEmp(request):
    em = Employees.objects.all()

    context = {
        'em': em,
    }
    return redirect(request, 'manageemp', context)


def UpdateEmp(request,id):
    if request.method=='POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        em = Employees(
            id=id,
            fullname=fullname,
            email=email,
            contact=contact,
            password=password
        )
        em.save()
        return redirect('manageemp')


    return redirect(request,'manageemp.html')

def DeleteEmp(request,id):
    em=Employees.objects.filter(id = id)
    em.delete()


    context = {
        'em': em,
    }
    return redirect('manageemp')



