from django.db import models

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


class Instructor(models.Model):
    category = models.ManyToManyField('Category')
    name = models.CharField(max_length=254)
    qualification = models.CharField(max_length=254)
    qualification_date = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
