from django.db import models
from django.forms import ModelForm

# Create your models here.
 
class Course(models.Model):
    course_code= models.CharField(max_length=40)
    course_name= models.CharField(max_length=100)
    course_credit = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.course_name
 
class Student(models.Model):
    student_usn = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    student_sem = models.IntegerField()
    enrolment = models.ManyToManyField(Course)
    def __str__(self):
        return self.student_name+"("+self.student_usn+")"
 