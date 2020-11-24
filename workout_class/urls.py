from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<category>', views.classes, name='classes'),
    path('class/<class_id>', views.class_detail, name='class_detail'),
]
