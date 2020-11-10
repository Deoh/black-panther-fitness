from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_instructors, name='instructors'),
    path('<instructor_id>', views.instructor_detail, name='instructor_detail'),
]
