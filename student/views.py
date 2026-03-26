from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = {'id': 1, 'name': 'John Doe', 'age': 20, 'grade': 'A'}
    return HttpResponse(f"Student Info: {students['name']}, Age: {students['age']}, Grade: {students['grade']}")
    