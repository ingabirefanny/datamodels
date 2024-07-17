from django.db import models


class Course (models.Model):
    course_name = models.CharField(max_length=20)
    course_trainer = models.CharField(max_length=20)
    course_careers=models.EmailField()
    course_id= models.PositiveSmallIntegerField()
    course_description= models.CharField(max_length=20)
    course_scores = models.PositiveSmallIntegerField()
    course_duration= models.DurationField()
    course_sessions= models.CharField(max_length=20)
    course_students= models.PositiveSmallIntegerField()
    def __str__(self):
        return f"{self.name} {self.trainer}"