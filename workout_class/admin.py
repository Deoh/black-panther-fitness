from django.contrib import admin
from .models import Category, Equipment, DifficultyLevel, WorkoutClass

# Register your models here.

admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(DifficultyLevel)
admin.site.register(WorkoutClass)
