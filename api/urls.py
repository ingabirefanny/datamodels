from django.urls import path

from api.views import ClassPeriodDetailView, ClassPeriodListView, CourseDetailView, StudentDetailView, StudentListView, TeacherDetailView, TeacherListView , CourseListView
urlpatterns=[
    path('student/',StudentListView.as_view(),name="student_list_view"),
    path('classperiod/',ClassPeriodListView.as_view(),name='classperiod_list_view'),
    path('course/',CourseListView.as_view(),name='course_list_view'),
    path('teacher/',TeacherListView.as_view(),name='teacher_list_view'),
    path("student/<int:id>" , StudentDetailView.as_view(),name="student_detail_view"),
    path("classperiod/<int:id>" , ClassPeriodDetailView.as_view(),name="classPeriod_detail_view"),
    path("course/<int:id>" , CourseDetailView.as_view(),name="course_detail_view"),
    path("teacher/<int:id>" , TeacherDetailView.as_view(),name="teacher_detail_view"),

]