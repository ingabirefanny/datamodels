# from rest_framework import serializers
# from course.models import Course
# from student.models import Student
# from ClassPeriod.models import ClassPeriod
# from teacher.models import Teacher
# from classes.models import Classes

# class MinimalCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = ['id', 'name']

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = "__all__"

# class MinimalStudentSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()

#     def get_full_name(self, obj):
#         return f"{obj.first_name} {obj.last_name}"

#     class Meta:
#         model = Student
#         fields = ["id", "full_name", "email"]

# class StudentSerializer(serializers.ModelSerializer):
#     courses = CourseSerializer(many=True)

#     class Meta:
#         model = Student
#         fields = "__all__"

# class MinimalClassPeriodSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()

#     def get_full_name(self, obj):
#         return f"{obj.teacher.first_name} {obj.teacher.last_name}"

#     class Meta:
#         model = ClassPeriod
#         fields = ["id", "full_name", "course_id"]

# class ClassPeriodSerializer(serializers.ModelSerializer):
#     teacher = TeacherSerializer()
#     course = CourseSerializer()

#     class Meta:
#         model = ClassPeriod
#         fields = "__all__"

# class MinimalTeacherSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()

#     def get_full_name(self, obj):
#         return f"{obj.first_name} {obj.last_name}"

#     class Meta:
#         model = Teacher
#         fields = ["id", "full_name", "email", "years_of_experience"]

# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = "__all__"

# class MinimalClassesSerializer(serializers.ModelSerializer):
#     full_name = serializers.SerializerMethodField()

#     def get_full_name(self, obj):
#         return f"{obj.first_name} {obj.last_name}"

#     class Meta:
#         model = Classes
#         fields = ["id", "full_name", "email"]

# class ClassesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Classes
#         fields = "__all__"

from rest_framework import serializers
from classes.models import Classes
from ClassPeriod.models import ClassPeriod
from classes.models import Classes
from course.models import Course
from student.models import Student
from teacher.models import Teacher


class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=["id","title","course_code","number_of_topics","duration"]
class MinimalStudentSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Student
        fields=["id","full_name","email"]

class CourseSerializer(serializers.ModelSerializer):
    # teachers = TeacherSerializer(many=True)
    class Meta:
        model =Course
        fields = "__all__"
class StudentSerializer(serializers.ModelSerializer):
    coursename=CourseSerializer(many=True)
    class Meta:
        model =Student
        fields= "__all__"
class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classes
        fields=["id","class_name"]
class ClassroomSerializer(serializers.ModelSerializer):
    students = MinimalStudentSerializer(many=True)
    # teacher=TeacherSerializer(many=True)
    class Meta:
        model =Classes
        fields = "__all__"
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassPeriod
        fields=["id","start_time","end_time"]
class ClassPeriodSerializer(serializers.ModelSerializer):
    # teacher = TeacherSerializer()
    course = CourseSerializer()
    class Meta:
        model =ClassPeriod
        fields = "__all__"

class MinimalTeacherSerializer(serializers.ModelSerializer):
    full_name=serializers.SerializerMethodField()
    def get_full_name(self,object):
        return f"{object.first_name} {object.last_name}"
    class Meta:
        model=Teacher
        fields=["id","full_name","email","years-of-experience"]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model =Teacher
        fields = "__all__"        