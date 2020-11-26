from django.contrib import admin
from .models import Category, Equipment, DifficultyLevel, WorkoutClass

# Register your models here.


class WorkoutClassAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'duration',
        'class_size',
        'instructor',
        'difficulty_level',
    )

    ordering = ('difficulty_level',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Equipment,  EquipmentAdmin)
admin.site.register(DifficultyLevel)
admin.site.register(WorkoutClass, WorkoutClassAdmin)
