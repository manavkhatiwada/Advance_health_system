from rest_framework import serializers
from chatbot.models import Patient
from staff.models import Staff

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'