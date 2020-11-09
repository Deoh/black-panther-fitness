from django.shortcuts import render
from .models import Instructor

# Create your views here.


def all_instructors(request):
    """ A view to show all instructors """
    instructors = Instructor.objects.all()

    context = {
        'instructors': instructors,
    }

    return render(request, 'instructors/instructors.html', context)
