#from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from . import forms, models  # <- after creating forms


# 3 - Login
class NewLoginView(LoginView):
    # before forms -> form_class = AuthenticationForm
    form_class = forms.LoginForm
    success_url = "/users/"
    template_name = "login.html"

# 1 - Register
class RegisterView(CreateView):
    #before forms ->  form_class = UserCreationForm
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = "/users/"

# 2 - created Users list
class UserListView(ListView):
    #before custom models -> queryset = User.objects.all()
    queryset = models.CustomUser.objects.all()
    template_name = "user_list.html"

    def get_queryset(self):
        return self.queryset