from django.http import HttpResponse
from django.shortcuts import render
from chatbot.models import Patient

def home(request):
    patients = Patient.objects.all()
    context = {
        'patients': patients,
    }
    return render(request,'home.html',context)