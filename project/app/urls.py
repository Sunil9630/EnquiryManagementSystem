
from django.urls import path
# from . import views
from . views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('home1/',home1,name='home1'),
    path('json/',movie_list,name='movie_list'),
    path('movie_details/<int:pk>/',movie_details,name='movie_details'),
    # path('',home,name='home')
]