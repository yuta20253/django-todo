from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy

# Create your views here.
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy("dashboard")

class DashBoardView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/dashboard.html"
    login_url = "login"
