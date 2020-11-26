from django.shortcuts import render, get_object_or_404
from .models import WorkoutClass, Category

# Create your views here.


def categories(request):
    """ A View to show workout categories """
    category = Category.objects.all()

    context = {
        'category': category,
    }

    return render(request, 'workout_class/categories.html', context)


def classes(request, category):
    """ A view to show workout classes """
    workout_class = WorkoutClass.objects.filter(category=category)
    category = get_object_or_404(Category, pk=category)

    context = {
        'workout_class': workout_class,
        'category': category,
    }

    return render(request, 'workout_class/workout_class.html', context)


def class_detail(request, class_id):
    """ A view to show individual workout class details """

    workout_class = get_object_or_404(WorkoutClass, pk=class_id)

    context = {
        'workout_class': workout_class,
    }

    return render(request, 'workout_class/class_detail.html', context)
