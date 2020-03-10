from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'(?P<club_name>[\w.@+-]+)/$', views.club, name="club"),
]