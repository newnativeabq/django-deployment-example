from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=128, unique=True)
    size = models.PositiveIntegerField()
    site = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:school_detail", kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=128, unique=True)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete='CASCADE')

    def __str__(self):
        rstr = ' '.join([self.name,'(', str(self.age), ')'])
        return rstr

