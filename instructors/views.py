from django.shortcuts import render

# Create your views here.


def all_instructors(request):
    """ A view to return the instructors page """
    return render(request, 'instructors/instructors.html')
