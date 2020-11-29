from django.db import models
from instructors.models import Instructor

# Create your models here.


class Category(models.Model):

    class Meta:  # fix 'categorys' name in admin to 'categories'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Equipment(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name


class DifficultyLevel(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.name


class WorkoutClass(models.Model):
    model_id = models.CharField(
        max_length=20, default='workout_class', editable=False)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    duration = models.DurationField()
    instructor = models.ForeignKey(
        Instructor, null=True, blank=True, on_delete=models.SET_NULL)
    class_size = models.PositiveSmallIntegerField()
    equipment = models.ManyToManyField(
        'Equipment', blank=True)
    difficulty_level = models.ForeignKey(
        'DifficultyLevel', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
