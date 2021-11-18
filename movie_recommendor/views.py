from django.shortcuts import render
from movie_recommendor import Movie_recommendation, imdb
import pandas as pd


def home(request):
    return render(request,'index.html')

def result(request):
    watched= request.GET['watched']

    res= Movie_recommendation.get_movie_recommendation(watched)
    movie= ''
    for s in res[0]['Title']:
        if s=='(':
            break
        movie= movie+s

    mov= imdb.movieinfo(movie)
    title= mov['title']
    release_date= mov['released']
    genre= mov['genre']
    director= mov['director']
    plot= mov['plot']
    awards= mov['awards']
    poster= mov['poster']
    rotten_tomatoes= mov['ratings'][1]['Value']
    metacritic= mov['metascore']
    imdbrating= mov['imdbrating']
    boxoffice= mov['boxoffice']

    return  render(request,'result.html',{'title':title,'release_date':release_date,'genre':genre,'director':director,'plot':plot,
                                          'awards':awards,'poster':poster,'rotten_tomatoes':rotten_tomatoes,'metacritic':metacritic,
                                          'imdbrating':imdbrating,'boxoffice':boxoffice})



