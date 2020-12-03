from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import WorkoutClass, Category
from .forms import WorkoutClassForm, EquipmentForm

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


def add_workout_class(request):
    """ Add a workout class to the website """

    if request.method == 'POST':  # post handler for the add workout class view
        form = WorkoutClassForm(request.POST, request.FILES)  # request.FILES makes sure to get the image of the class if one was submitted in POST.
        form_equipment = EquipmentForm(request.POST)
        # Class form
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Class!')
            return redirect(reverse('add_workout_class'))
        else:
            messages.error(request, 'Failed to add Class. Please ensure the form is valid.')
        # Equipment form
        if form_equipment.is_valid():
            form_equipment.save()
            messages.success(request, 'Successfully added Equipment!')
            return redirect(reverse('add_workout_class'))
        else:
            messages.error(request, 'Failed to add Equipment. Please ensure the form is valid.')
    else:
        form = WorkoutClassForm()
        form_equipment = EquipmentForm()

    template = 'workout_class/add_workout_class.html'
    context = {
        'form': form,
        'form_equipment': form_equipment,
    }

    return render(request, template, context)


def edit_workout_class(request, workout_class_id):
    """ Edit a workout_class in the store """
    workout_class = get_object_or_404(WorkoutClass, pk=workout_class_id)

    if request.method == 'POST':
        form = WorkoutClassForm(request.POST, request.FILES, instance=workout_class)
        # Class form
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workout_class!')
            return redirect(reverse('workout_class_detail', args=[workout_class.id]))
        else:
            messages.error(request, 'Failed to update workout_class. Please ensure the form is valid.')
    else:
        form = WorkoutClassForm(instance=workout_class)
        messages.info(request, f'You are editing {workout_class.name}')

    template = 'workout_classs/edit_workout_class.html'
    context = {
        'form': form,
        'workout_class': workout_class,
    }

    return render(request, template, context)
