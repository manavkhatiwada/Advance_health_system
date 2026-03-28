from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    photo = models.CharField(max_length=500, blank=True, null=True)  # Changed to CharField for path string
    designation = models.CharField(max_length=100)
    email_adress = models.EmailField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name
