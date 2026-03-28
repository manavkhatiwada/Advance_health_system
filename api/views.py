# from django.shortcuts import render
# from django.http import JsonResponse
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from chatbot.models import Patient
from rest_framework.decorators import api_view
from .serializers import PatientSerializer


# def students(request):
#     students = {'id': 1, 'name': 'John Doe', 'age': 20, 'grade': 'A'}
#     return JsonResponse(students)

# Create your views here.
@api_view(['GET', 'POST'])
def students(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = serializers.PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def patientDetailView(request,pk):
        try :
            patient = Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = PatientSerializer(patient)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            serializer = PatientSerializer(patient,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

        elif request.method == 'DELETE':
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


        



