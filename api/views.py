# from django.shortcuts import render
# from django.http import JsonResponse
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from chatbot.models import Patient
from rest_framework.decorators import api_view



# def students(request):
#     students = {'id': 1, 'name': 'John Doe', 'age': 20, 'grade': 'A'}
#     return JsonResponse(students)

# Create your views here.
@api_view(['GET'])
def students(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = serializers.PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


