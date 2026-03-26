from django.shortcuts import render
from django.http import JsonResponse

def students(request):
    students = {'id': 1, 'name': 'John Doe', 'age': 20, 'grade': 'A'}
    return JsonResponse(students)

# Create your views here.
