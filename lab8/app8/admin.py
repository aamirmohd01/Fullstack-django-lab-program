from django.contrib import admin
from app8.models import Course, Student

# Register your models here.
#admin.site.register(Students)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ordering=('student_name',)
    search_fields = ('student_name',)
   
admin.site.register(Course)




