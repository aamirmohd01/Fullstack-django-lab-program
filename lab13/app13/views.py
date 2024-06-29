from django.http import HttpResponse
from django.shortcuts import render
from .models import Course, Student

def course_search_ajax(request):
    if request.method == "POST":
        cid = request.POST.get("cname")
        students = Student.objects.filter(enrolment__id=cid)
        
        if not students.exists():
            return HttpResponse("<h1>No Students enrolled</h1>")
        
        return render(request, "selected_students.html", {"student_list": students})
    
    else:
        courses = Course.objects.all()
        return render(request, "course_search_aj.html", {"courses": courses})
