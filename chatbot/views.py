from django.shortcuts import get_object_or_404, render

from chatbot.models import Patient
from django.http import HttpResponse
# Create your views here.
# from django.shortcuts import render
# from .models import Patient

# def home(request):
#     patients = Patient.objects.all()
#     context = {
#         'patients': patients
#     }
#     return render(request, 'home.html', context)


def patient_detail(request,pk):
    patient = get_object_or_404(Patient, pk=pk)
    context = {
        'patient': patient
    }
    return render(request,'Patient_details.html',context) 
