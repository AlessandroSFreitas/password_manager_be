from django.urls import path
from login import views


urlpatterns = [
    path('login/', views.LoginViewSet.as_view({"get": "retrieve"}), name="login"),
    path('home/', views.LoginViewSet.as_view({"post": "create"}), name="home"),
]
