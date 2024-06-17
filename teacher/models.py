from django.db import models

# Create your models here.

class Teacher (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    year_of_birth=models.DateField(max_length=10)
    nationality= models.CharField(max_length=20)
    gender= models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    teacher_id= models.PositiveSmallIntegerField()
    course= models.CharField(max_length=20)
    years_of_experience= models.PositiveSmallIntegerField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"