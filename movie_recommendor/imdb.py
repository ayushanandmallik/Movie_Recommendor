from omdbapi.movie_search import GetMovie
from tmdbv3api import TMDb
from tmdbv3api import Movie
import os
from dotenv import load_dotenv


load_dotenv()

omdb_api_key= os.getenv('omdb_api_key')
tmdb_api_key= os.getenv('tmdb_api')

omdb_m= GetMovie(api_key=omdb_api_key)


def reverse_string(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

def movieinfo(name):
    return omdb_m.get_movie(name)



tmdb= TMDb()
tmdb.api_key= tmdb_api_key

tmdb.language= 'en'
tmdb.debug= True

movie= Movie()
def search(m):
    return movie.search(m)

def rec(m):
    s= search(m)
    r= movie.recommendations(s[0]['id'])
    recommended_movies=[]
    for i in r:
        recommended_movies.append(i['title'])
    return r

def popular_movies():
    popular= movie.popular()
    pm=[]
    for movies in popular:
        pm.append({'title':movies['original_title'], 'poster':movies['poster_path']})
    return pm

print(popular_movies())


