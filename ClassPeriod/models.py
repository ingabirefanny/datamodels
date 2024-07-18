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
    


#     class StudentListView(APIView):
#     def get (self,request):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status= status.HTTP_400_CREATED)
# class StudentDetailView(APIView):
#     def get(self,request, id):
#         student= Student.objects.get(id=id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#     def put(self,request,id):
#         student=Student.objects.get(id=id)
#         serializer=StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,id):
#         student=Student.objects.get(id=id)
#         student.delete()
#         return Response(status=status.HTTP_202_ACCEPTED)