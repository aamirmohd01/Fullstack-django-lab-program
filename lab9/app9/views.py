from django.http import HttpResponse
from django.shortcuts import render
from app9.models import ProjectReg

def add_project(request):
    if request.method == "POST":
        form=ProjectReg(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Record inserted successfully</h1>")
        else:
            return HttpResponse("<h1>Record not inserted</h1>")
    else:
        form=ProjectReg()
        return render(request,"add_project.html",{"form":form})