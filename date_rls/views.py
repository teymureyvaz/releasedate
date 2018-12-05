from django.shortcuts import render
from django.contrib.auth.models import User
from date_rls.models import Movie
from django.contrib.auth import get_user_model
from django.views.generic import list
from django.views.generic import edit
from django.views.generic import detail
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect

def movie_list(request):
    user = request.user
    user_movies = []
    if user.is_authenticated:
        user_movies = user.movies.all()
    movies = Movie.objects.all()
    return render(request,'date_rls/movie_list.html',{'user_movies':user_movies,'movies':movies})

def add_to_list(request,pk):
	user =request.user
	movie = Movie.objects.get(id=pk)
	user.movies.add(movie)
	return HttpResponseRedirect(reverse('movie_list'))

def user_movie_list(request,pk):
	user = User.objects.get(id=pk)
	movies = user.movies.all()
	return render(request,'accounts/my_list.html',{'movie_list':movies})

def user_movie_remove(request,pk):
	user = request.user
	movie = Movie.objects.get(id=pk)
	user.movies.remove(movie)
	return HttpResponseRedirect(reverse('my_list',args=(request.user.pk, )))
