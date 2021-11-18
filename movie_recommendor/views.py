from django.shortcuts import render
from movie_recommendor import Movie_recommendation
import pandas as pd


def home(request):
    return render(request,'index.html')

def result(request):
    watched= request.GET['watched']

    res= Movie_recommendation.get_movie_recommendation(watched)
    #res= result.to_html()
    mov= []
    for i in res:
        mov.append(i['Title'])
    return  render(request,'result.html',{'result':mov})



