from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    http_method_names = ['post', 'get']
    template_name = 'users/logout.html'

@user_passes_test(lambda user: user.is_staff)
def staff_only_view(request):
    return render(request, 'users/staff.html')