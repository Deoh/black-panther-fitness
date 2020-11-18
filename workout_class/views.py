from django.shortcuts import render, get_object_or_404
# from .models import WorkoutClass

# Create your views here.


def all_workout_class(request):
    # """ A view to show all workout classes """
    # workout_class = WorkoutClass.objects.all()

    # context = {
    #     'workout_class': workout_class,
    # }

    return render(request, 'workout_class/workout_class.html')
