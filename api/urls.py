from django.urls import path


from api.views import  ClassPeriodListView, CourseListView, StudentDetailView,  TeacherDetailView, TeacherListView 
urlpatterns=[

    path('classperiod/',ClassPeriodListView.as_view(),name='classperiod_list_view'),
    path('course/',CourseListView.as_view(),name='course_list_view'),
    path('teacher/',TeacherListView.as_view(),name='teacher_list_view'),
    path("student/<int:id>" , StudentDetailView.as_view(),name="student_detail_view"),
    path("course/<int:id>" ,CourseListView .as_view(),name="course_detail_view"),
    

]