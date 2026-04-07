from django.urls import path,include

from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('staff',views.Staff,basename='staff')
router.register('staff', views.StaffViewset, basename='staff')

urlpatterns = [
    path('students/',views.students),
    path('students/<int:pk>/',views.patientDetailView),
    # path('staff/',views.Staff.as_view()),  
    # path('staff/<int:pk>',views.StaffDetail.as_view())

    path('',include(router.urls)),
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
]