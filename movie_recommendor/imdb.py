from omdbapi.movie_search import GetMovie
from tmdbv3api import TMDb
from tmdbv3api import Movie
import os
from dotenv import load_dotenv
import requests
import json
import time


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
    for i in range(10):
        pm.append({'title':popular[i]['original_title'], 'poster':movieinfo(popular[i]['original_title'])['poster']})
    return pm


def actors(m):
    s= search(m)[0]['id']
    a= movie.credits(s)
    res=[]
    
    for cr in a['cast']:
        if cr['known_for_department']=='Acting':
            res.append({'actor':cr['name'],'picture':cr['profile_path']})
    
    no_of_actor= len(res)
    if no_of_actor<=10:
        return res
    return res[:10]
    

tmdb_api= requests.Session()
tmdb_api.params= {'api_key':tmdb_api_key}

def trending():
    url= 'https://api.themoviedb.org/3/trending/movie/day?api_key='+tmdb_api_key
    movies=[]
    j= tmdb_api.get(url)
    json_response= json.loads(j.text)
    
    m= json_response['results']
    tr=[]
    for i in range(10):
        tr.append({'title':m[i]['original_title'], 'poster':movieinfo(m[i]['original_title'])['poster']})
    return tr

#print(trending())
#print(actors('eternals'))
#print(actor_img('/k3W1XXddDOH2zibPkNotIh5amHo.jpg'))


