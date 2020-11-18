from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workout_class, name='workout_class'),
]
