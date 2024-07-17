from django.shortcuts import render
from rest_framework.views import APIView
from ClassPeriod.models  import ClassPeriod
from course.models import Course
from teacher.models import Teacher
from student.models import Student
from .serializers import ClassPeriodSerializer,StudentSerializer,TeacherSerializer,CourseSerializer
from rest_framework.response import Response

class StudentListView (APIView):
    def get (self,request):
        students = Student.objects.all()
        serializer= StudentSerializer(students,many=True)
        return Response (serializer.data)
    
class ClassPeriodListView (APIView):
    def get (self,request):
        classperiod = ClassPeriod.objects.all()
        serializer= ClassPeriodSerializer(classperiod,many=True)
        return Response (serializer.data)    
    
class TeacherListView (APIView):
    def get (self,request):
        teacher = Teacher.objects.all()
        serializer= TeacherSerializer(teacher,many=True)
        return Response (serializer.data)   

class CourseListView (APIView):
    def get (self,request):
        course = Course.objects.all()
        serializer= CourseSerializer(course,many=True)
        return Response (serializer.data)       