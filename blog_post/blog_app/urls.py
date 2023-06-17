from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("",views.default),
   path("home/",views.home, name="homepage"),
   path("explore/<id>",views.explore, name="explore_content"),
   path("getone/<id>",views.get_one,name="view_one"),

]
