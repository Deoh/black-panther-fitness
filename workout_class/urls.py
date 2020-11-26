from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('classes/<category>', views.classes, name='classes'),
    path('class_detail/<class_id>', views.class_detail, name='class_detail'),
]
