#from django.shortcuts import render 
from django.views import generic
from app10.models import Student
 
# Create your views here.
class StudentListView(generic.ListView):
    model=Student
    template_name="student_list.html"

class StudentDetailView(generic.DetailView):
    model=Student
    template_name="student_detail.html"