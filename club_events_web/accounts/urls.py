from django.urls import path, include
from . import views
urlpatterns = [
    path('', include('allauth.urls')),
    path('', views.login, name="login"),
    path('signUP/', views.signUP, name="signUP"),
    path('logout/', views.signUP, name="logout"),
]