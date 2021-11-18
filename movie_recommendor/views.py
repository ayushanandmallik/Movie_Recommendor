from django.shortcuts import render
from movie_recommendor import Movie_recommendation


def home(request):
    return render(request,'index.html')

def result(request):
    watched= request.GET['watched']

    res= Movie_recommendation.get_movie_recommendation(watched)


    return  render(request,'result.html',{'result':res})



