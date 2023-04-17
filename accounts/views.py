from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from accounts.forms import CustomAuthenticationForm
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'contract/login.html'
    authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy("index")

