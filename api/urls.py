from django.urls import path

from . import views

urlpatterns = [
    path('students/',views.students),
    path('students/<int:pk>/',views.patientDetailView),
    path('staff/',views.Staff.as_view()),  # TODO: Create Staff view
    path('staff/<int:pk>',views.StaffDetail.as_view())
]