from django.db import models

# Create your models here.
class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=40)
    classroom = models.CharField(max_length=30)
    day_of_week = models.CharField(max_length=50)

    def __str__(self):
        return self.classroom
    

