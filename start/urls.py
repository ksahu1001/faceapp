from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("videoapp/", views.video, name="videoapp"),
    path("videoapp/confo/<roomid>/<usertype>/<userref>", views.confo, name="room"),


]