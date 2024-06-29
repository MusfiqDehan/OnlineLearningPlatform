from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),

    # Course URLs
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/<int:pk>/update/', views.course_update, name='course_update'),
    path('course/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('course/<int:pk>/enroll/', views.enroll_course, name='enroll_course'),
    path('course/<int:course_pk>/lessons/',
         views.lesson_list, name='lesson_list'),
    path('course/<int:course_pk>/lesson/<int:lesson_pk>/',
         views.lesson_detail, name='lesson_detail'),
    path('course/<int:course_pk>/lesson/<int:lesson_pk>/complete/',
         views.mark_lesson_complete, name='mark_lesson_complete'),

    # Lesson URLs
    path('course/<int:course_pk>/lesson/create/',
         views.lesson_create, name='lesson_create'),
    path('course/<int:course_pk>/lesson/<int:pk>/update/',
         views.lesson_update, name='lesson_update'),
    path('course/<int:course_pk>/lesson/<int:pk>/delete/',
         views.lesson_delete, name='lesson_delete'),
]
