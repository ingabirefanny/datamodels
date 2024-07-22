from django.shortcuts import render
from rest_framework.views import APIView
from ClassPeriod.models  import ClassPeriod
from course.models import Course
from teacher.models import Teacher
from student.models import Student
from rest_framework import status
from .serializers import ClassPeriodSerializer,StudentSerializer,TeacherSerializer,CourseSerializer
from rest_framework.response import Response

class StudentListView (APIView):
    def get (self,request):
        students = Student.objects.all()
        serializer= StudentSerializer(students,many=True)
        return Response (serializer.data)
    

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
        

class StudentDetailView(APIView):
    def get(self,request, id):
        student= Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,id):
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        student=Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)   
    

    
class ClassPeriodListView (APIView):
    def get (self,request):
        classperiod = ClassPeriod.objects.all()
        serializer= ClassPeriodSerializer(classperiod,many=True)
        return Response (serializer.data)    
    
    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
        

class ClassPeriodDetailView(APIView):
    def get(self,request, id):
        classperiod= ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)

    def put(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        serializer=ClassPeriodSerializer(classperiod,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        classperiod=ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response(status=status.HTTP_202_ACCEPTED)   
    
    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
        


    
class TeacherListView (APIView):
    def get (self,request):
        teacher = Teacher.objects.all()
        serializer= TeacherSerializer(teacher,many=True)
        return Response (serializer.data)   
    


    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
        

class TeacherDetailView(APIView):
    def get(self,request, id):
        teacher= Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self,request,id):
        teacher=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,id):
        teacher=Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)   
    
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
        

class CourseListView (APIView):
    def get (self,request):
        course = Course.objects.all()
        serializer= CourseSerializer(course,many=True)
        return Response (serializer.data)       
    

    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)
        

class CourseDetailView(APIView):
    def get(self,request, id):
        course= Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self,request,id):
        course=Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        course=Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)   
    
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_CREATED)