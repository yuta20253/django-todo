from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, DashBoardView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("dashboard/", DashBoardView.as_view(), name="dashboard")
]
