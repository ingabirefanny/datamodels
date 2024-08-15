from pyclbr import Class
from rest_framework import serializers
from ClassPeriod.models import ClassPeriod
from course.models import Course
from student.models import Student
from teacher.models import Teacher
from classes.models import Classes

class StudentSerializer(serializers.ModelSerializer):
    class meta:
        model=Student
        fields= "__all__"
class ClassPeriodSerializer(serializers.ModelSerializer):
    class meta:
        model=ClassPeriod
        fields= "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class meta:
        model=Teacher
        fields= "__all__"       
class CourseSerializer(serializers.ModelSerializer):
    class meta:
        model=Course
        fields= "__all__"    

class ClassesSerializer(serializers.ModelSerializer):
    class meta:
        model=Classes
        fields= "__all__"        

