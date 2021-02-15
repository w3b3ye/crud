from django.http import request
from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    """Function to add and show all items."""
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            #First method of saving the form data in DB.
            #fm.save() 
            #Second method of saving the form data in DB.
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})

def delete_items(request, id):
    """Function to delete data."""
    if request.method == 'POST':
        dl = User.objects.get(pk=id)
        dl.delete()
        return redirect('addandshow')

def update_items(request, id):
    """Function to update data."""
    if request.method == 'POST':
        dt = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
    else:
        dt = User.objects.get(pk=id)
        fm = StudentRegistration(instance=dt)

    return render(request, 'enroll/updatestudent.html', {'form':fm})

