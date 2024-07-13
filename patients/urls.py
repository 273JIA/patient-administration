from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Native path to access the django admin
    path('admin/', admin.site.urls),
    # Path to access the frontend page
    path('', views.frontend, name="frontend"),
    # Path to login / logout
    path('login/', include('django.contrib.auth.urls')),

    # --------------------- BACKEND SECTION ---------------------|
    # Path to Access the backend page
    path('backend/', views.backend, name="backend"),
    # Path to Add patient
    path('add_patient', views.add_patient, name="add_patient"),
    # Path to Access the patient individually
    path('patient/<str:patient_id>', views.patient, name="patient"),
    # Path to Edit patient
    path('edit_patient', views.edit_patient, name="edit_patient"),
    # Path to Delete the patient
    path('delete_patient/<str:patient_id>', views.delete_patient, name="delete_patient"),

    # Support
    path('support', views.support, name="support"),
]