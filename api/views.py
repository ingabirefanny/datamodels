
from django.shortcuts import render
from django.utils.module_loading import import_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from student.models import Student
from course.models import Course
from classes.models import Classes

from teacher.models import Teacher
from ClassPeriod .models import ClassPeriod
from .serializers import StudentSerializer

from .serializers import (
   CourseSerializer,
   ClassesSerializer,
   TeacherSerializer,
   ClassPeriodSerializer
)

class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def put(self, request, id):
       student = Student.objects.get(id=id)
       serializer = StudentSerializer(student, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
       student = Student.objects.get(id=id)
       student.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request, id):
       action = request.data.get('action')


       if action == 'add_to_class':
           return self.add_student_to_class(request, id)
       elif action == 'assign_teacher_course':
           return self.assign_teacher_course(request)
       elif action == 'assign_teacher_class':
           return self.assign_teacher_class(request)
       elif action == 'create_class_period':
           return self.create_class_period(request)
       elif action == 'get_weekly_timetable':
           return self.get_weekly_timetable(request)
       else:
           return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)


    def add_student_to_class(self, request, student_id):
       class_id = request.data.get('class_id')
       try:
           student = Student.objects.get(id=student_id)
           class_obj = Classes.objects.get(id=class_id)
           class_obj.students.add(student)
           return Response({"message": "Student added to class successfully"}, status=status.HTTP_200_OK)
       except (Student.DoesNotExist, Classes.DoesNotExist):
           return Response({"error": "Student or Class not found"}, status=status.HTTP_404_NOT_FOUND)


    def assign_teacher_course(self, request):
       teacher_id = request.data.get('teacher_id')
       course_id = request.data.get('course_id')
       try:
           teacher = Teacher.objects.get(id=teacher_id)
           course = Course.objects.get(id=course_id)
           teacher.courses.add(course)
           return Response({"message": "Teacher assigned to course successfully"}, status=status.HTTP_200_OK)
       except (Teacher.DoesNotExist, Course.DoesNotExist):
           return Response({"error": "Teacher or Course not found"}, status=status.HTTP_404_NOT_FOUND)


    def assign_teacher_class(self, request):
       teacher_id = request.data.get('teacher_id')
       class_id = request.data.get('class_id')
       try:
           teacher = Teacher.objects.get(id=teacher_id)
           class_obj = Classes.objects.get(id=class_id)
           class_obj.teacher = teacher
           class_obj.save()
           return Response({"message": "Teacher assigned to class successfully"}, status=status.HTTP_200_OK)
       except (Teacher.DoesNotExist, Classes.DoesNotExist):
           return Response({"error": "Teacher or Class not found"}, status=status.HTTP_404_NOT_FOUND)



    def create_class_period(self, request):
       teacher_id = request.data.get('teacher_id')
       course_id = request.data.get('course_id')
       class_id = request.data.get('class_id')
       start_time = request.data.get('start_time')
       end_time = request.data.get('end_time')
       day_of_week = request.data.get('day_of_week')


       try:
           teacher = Teacher.objects.get(id=teacher_id)
           course = Course.objects.get(id=course_id)
           class_obj = Classes.objects.get(id=class_id)


           class_period = ClassPeriod.objects.create(
               teacher=teacher,
               course=course,
               class_obj=class_obj,
               start_time=start_time,
               end_time=end_time,
               day_of_week=day_of_week
           )
           serializer = ClassPeriodSerializer(class_period)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       except (Teacher.DoesNotExist, Course.DoesNotExist, Classes.DoesNotExist):
           return Response({"error": "Teacher, Course, or Class not found"}, status=status.HTTP_404_NOT_FOUND)
def get_weekly_timetable(self, request):
    class_id = request.data.get('class_id')
    try:
        class_obj = Classes.objects.get(id=class_id)
        class_periods = ClassPeriod.objects.filter(class_obj=class_obj).order_by('day_of_week', 'start_time')
        
        timetable = {}
        for period in class_periods:
            day = period.get_day_of_week_display()
            if day not in timetable:
                timetable[day] = []
            timetable[day].append({
                'course': period.course.name,
                'teacher': period.teacher.name,
                'start_time': period.start_time.strftime('%H:%M'),
                'end_time': period.end_time.strftime('%H:%M')
            })
        
        return Response(timetable, status=status.HTTP_200_OK)
    except Classes.DoesNotExist:
        return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)














class  CourseListView(APIView):
  def get(self,request):
      courses= Course.objects.all()
      serializer = CourseSerializer(Course,many=True)
      return Response(serializer.data)
 
  def post(self, request):
      serializer = ClassesSerializer(data= request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data , status=status.HTTP_201_CREATED)
      else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherListView(APIView):
  def get (self,request):
      teacher = Teacher.objects.all()
      serializer = TeacherSerializer(teacher,many=True)
      return Response(serializer.data)








  def post(self, request):
      serializer = TeacherSerializer(data= request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data , status=status.HTTP_201_CREATED)
      else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class  ClassListView (APIView):
  def get (self,request):
      classes = Classes.objects.all()
      serializer =   ClassesSerializer(classes,many=True)
      return Response(serializer.data)




  def post(self, request):
      serializer = ClassesSerializer(data= request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data , status=status.HTTP_201_CREATED)
      else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodListView(APIView):
  def get (self,request):
      classperiod = ClassPeriod.objects.all()
      serializer = ClassPeriodSerializer(classperiod,many=True)
      return Response(serializer.data)








class StudentDetailView(APIView):
  def get (self, request,id):
      student = Student.objects.get(id = id)
      serializer = StudentSerializer(student)
      return Response(serializer.data)
  def put (self, request,id):
      student = Student.objects.get(id = id)
      serializer = StudentSerializer(student,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, id):
      student = Student.objects.get(id = id)
      student.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
class TeacherDetailView(APIView):
  def get (self, request,id):
      teacher = Teacher.objects.get(id = id)
      serializer = TeacherSerializer(teacher)
      return Response(serializer.data)
  def put (self, request,id):
      teacher = Teacher.objects.get(id = id)
      serializer = TeacherSerializer(teacher,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, id):
      teacher = Teacher.objects.get(id = id)
      teacher.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
class ClassDetailView(APIView):
  def get (self, request,id):
      classes= Classes.objects.get(id = id)
      serializer = ClassesSerializer(classes)
      return Response(serializer.data)
  def put (self, request,id):
      classes = Classes.objects.get(id = id)
      serializer = StudentSerializer(classes,data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, id):
      classes = Classes.objects.get(id = id)
      classes.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, id):
      course = Student.objects.get(id = id)
      course.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  
class ClassroomPeriodDetailView(APIView):
    def get(self, request, id):
        classrom_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classrom_period)
        return Response(serializer.data)

    def put(self, request, id):
        classroom_period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classroom_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classroom_period = ClassPeriod.objects.get(id=id)
        classroom_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)



































