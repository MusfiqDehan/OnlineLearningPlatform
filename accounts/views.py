import logging
from django.contrib.auth import login
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from .forms import StudentSignUpForm, InstructorSignUpForm
from .models import User

logger = logging.getLogger(__name__)


def student_google_login(request):
    logger.info("student_google_login view called")
    request.session['user_type'] = 'student'
    return redirect(reverse('google_login'))


def instructor_google_login(request):
    logger.info("instructor_google_login view called")
    request.session['user_type'] = 'instructor'
    return redirect(reverse('google_login'))


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


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('course_list')

    def get_success_url(self):
        return self.success_url


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('course_list')
