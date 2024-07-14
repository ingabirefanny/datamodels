from django.shortcuts import render
from restf_ramework.views import APIView
from student.models import StudentSerializer
from rest_framework.response import response
from .views import StudentViewList

class StudentListView (APIView):
    def get (self,request):
        students = student.objects.all()
        serializer= StudenSerialize(students,many=True)
        return Response (serializer.data)
    
    