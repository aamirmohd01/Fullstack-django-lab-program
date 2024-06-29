from django.shortcuts import render

# Create your views here.
def showlist(request):
    students = ['Aamir', 'Ketan', 'Abhishek', 'Aadarsh', 'Prajwal']
    fruits = ['Mango', 'Banana', 'Apple', 'Guava', 'Jamun']
    return render(request, 'list.html', {"fruits":fruits, "students":students})