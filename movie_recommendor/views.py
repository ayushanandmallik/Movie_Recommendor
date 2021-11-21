from django.shortcuts import render
from movie_recommendor import Movie_recommendation, imdb
import pandas as pd


def home(request):
    return render(request,'index.html')


def result(request):
    watched= request.GET['watched']

    searched_movie= imdb.search(watched)
    s_title= searched_movie[0]['original_title']
    s_overview= searched_movie[0]['overview']
    s_poster= 'https://image.tmdb.org/t/p/w500'+searched_movie[0]['poster_path']
    s_released= searched_movie[0]['release_date']

    mov= imdb.movieinfo(s_title)
    genre= mov['genre']
    director= mov['director']
    awards= mov['awards']
    rotten_tomatoes= mov['ratings'][1]['Value']
    metacritic= mov['metascore']
    imdbrating= mov['imdbrating']
    boxoffice= mov['boxoffice']

    recommended_movies= imdb.rec(s_title)
    rec_mov= []
    for movies in recommended_movies:
        mov= imdb.movieinfo(movies['original_title'])
        rec_mov.append(mov)


    return  render(request,'result.html',{'title':s_title,'release_date':s_released,'genre':genre,'director':director,'plot':s_overview,
                                          'awards':awards,'poster':s_poster,'rotten_tomatoes':rotten_tomatoes,'metacritic':metacritic,
                                          'imdbrating':imdbrating,'boxoffice':boxoffice,'recommended_movies':rec_mov})


def seemore(request, movie_name):
    watched= movie_name
    context={'movie_name':movie_name}

    searched_movie= imdb.search(watched)
    s_title= searched_movie[0]['original_title']
    s_overview= searched_movie[0]['overview']
    s_poster= 'https://image.tmdb.org/t/p/w500'+searched_movie[0]['poster_path']
    s_released= searched_movie[0]['release_date']

    mov= imdb.movieinfo(s_title)
    genre= mov['genre']
    director= mov['director']
    awards= mov['awards']
    rotten_tomatoes= mov['ratings'][1]['Value']
    metacritic= mov['metascore']
    imdbrating= mov['imdbrating']
    boxoffice= mov['boxoffice']

    recommended_movies= imdb.rec(s_title)
    rec_mov= []
    for movies in recommended_movies:
        mov= imdb.movieinfo(movies['original_title'])
        rec_mov.append(mov)


    return  render(request,'result.html',{'title':s_title,'release_date':s_released,'genre':genre,'director':director,'plot':s_overview,
                                          'awards':awards,'poster':s_poster,'rotten_tomatoes':rotten_tomatoes,'metacritic':metacritic,
                                          'imdbrating':imdbrating,'boxoffice':boxoffice,'recommended_movies':rec_mov})


def genre(request):
    g= request.GET['genre']
    return render(request, 'genre.html',{'genre':g})