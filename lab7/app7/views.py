from django.shortcuts import render
from django.http import HttpResponse
from app7.models import Course, Students
 
# Create your views here.
def reg(request):
    if request.method == "POST":
        sid = request.POST.get("sname")
        cid = request.POST.get("cname")
        student = Students.objects.get(id=sid)
        course = Course.objects.get(id=cid)
        res = student.enrolment.filter(id=cid)
        if res:
            return HttpResponse("<h1>Student already enrolled</h1>")
        student.enrolment.add(course)
        return HttpResponse("<h1>Student enrolled successfully<h1>")
    else:
        students = Students.objects.all()
        courses = Course.objects.all()
        return render(request, "reg.html", {"students":students, "courses":courses})
    
