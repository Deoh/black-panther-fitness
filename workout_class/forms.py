from django import forms
from .models import WorkoutClass, Category, DifficultyLevel, Equipment
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
        name = [(c.id, c.name) for c in difficulty_level]
        name2 = [(c.id, c.name) for c in instructor]

        self.fields['category'].choices = friendly_names
        self.fields['difficulty_level'].choices = name
        self.fields['instructor'].choices = name2
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border'


class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border'
