from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from .models import Movie
# from django.http import HttpResponse

# def home(req):
#     return HttpResponse("Hello, world.")

def home(req):
    data={
        'Name':'sunil',
        'Qualifictaion':'M.tech'
    }
    return render(req,'index.html',data)

def home1(req):
    return redirect('https://www.google.co.in/')

def movie_list(req):
    movies = Movie.objects.all()
    print(movies)
    print(movies.values())
    data={
        'movies':list(movies.values())
    }
    print(data)
    return JsonResponse(data)

def movie_details(req,pk):
    movie = Movie.objects.get(pk=pk)
    data={
        'movie_name':movie.name,
        'desc':movie.description,
        'active':movie.active,
    }
    return JsonResponse(data)
