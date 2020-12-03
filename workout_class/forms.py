from django import forms
from .models import WorkoutClass, Category, DifficultyLevel
from instructors.models import Instructor


class WorkoutClassForm(forms.ModelForm):

    class Meta:
        model = WorkoutClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        difficulty_level = DifficultyLevel.objects.all()
        instructor = Instructor.objects.all()
        # below is special syntax is called the list comprehension
        # and is just a shorthand way of creating a for loop that adds items to a list.
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        name = [(c.id, c.get_name()) for c in difficulty_level]
        instructor = [(c.id, c.get_name()) for c in instructor]

        self.fields['category'].choices = friendly_names
        self.fields['difficulty_level'].choices = name
        self.fields['instructor'].choices = name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border'
