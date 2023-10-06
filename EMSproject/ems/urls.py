from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePageView, name="home"),
     path("aregistration/", views.aregistration, name="aregistration"),
       path("adminloginpage/", views.adminloginpage, name="adminloginpage"),
         path("uregistration/", views.uregistration, name="uregistration"),
           path("userloginpage/", views.userloginpage, name="userloginpage"),
           path("userDashboard/", views.userDashboard, name="userDashboard"),
]