
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("load/", views.load, name="load"),
    path("summary/", views.summary, name="summary"),
]
