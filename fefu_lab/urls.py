from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('student_detail/', views.student_detail, name='student_detail'),
    path('course_detail/', views.course_detail, name='course_detail'),
]
