from ctypes.wintypes import tagSIZE
from typing_extensions import Self
from unicodedata import category
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.TextField()

    def __str__(self) :
        return self.name , self.description , self.image 

class Course(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.name 


    
class Lecture(models.Model):
    name = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)  # FK act as a cloumn 
    def __str__(self):
        return self.name


class Slide(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return self.name


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, related_name="tags")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



