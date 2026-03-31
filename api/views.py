from django.shortcuts import render,get_object_or_404
# from django.http import JsonResponse
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from chatbot.models import Patient
from rest_framework.decorators import api_view
from .serializers import PatientSerializer, StaffSerializers
from rest_framework.views import APIView
from staff.models import Staff as StaffModel
from django.http import Http404
from rest_framework import mixins, generics, views, viewsets
from rest_framework.generics import GenericAPIView
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


        
# class Staff(APIView):
#     def get(self,request):
#         staff = StaffModel.objects.all()
#         serializer = StaffSerializers(staff,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer = StaffSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    

# class StaffDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return StaffModel.objects.get(pk=pk)
#         except StaffModel.DoesNotExist:
#             raise Http404
        
#     def get(self,request,pk):
#         staff = self.get_object(pk)
#         serializer = StaffSerializers(staff)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         staff = self.get_object(pk)
#         serializer = StaffSerializers(staff,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         staff = self.get_object(pk)
#         staff.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class Staff(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = StaffModel.objects.all()
#     serializer_class = StaffSerializers

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)


# class StaffDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = StaffModel.objects.all()
#     serializer_class = StaffSerializers

#     def get(self, request, pk=None):
#         return self.retrieve(request, pk=pk)

#     def put(self, request, pk=None):
#         return self.update(request, pk=pk)

#     def delete(self, request, pk=None):
#         return self.destroy(request, pk=pk)



# class Staff(generics.ListCreateAPIView):
#     queryset = StaffModel.objects.all()
#     serializer_class = StaffSerializers


# class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StaffModel.objects.all()
#     serializer_class = StaffSerializers
#     lookup_field = 'pk'

""""viewset"""

# class Staff(viewsets.ViewSet):
#     def list(self,request):
#         queryset= StaffModel.objects.all()
#         serializer = StaffSerializers(queryset,many=True)
#         return Response(serializer.data)
    

#     def create(self,request):
#         serializers = StaffSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors)

#     def retrieve(self,request,pk=None):
#         staff = get_object_or_404(StaffModel,pk=pk)
#         serializers = StaffSerializers(staff)
#         return Response(serializers.data,status=status.HTTP_200_OK)
    
#     def delete(self,request,pk=None):
#         staff = get_object_or_404(StaffModel,pk=pk)
#         staff.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class StaffViewset(viewsets.ModelViewSet):
    queryset = StaffModel.objects.all()
    serializer_class = StaffSerializers