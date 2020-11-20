from django.shortcuts import render, get_object_or_404
from .models import WorkoutClass, Category

# Create your views here.


def categories(request):
    """ A View to show workout categories """
    category = Category.objects.all()

    context = {
        'category': category,
    }

    return render(request, 'workout_class/workout_class_category.html', context)


def workout_class(request, category):
    """ A view to show workout classes """
    workout_class = WorkoutClass.objects.filter(category=category)   

    context = {
        'workout_class': workout_class,
    }

    return render(request, 'workout_class/workout_class.html', context)
