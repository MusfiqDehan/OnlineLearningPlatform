from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import StudentSignUpForm, InstructorSignUpForm
from .models import User

# Custom Login View


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('course_list')

    def get_success_url(self):
        return self.success_url

# Logout View


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('course_list')

# Student Sign Up View


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/student_signup.html', {'form': form, 'user_type': 'student'})

# Instructor Sign Up View


def instructor_signup(request):
    if request.method == 'POST':
        form = InstructorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('course_list')
    else:
        form = InstructorSignUpForm()
    return render(request, 'accounts/instructor_signup.html', {'form': form, 'user_type': 'instructor'})
