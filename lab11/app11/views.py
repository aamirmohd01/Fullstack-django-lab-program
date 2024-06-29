from django.http import HttpResponse
from app11.models import Course
import csv
from reportlab.pdfgen import canvas

def construct_csv_from_model(request):
    courses = Course.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courses_data.csv"'

    writer = csv.writer(response)
    writer.writerow(["CourseName", "CourseCode", "Credits"])

    for course in courses:
        writer.writerow([course.course_name, course.course_code, course.course_credits])

    return response

def construct_pdf_from_model(request):
    courses = Course.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="courses_data.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, "Courses List")

    y = 750
    for course in courses:
        p.drawString(100, y, f"Course Name: {course.course_name}, Code: {course.course_code}, Credits: {course.course_credits}")
        y -= 20

    p.showPage()
    p.save()

    return response
