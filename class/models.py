from django.db import models

# Create your models here.
class Class (models.Model):
    class_name = models.CharField(max_length=20)
    class_teacher = models.CharField(max_length=20)
    class_capacity=models.PositiveSmallIntegerField()
    class_motto= models.CharField(max_length=20)
    class_vision= models.CharField(max_length=10)
    class_goals = models.CharField(max_length=20)
    class_equipments= models.PositiveSmallIntegerField()
    class_lessons= models.CharField(max_length=20)
    class_enrollment= models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} {self.class_capacity}"