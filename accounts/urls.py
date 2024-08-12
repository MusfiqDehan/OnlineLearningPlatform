from django.urls import path, include
from .views import student_signup, instructor_signup, CustomLoginView, logout_view, student_google_login, instructor_google_login

urlpatterns = [
    path('signup/student/', student_signup, name='student_signup'),
    path('signup/instructor/', instructor_signup, name='instructor_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('student-google/', student_google_login, name='student_google_login'),
    path('instructor-google/', instructor_google_login,
         name='instructor_google_login'),
    path('', include('allauth.urls')),
]
