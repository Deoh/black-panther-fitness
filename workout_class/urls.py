from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('classes/<int:category>/', views.classes, name='classes'),
    path('class_detail/<class_id>', views.class_detail, name='class_detail'),
    path('add/', views.add_workout_class, name='add_workout_class'),
    path('edit/<int:workout_class_id>/',
         views.edit_workout_class, name='edit_workout_class'),
    path('delete/<int:workout_class_id>/', views.delete_workout_class, name='delete_workout_class'),
]
