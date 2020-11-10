from django.shortcuts import render, get_object_or_404
from .models import Instructor

# Create your views here.


def all_instructors(request):
    """ A view to show all instructors """
    instructors = Instructor.objects.all()

    context = {
        'instructors': instructors,
    }

    return render(request, 'instructors/instructors.html', context)


def instructor_detail(request, instructor_id):
    """ A view to show instructor details """

    instructor = get_object_or_404(Instructor, pk=instructor_id)

    context = {
        'instructor': instructor,
    }

    return render(request, 'instructors/instructor_detail.html', context)
