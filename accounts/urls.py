from django.urls import path
from .views import student_signup, instructor_signup, CustomLoginView, logout_view

urlpatterns = [
    path('signup/student/', student_signup, name='student_signup'),
    path('signup/instructor/', instructor_signup, name='instructor_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
