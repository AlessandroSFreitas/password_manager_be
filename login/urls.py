from django.urls import path
from login import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('home/', views.HomeView.as_view(), name="home"),
]
