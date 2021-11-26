from threading import active_count
from django.shortcuts import render, redirect
from movie_recommendor import Movie_recommendation, imdb, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    popular= imdb.popular_movies()
    trending= imdb.trending()
    return render(request,'index.html',{'popular':popular,'trending':trending})


def result(request):
    watched= request.GET['watched']
    NA= 'NA'
    searched_movie= imdb.search(watched)
    s_title= searched_movie[0]['original_title']
    s_overview= searched_movie[0]['overview']
    s_poster= 'https://image.tmdb.org/t/p/w500'+searched_movie[0]['poster_path']
    s_released= searched_movie[0]['release_date']
    actors= imdb.actors(s_title)


    try:
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
                                            'imdbrating':imdbrating,'boxoffice':boxoffice,'recommended_movies':rec_mov,'actors':actors})

    except:
        recommended_movies= imdb.rec(s_title)
        rec_mov= []
        for movies in recommended_movies:
            mov= imdb.movieinfo(movies['original_title'])
            rec_mov.append(mov)
        return  render(request,'result.html',{'title':s_title,'release_date':s_released,'genre':NA,'director':NA,'plot':s_overview,
                                            'awards':NA,'poster':s_poster,'rotten_tomatoes':NA,'metacritic':NA,
                                            'imdbrating':NA,'boxoffice':NA,'recommended_movies':rec_mov,'actors':actors})


def seemore(request, movie_name):
    watched= movie_name
    context={'movie_name':movie_name}
    NA= 'NA'
    searched_movie= imdb.search(watched)
    s_title= searched_movie[0]['original_title']
    s_overview= searched_movie[0]['overview']
    s_poster= 'https://image.tmdb.org/t/p/w500'+searched_movie[0]['poster_path']
    s_released= searched_movie[0]['release_date']
    actors= imdb.actors(s_title)
    try:
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
                                            'imdbrating':imdbrating,'boxoffice':boxoffice,'recommended_movies':rec_mov,'actors':actors})

    except:
        recommended_movies= imdb.rec(s_title)
        rec_mov= []
        for movies in recommended_movies:
            mov= imdb.movieinfo(movies['original_title'])
            rec_mov.append(mov)
        return  render(request,'result.html',{'title':s_title,'release_date':s_released,'genre':NA,'director':NA,'plot':s_overview,
                                            'awards':NA,'poster':s_poster,'rotten_tomatoes':NA,'metacritic':NA,
                                            'imdbrating':NA,'boxoffice':NA,'recommended_movies':rec_mov, 'actors':actors})

def register(request):
    form= forms.RegisterForm()
    if request.method=='POST':
        form= forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registeration successful, login to continue')
            return redirect('login')
    context={'form':form}
    return render(request, 'register.html', context=context)


def login(request):
    return render(request,'login.html')