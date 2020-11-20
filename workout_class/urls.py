from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<category>', views.workout_class, name='workout_class'),
]
