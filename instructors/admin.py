from django.contrib import admin
from .models import Instructor, Category

# Register your models here.


class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'qualification',
        'qualification_date',
        'price',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Category, CategoryAdmin)
